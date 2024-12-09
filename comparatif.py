import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Liste des 10 ETF
etfs = ['QQQ', 'SPY', 'TQQQ', 'ARKK', 'SOXX', 'VGT', 'XBI', 'FTEC', 'FDN', 'CLOU',
        'TECL', 'SOXL', 'UPRO', 'FNGU', 'LABU', 'TMF', 'SQQQ', 'TNA', 'QLD', 'SSO',
        'DIA', 'XLK', 'IWM', 'VT', 'XLF', 'XLV', 'XLE', 'ARKW', 'TQQQ', 'SH']

# Télécharger les données de ces ETF
data = yf.download(etfs, start='2015-01-01', end='2020-01-01')['Adj Close']

# Calculer les rendements quotidiens
returns = data.pct_change()

# Calculer les rendements annuels
annual_returns = returns.mean() * 252 * 100

# Calculer la volatilité annuelle
annual_volatility = returns.std() * np.sqrt(252) * 100

# Calculer le ratio rendement/volatilité avec un poids de 2 sur les rendements
adjusted_ratio = (annual_returns) / annual_volatility

# Afficher les rendements annuels, volatilités annuelles et le ratio ajusté
ratios_df = pd.DataFrame({
    'Rendement Annuel (%)': annual_returns,
    'Volatilité Annuelle (%)': annual_volatility,
    'Ratio Ajusté (Rendement / Volatilité)': adjusted_ratio
})

print("Rendements annuels, Volatilités et Ratio ajusté :\n")
print(ratios_df)

# Trier les ETF par le ratio ajusté (rendement pondéré par 2)
sorted_ratios_df = ratios_df.sort_values(by='Ratio Ajusté (Rendement / Volatilité)', ascending=False)
print("\nETF classés par le ratio ajusté :\n", sorted_ratios_df)

# Visualiser les ETF ayant les meilleurs ratios ajustés (Top 5)
top_etfs = sorted_ratios_df.index[:5]
top_cumulative_returns = (1 + returns[top_etfs]).cumprod() - 1

# Tracer les rendements cumulés des 5 ETF ayant les meilleurs ratios ajustés
plt.figure(figsize=(10, 6))
for etf in top_etfs:
    plt.plot(top_cumulative_returns.index, top_cumulative_returns[etf], label=etf)

# Ajouter un titre et des légendes
plt.title("Performances des ETF avec les meilleurs ratios ajustés", fontsize=16)
plt.xlabel("Date")
plt.ylabel("Rendements cumulés")
plt.grid(True)
plt.legend(loc="upper left")

# Afficher le graphique
plt.show()
