import yfinance as yf
import os
import pandas as pd

def download_and_cache(tickers: list[str], data_path):
    d = {}
    for t in tickers:
        path = os.path.join(data_path, t + '.csv')
        if os.path.exists(path):
            d[t] = pd.read_csv(path, index_col=0, parse_dates=True)
            if d[t].shape[0] == 0:
                d[t] = yf.download(t, auto_adjust=True).dropna()
        else:
            d[t] = yf.download(t, auto_adjust=True).dropna()
            if not d[t].empty:
                d[t].to_csv(path)
    return d

def read_tickers_from_file(filepath):
    tickers = []
    with open(filepath, 'r') as f:
        for t in f.readlines():
            t = t.strip()
            if t.isdecimal():
                tickers.append(t + '.BO')
            else:
                tickers.append(t + '.NS')
    return tickers