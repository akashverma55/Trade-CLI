# Binance Testnet Trading CLI

A simple command-line code that places BUY/SELL orders on the Binance Testnet.

---

## What's Inside

```
trading_bot/
├── .env                  ← Your API keys (never share this)
├── requirements.txt      ← Libraries to install
├── cli.py                ← The file you run
├── test_connection.py    ← Tests if your keys work
├── bot/
│   ├── client.py         ← Connects to Binance using your keys
│   ├── orders.py         ← Places MARKET and LIMIT orders
│   ├── validators.py     ← Checks your input before sending to Binance
│   └── logging_config.py ← Saves logs to terminal + bot.log file
```

---

## Setup (Do this once)

### 1. Install the libraries
```bash
pip install -r requirements.txt
```

### 2. Get your Testnet API Keys
1. Go to https://testnet.binance.vision/
2. Click "Log In with GitHub"
3. Click "Generate HMAC_SHA256 Key"
4. Copy both keys immediately — the Secret Key is only shown once

### 3. Create your .env file
Create a file called `.env` in the project folder and paste your keys like this:
```
API_KEY=your_api_key_here
SECRET_KEY=your_secret_key_here
```

## How to Place Orders

### Market Order — executes instantly at the current price
```bash
# Buy BTC
python cli.py --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.01

# Sell BTC
python cli.py --symbol BTCUSDT --side SELL --order-type MARKET --quantity 0.01
```

### Limit Order — executes only when the price reaches your target
```bash
# Buy BTC when price drops to 80000
python cli.py --symbol BTCUSDT --side BUY --order-type LIMIT --quantity 0.01 --price 80000

# Sell BTC when price rises to 95000
python cli.py --symbol BTCUSDT --side SELL --order-type LIMIT --quantity 0.01 --price 95000
```

### Other trading pairs
```bash
# Ethereum market buy
python cli.py --symbol ETHUSDT --side BUY --order-type MARKET --quantity 0.1

# BNB market buy
python cli.py --symbol BNBUSDT --side BUY --order-type MARKET --quantity 1
```

### See all options
```bash
python cli.py --help
```

---

## What a Successful Order Looks Like

```
2026-04-22 16:25:55 | INFO    | New order request - BUY 0.01 BTCUSDT at MARKET price
2026-04-22 16:25:55 | INFO    | Connected to Binance Testnet successfully
2026-04-22 16:25:56 | SUCCESS | Order placed! ID=123456 | Status=FILLED | Avg Price=84500.0

Order Successful!
   Order ID  : 123456
   Status    : FILLED
   Avg Price : 84500.0
```

---

## Options Reference

| Option          | Required         | Example         | What it does                        |
|-----------------|------------------|-----------------|-------------------------------------|
| `--symbol`      | Yes              | `BTCUSDT`       | The trading pair                    |
| `--side`        | Yes              | `BUY` or `SELL` | Whether you're buying or selling    |
| `--order-type`  | Yes              | `MARKET`        | MARKET = instant, LIMIT = at price  |
| `--quantity`    | Yes              | `0.01`          | How much to buy or sell             |
| `--price`       | Only for LIMIT   | `80000`         | The target price for a LIMIT order  |

---

## Logs

Every order attempt is saved to `bot.log` in the project folder.
The terminal also shows live colored output as commands run.
The log file rotates automatically when it reaches 5MB.

---
