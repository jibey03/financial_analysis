import yfinance as yf
import matplotlib.pyplot as plt

# Définir l'ETF à tracer
etf_symbol = 'QQQ'  # Remplace par le symbole de l'ETF que tu souhaites tracer

# Télécharger les données de l'ETF
data = yf.download(etf_symbol, start='2001-01-01', end='2024-12-01')['Adj Close']

print (data)

# # Tracer la courbe de l'ETF
# plt.figure(figsize=(10, 6))
# plt.plot(data.index, data, label=etf_symbol, color='blue')
# plt.title(f"Cours de l'ETF {etf_symbol}", fontsize=16)
# plt.xlabel("Date", fontsize=12)
# plt.ylabel("Prix ajusté", fontsize=12)
# plt.grid(True)
# plt.legend()
# plt.show()


# # Calculer les rendements quotidiens
# returns = data.pct_change()

# # Calculer les rendements annuels
# annual_returns = returns.mean() * 252 * 100
# print("Rendement annuel =\n", annual_returns)