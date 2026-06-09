# 🔍 NetWatch — Network Packet Analyzer

A real-time network packet analyzer built with Python (Scapy + Flask) and a custom cyberpunk-style dashboard. Captures live network traffic, detects suspicious activity, and generates PDF reports.

---

## 🖥️ Dashboard Preview
<img width="1917" height="963" alt="image" src="https://github.com/user-attachments/assets/debcb489-4864-43ed-be74-7c1835e2b00e" />
<img width="1857" height="842" alt="image" src="https://github.com/user-attachments/assets/ee4ccd36-0709-4a8a-b54f-3af710597d15" />




---

## ✨ Features

- **Live Packet Capture** — Real-time TCP, UDP, DNS, ICMP traffic monitoring
- **Protocol Distribution** — Visual donut chart showing traffic breakdown
- **Suspicious Activity Detection** — Auto-detects port scans, ping floods, suspicious ports (Metasploit, RDP, Telnet)
- **IP Geolocation** — Lookup any IP to find country, city, ISP
- **Top IP Addresses** — See which IPs are most active on your network
- **PDF Export** — Download full session report with one click

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Packet Capture | Python + Scapy |
| Backend | Python Flask |
| Frontend | HTML, CSS, JavaScript |
| Charts | Chart.js |
| Geolocation | ip-api.com |
| PDF Export | jsPDF + AutoTable |

---

## 🚀 Setup & Run

### Requirements
- Kali Linux / Ubuntu
- Python 3.x
- Root/sudo access (required for packet capture)

### One-click setup:
```bash
git clone https://github.com/YOURUSERNAME/network-packet-analyzer.git
cd network-packet-analyzer
sudo bash setup.sh
```

### Manual setup:
```bash
# Install dependencies
sudo pip3 install flask flask-cors scapy requests --break-system-packages

# Start backend
sudo python3 backend/app.py

# Open dashboard in new terminal
firefox frontend/index.html
```

---

## 📡 Generate Test Traffic

```bash
# DNS traffic
nslookup google.com

# ICMP ping
ping -c 5 8.8.8.8

# HTTP traffic
curl http://example.com
```

---

## ⚠️ Disclaimer

This tool is for educational purposes and authorized network monitoring only.
Never use on networks you don't own or have permission to monitor.

---

## 👨‍💻 Author

**Tirth Bhimani** — B.Tech Computer Engineering, Semester 5
Aditya Silver Oak Institute of Technology, Ahmedabad

> Built as a cybersecurity internship portfolio project
