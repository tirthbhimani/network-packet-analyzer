import requests
from flask import Flask, jsonify
from flask_cors import CORS
from scapy.all import sniff, IP, TCP, UDP, ICMP, DNS, DNSQR
from datetime import datetime
import threading

app = Flask(__name__)
CORS(app)

packets = []
capturing = False

def process_packet(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = "OTHER"
        info = ""

        if TCP in packet:
            protocol = "TCP"
            info = f"Port {packet[TCP].sport} → {packet[TCP].dport}"
        elif UDP in packet:
            protocol = "UDP"
            info = f"Port {packet[UDP].sport} → {packet[UDP].dport}"
        elif ICMP in packet:
            protocol = "ICMP"
            info = "Ping packet"

        if DNS in packet and DNSQR in packet:
            protocol = "DNS"
            info = f"Query: {packet[DNSQR].qname.decode()}"

        packet_data = {
            "timestamp": datetime.now().strftime("%H:%M:%S"),
            "protocol": protocol,
            "src_ip": src_ip,
            "dst_ip": dst_ip,
            "info": info
        }
        packets.append(packet_data)

        # Keep only last 100 packets in memory
        if len(packets) > 100:
            packets.pop(0)

def start_sniffing():
    sniff(prn=process_packet, store=False)

@app.route("/api/start", methods=["GET"])
def start_capture():
    global capturing
    if not capturing:
        capturing = True
        thread = threading.Thread(target=start_sniffing, daemon=True)
        thread.start()
        return jsonify({"status": "Capture started"})
    return jsonify({"status": "Already running"})

@app.route("/api/packets", methods=["GET"])
def get_packets():
    return jsonify(packets)

@app.route("/api/stats", methods=["GET"])
def get_stats():
    stats = {"TCP": 0, "UDP": 0, "DNS": 0, "ICMP": 0, "OTHER": 0}
    for p in packets:
        proto = p["protocol"]
        if proto in stats:
            stats[proto] += 1
        else:
            stats["OTHER"] += 1
    return jsonify(stats)

@app.route("/api/geoip/<ip>", methods=["GET"])
def get_geoip(ip):
    try:
        # Skip private IPs
        private_ranges = ["192.168.", "10.", "172.16.", "127.", "224.", "239."]
        if any(ip.startswith(r) for r in private_ranges):
            return jsonify({
                "ip": ip,
                "country": "Private Network",
                "city": "LAN",
                "isp": "Local",
                "lat": 0, "lon": 0,
                "flag": "🏠"
            })

        res = requests.get(f"http://ip-api.com/json/{ip}?fields=country,city,isp,lat,lon,countryCode", timeout=5)
        data = res.json()
        return jsonify({
            "ip": ip,
            "country": data.get("country", "Unknown"),
            "city": data.get("city", "Unknown"),
            "isp": data.get("isp", "Unknown"),
            "lat": data.get("lat", 0),
            "lon": data.get("lon", 0),
            "flag": f"https://flagcdn.com/24x18/{data.get('countryCode','').lower()}.png"
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
