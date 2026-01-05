# 📡 Market Sentinel  
### Live Crypto & Stock Dashboard (Raspberry Pi)

This project is a lightweight **live market dashboard** built with **Streamlit**, designed to run smoothly on a **Raspberry Pi**.

It tracks selected **cryptocurrencies and stocks** in near real-time using Yahoo Finance data and displays price changes in a clean, readable dashboard format.

This repo is part of my personal IT journey notes and small experiments.  
I’ve been building things like this since 2019 to understand systems by actually running them.

If you notice something wrong or something that could be done better, feel free to reach out or open an issue.

---

## ✅ What this app does

- Tracks **crypto & stock prices** (BTC, ETH, SOL, AAPL, TSLA by default)
- Pulls live data from **Yahoo Finance**
- Calculates **daily percentage change**
- Displays everything in a **dark-themed Streamlit dashboard**
- Auto-refreshes every **60 seconds**
- Designed to run **24/7 on Raspberry Pi**

---

## 🧰 Tech Stack

- **Python 3**
- **Streamlit** – UI / dashboard
- **yfinance** – market data
- **pandas** – data handling
- **plotly** – charting support (future-ready)

---

## 🖥️ Target Environment

This project is written and tested primarily for:

- **Raspberry Pi 4 / 5**
- **Raspberry Pi OS (64-bit recommended)**
- Linux terminal usage

> It will also run on macOS or Linux PCs, but Raspberry Pi is the intended environment.

---

## 🧱 Prerequisites

### Hardware
- Raspberry Pi (4 or newer recommended)
- Internet connection
- microSD card with Raspberry Pi OS installed

## 🧱 Software Setup

Make sure your system is up to date:

```bash
sudo apt update && sudo apt upgrade -y
Check Python version:

bash
Copy code
python3 --version
Python 3.9+ is recommended.
```
📥 Clone the Repository
Go to a directory where you keep your projects:

```bash
Copy code
cd ~
Clone the repository (replace with your actual GitHub repo URL):
```
bash
Copy code
git clone https://github.com/YOUR_GITHUB_USERNAME/market-sentinel.git
cd market-sentinel
📦 Install Required Packages
It’s strongly recommended to use a virtual environment on Raspberry Pi.

1️⃣ Create a virtual environment
bash
Copy code
python3 -m venv venv
2️⃣ Activate it
bash
Copy code
source venv/bin/activate
You should now see (venv) in your terminal.

3️⃣ Upgrade pip
bash
Copy code
pip install --upgrade pip
4️⃣ Install dependencies
bash
Copy code
pip install streamlit yfinance pandas plotly
▶️ Run the App
From inside the project folder:

bash
Copy code
streamlit run app.py
Replace app.py with the actual filename if different.

After running the command, Streamlit will show something like:

text
Copy code
Local URL: http://localhost:8501
Network URL: http://192.168.1.xxx:8501
🌐 Access from Another Device (Optional)
If your Raspberry Pi is on the same network, open a browser and go to:

cpp
Copy code
http://RASPBERRY_PI_IP:8501
Perfect for:

Wall dashboards

Old tablets

Always-on monitors
