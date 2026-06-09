from scapy.all import sniff, IP, TCP, UDP, ICMP, DNS, DNSQR
from datetime import datetime

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

        # DNS detection
        if DNS in packet and DNSQR in packet:
            protocol = "DNS"
            info = f"Query: {packet[DNSQR].qname.decode()}"

        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] {protocol} | {src_ip} → {dst_ip} | {info}")

print("Starting packet capture... (Ctrl+C to stop)")
sniff(prn=process_packet, store=False, count=50)
