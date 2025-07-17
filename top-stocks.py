from yahooquery import Screener
import pandas as pd
import streamlit as st
import time

st.subheader("Biotech Stock Screener price under $20")

# get stocks from screener
def fetch_stocks():
    screener = Screener()
    data = screener.get_screeners("biotechnology")
    quotes = data.get("biotechnology", {}).get("quotes", [])
    if not quotes:
        return pd.DataFrame()

    df = pd.DataFrame(quotes)
    
    # Filter for stocks under $10
    df = df[df["regularMarketPrice"] < 20]
    
    return df 

# Display stocks
stocks = fetch_stocks()
if stocks.empty:
    st.write("No stocks found under $20.")  
else:
    # Select relevant columns
    stocks = stocks[["symbol", "shortName", "regularMarketPrice", "regularMarketChange", "regularMarketChangePercent", "regularMarketVolume"]]
    stocks.rename(columns={
        "symbol": "Ticker",
        "shortName": "Name",
        "regularMarketPrice": "Price",
        "regularMarketChange": "Change",
        "regularMarketChangePercent": "% Change",
        "regularMarketVolume": "Volume"
    }, inplace=True)

    # Add conditional formatting
    def highlight_change(val):
        try:
            if val.startswith('+'):
                return 'color: green; font-weight: bold'
            elif val.startswith('-'):
                return 'color: red; font-weight: bold'
        except:
            pass
        return ''

    styled_df = stocks.style.map(highlight_change, subset=["% Change"])
    
    st.dataframe(styled_df)

   
# day_gainers_options
st.subheader("Day Gainers Options")    
def fetch_day_gainers_options():
    screener = Screener()
    data = screener.get_screeners("day_gainers_options")
    quotes = data.get("day_gainers_options", {}).get("quotes", [])
    if not quotes:
        return pd.DataFrame()

    df = pd.DataFrame(quotes)
    # Filter for significant price gainers
   # df = df[df["regularMarketChangePercent"].fillna(0) > 5     
    return df.head(20) 

#display day gainers options
day_gainers_options = fetch_day_gainers_options()
if day_gainers_options.empty:
    st.write("No day gainers options found.")       
else:
    # Select relevant columns
    day_gainers_options = day_gainers_options[["underlyingSymbol", "underlyingShortName", "regularMarketPrice", "regularMarketChange", "regularMarketChangePercent", "regularMarketVolume"]]
    day_gainers_options.rename(columns={
        "underlyingSymbol": "Ticker",
        "underlyingShortName": "Name",
        "regularMarketPrice": "Price",
        "regularMarketChange": "Change",
        "regularMarketChangePercent": "% Change",
        "regularMarketVolume": "Volume"
    }, inplace=True)

    # Add conditional formatting
    styled_day_gainers_df = day_gainers_options.style.map(highlight_change, subset=["% Change"])
    st.dataframe(styled_day_gainers_df) 
            

# Day gainers stocks
st.subheader("Day Gainers Stocks under $20")    
def fetch_day_gainers_stocks():
    screener = Screener()
    data = screener.get_screeners("day_gainers")
    quotes = data.get("day_gainers", {}).get("quotes", [])
    if not quotes:
        return pd.DataFrame()

    df = pd.DataFrame(quotes)
    
    # Filter for stocks under $10
    df = df[df["regularMarketPrice"] < 20]
    
    return df   

# Display day gainers stocks
day_gainers_stocks = fetch_day_gainers_stocks() 
if day_gainers_stocks.empty:
    st.write("No day gainers stocks found under $20.")          
else:       
    # Select relevant columns
    day_gainers_stocks = day_gainers_stocks[["symbol", "shortName", "regularMarketPrice", "regularMarketChange", "regularMarketChangePercent", "regularMarketVolume"]]
    day_gainers_stocks.rename(columns={
        "symbol": "Ticker",
        "shortName": "Name",
        "regularMarketPrice": "Price",
        "regularMarketChange": "Change",
        "regularMarketChangePercent": "% Change",
        "regularMarketVolume": "Volume"
    }, inplace=True)

    # Add conditional formatting
    styled_day_gainers_df = day_gainers_stocks.style.map(highlight_change, subset=["% Change"])
    st.dataframe(styled_day_gainers_df)




# Maually refresh the data
if st.button("🔄 Refresh-Now"): 
    st.rerun()  
            
   
    
  #auto-refresh every 30 seconds
countdown = st.empty()
for i in range(30, 0, -1):
    countdown.markdown(f"⏳ Auto-refreshing in `{i}` seconds... or click 🔄 above")
    time.sleep(1)  
st.rerun()  

    
  # Optional: Add a button to refresh manually

 

