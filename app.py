import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
import time

# --- CONFIGURATION ---
# Symbols to track (Yahoo Finance tickers)
# Append -USD for crypto. Use standard tickers for stocks.
SYMBOLS = ["BTC-CAD", "ETH-CAD", "SOL-CAD", "AAPL", "GD", "BRK-B", "XOM", "SPY"]
REFRESH_RATE = 60 # Refresh interval in seconds

# Page Setup (Wide Mode)
st.set_page_config(page_title="Market Sentinel", layout="wide", page_icon="📈")

# Custom CSS for Styling
st.markdown("""
<style>
    .metric-card {
        background-color: #1E1E1E;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #333;
        margin-bottom: 10px;
    }
    .stApp { background-color: #0E1117; }
</style>
""", unsafe_allow_html=True)

st.title("📡 Market Sentinel | Live Dashboard")

# Main Loop (Auto-Refresh)
placeholder = st.empty()

while True:
    with placeholder.container():
        # Fetch Data
        try:
            data = yf.download(SYMBOLS, period="1d", interval="5m", progress=False)
            
            # Create Columns
            cols = st.columns(len(SYMBOLS))
            
            for i, symbol in enumerate(SYMBOLS):
                with cols[i]:
                    # Calculate Price and Change
                    try:
                        # Handle multi-index columns from yfinance
                        current_price = data['Close'][symbol].iloc[-1]
                        open_price = data['Open'][symbol].iloc[0]
                        change = ((current_price - open_price) / open_price) * 100
                        
                        # Determine Color and Arrow
                        color = "#4CAF50" if change >= 0 else "#FF5252" # Green or Red
                        arrow = "▲" if change >= 0 else "▼"
                        
                        # Render Card
                        st.markdown(f"""
                        <div class="metric-card">
                            <h3 style="margin:0; color:#aaa;">{symbol}</h3>
                            <h2 style="margin:0; color:{color};">${current_price:.2f}</h2>
                            <p style="margin:0; color:{color};">{arrow} {change:.2f}%</p>
                        </div>
                        """, unsafe_allow_html=True)
                        
                    except Exception as e:
                        st.error(f"Error fetching {symbol}")
            
            st.caption(f"Last Updated: {time.strftime('%H:%M:%S')}")
            
        except Exception as e:
            st.error("Waiting for connection or API limit...")
            
        # Wait for next update
        time.sleep(REFRESH_RATE)