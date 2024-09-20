import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib as plt


etfs = ['SPY', 'QQQ', 'TQQQ']


data = yf.download(etfs, start='2000-01-01', end='2023-01-01')['Adj Close']


print(data.head())


# Calculer les rendements quotidiens
returns = data.pct_change()

# Calculer les rendements cumulés
cumulative_returns = (1 + returns).cumprod() - 1

# Afficher les rendements cumulés
print(cumulative_returns.tail())



annual_returns = returns.mean() * 252
print("rendement annuel = " , annual_returns)
