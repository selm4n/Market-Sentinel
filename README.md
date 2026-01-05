# 📡 Market Sentinel
### Live Crypto & Stock Dashboard (Raspberry Pi)

Personal notes & experiments from my IT journey since 2019.

This project is a lightweight live market dashboard built with Streamlit, designed to run smoothly on a Raspberry Pi.
It tracks selected cryptocurrencies and stocks using Yahoo Finance data and displays them in a clean, always-on dashboard.

If you notice something wrong or have a better way to do it, feel free to reach out or open an issue.

---

## ✅ What this app does

- Tracks crypto and stock prices (BTC, ETH, SOL, AAPL, TSLA by default)
- Pulls live data from Yahoo Finance
- Calculates daily percentage change
- Dark-themed Streamlit dashboard
- Auto-refreshes every 60 seconds
- Designed to run 24/7 on Raspberry Pi

---

## 🧰 Tech Stack

- Python 3
- Streamlit
- yfinance
- pandas
- plotly

---

## 🖥️ Target Environment

- Raspberry Pi 4 / 5
- Raspberry Pi OS (64-bit recommended)
- Linux terminal usage

This app may run on other platforms, but Raspberry Pi is the primary target.

---

## 🧱 Software Setup

Update the system:

```bash
sudo apt update && sudo apt upgrade -y
```

Check Python version:

```bash
python3 --version
```

Python 3.9+ is recommended.

---

## 📥 Clone the Repository

Go to your home directory:

```bash
cd ~
```

Clone the repository:

```bash
git clone https://github.com/selm4n/market-sentinel.git
cd market-sentinel
```

---

## 📦 Install Required Packages

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

Upgrade pip:

```bash
pip install --upgrade pip
```

Install dependencies:

```bash
pip install streamlit yfinance pandas plotly
```

---

## ▶️ Run the App

From inside the project folder:

```bash
streamlit run app.py
```

Replace `app.py` with the actual filename if different.

After running the command, Streamlit will show something like:

```text
Local URL: http://localhost:8501
Network URL: http://192.168.1.xxx:8501
```

---

## 🌐 Access from Another Device

If your Raspberry Pi is on the same network, open a browser and go to:

```text
http://RASPBERRY_PI_IP:8501
```

Perfect for wall dashboards, old tablets, and always-on monitors.

---

## ⚙️ Configuration

Inside the script:

```python
SYMBOLS = ["BTC-USD", "ETH-USD", "SOL-USD", "AAPL", "TSLA"]
REFRESH_RATE = 60
```

- Crypto symbols use `-USD` (example: AVAX-USD)
- Stocks use standard tickers (example: MSFT, NVDA)
- Refresh rate is in seconds

---

## ⚠️ Notes & Limitations

- Yahoo Finance may rate-limit excessive requests
- Very short refresh intervals may cause temporary errors
- This app is for monitoring, not trading

---

## 🧠 Why Raspberry Pi?

- Low power consumption
- Silent operation
- Perfect for always-on dashboards
- Great excuse to keep a Pi doing something useful

---

📍 Built as part of my Field Notes on IT
