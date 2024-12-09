import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.optimize import minimize

# Télécharger les données des ETF
etfs = ['SPY', 'QQQ', 'TQQQ', 'AI.PA']
data = yf.download(etfs, start='2015-01-01', end='2024-01-01')['Adj Close']

# Afficher les premières lignes des données
print(data.head())

# Calculer les rendements quotidiens
returns = data.pct_change()

# Calculer les rendements annuels
annual_returns = returns.mean() * 252 * 100
print("Rendement annuel =\n", annual_returns)

# Calculer la matrice de corrélation
correlation_matrix = returns.corr()

# Afficher la matrice de corrélation avec une heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5, vmin=-1, vmax=1)

# Ajouter un titre
plt.title('Matrice de corrélation des rendements', fontsize=16)
plt.show()

# Trouver la plus grosse chute sur une journée
max_daily_drop = returns.min().min() * 100  # La plus grosse baisse en pourcentage
worst_day = returns.idxmin().min()  # La date de la plus grosse baisse

# Afficher les résultats
print(f"La plus grosse chute sur une journée est de {max_daily_drop:.2f}%")
print(f"Elle a eu lieu le {worst_day}")
