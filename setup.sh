#!/bin/bash
echo "==============================="
echo "  NetWatch - Packet Analyzer"
echo "  Setup Script"
echo "==============================="

echo "[1/3] Installing dependencies..."
sudo pip3 install flask flask-cors scapy --break-system-packages

echo "[2/3] Starting backend..."
sudo python3 backend/app.py &
sleep 2

echo "[3/3] Opening dashboard..."
xdg-open frontend/index.html

echo "==============================="
echo "  NetWatch is running!"
echo "  Backend: http://localhost:5000"
echo "==============================="
