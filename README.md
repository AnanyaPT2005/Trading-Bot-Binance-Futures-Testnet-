# Binance Futures Testnet Trading Bot (Python)

A simplified Python trading bot that places MARKET and LIMIT orders on Binance Futures Testnet (USDT-M).  
Built with structured architecture, proper logging, validation, and error handling.

---

## 🚀 Features

- Place MARKET orders
- Place LIMIT orders
- Supports BUY and SELL
- Interactive CLI menu
- Input validation
- Structured layered architecture
- Logging of API requests, responses, and errors
- Exception handling for API & validation errors
- Uses Binance Futures Testnet (safe sandbox)

## Requirements

Python 3.10+

requests

python-dotenv

python-binance

---

##  Setup Instructions
1. Clone Repo
2. Create virtual Environment and activate
    python -m venv venv
    venv\Scripts\activate  
3. Install Dependencies: pip install -r requirements.txt
4. Create Binance Futures Testnet Account:

Go to: https://testnet.binancefuture.com

Register a testnet account

Go to API Management

Create API key

Enable:

Futures

Trading

Copy API Key and Secret Key

5. Create .env File. Add api and Secret key:
    BINANCE_API_KEY=your_api_key_here
    BINANCE_SECRET_KEY=your_secret_key_here
6. Run: python cli.py

## Menu & Examples:

1. Place MARKET order
2. Place LIMIT order
3. Exit

### Market Order:
Symbol: BTCUSDT
Side: BUY
Quantity: 0.002

### Limit Order:
Symbol: BTCUSDT
Side: SELL
Quantity: 0.002
Price: 100000

Logs include:

Order request details

API responses

Validation errors

API exceptions

Logs are stored in logs/trading_bot.log

## Assumptions

Minimum notional value (100 USDT) is enforced by Binance Futures.

MARKET orders on testnet may return status NEW due to testnet behavior.

Only USDT-M Futures Testnet is supported.

Uses python-binance library for API interaction.