import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns


etfs = ['SPY', 'QQQ', 'TQQQ','AI.PA']


data = yf.download(etfs, start='2015-01-01', end='2024-01-01')['Adj Close']


print(data.head())


# Calculer les rendements quotidiens
returns = data.pct_change()






annual_returns = returns.mean() * 252 * 100
print("rendement annuel = " , annual_returns)


# Calculer la matrice de corrélation
correlation_matrix = returns.corr()

# Afficher la matrice de corrélation avec une heatmap
plt.figure(figsize=(8, 6))  # Ajuste la taille du graphique
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5, vmin=-1, vmax=1)

# Ajouter un titre
plt.title('Matrice de corrélation des rendements', fontsize=16)

# Afficher le graphique
plt.show()