import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Télécharger les données du TQQQ des 20 dernières années
end_date = pd.Timestamp.today()
start_date = end_date - pd.DateOffset(years=15)
tqqq_data = yf.download('TQQQ', start=start_date, end=end_date)['Adj Close']

# Montants d'investissement
initial_investment = 8000
monthly_contribution = 600  # Montant fixe par mois

# Calculer les rendements mensuels
tqqq_returns = tqqq_data.pct_change().resample('M').ffill()

# Calculer le rendement annuel moyen (CAGR)
start_value = tqqq_data.iloc[0]
end_value = tqqq_data.iloc[-1]
years = (end_date.year - start_date.year)
cagr = (end_value / start_value) ** (1 / years) - 1

# Réduire le rendement annuel de 5% pour une marge de sécurité
adjusted_cagr = cagr - 0.05
monthly_average_return = (1 + adjusted_cagr) ** (1 / 12) - 1

print(f"\nRendement annuel moyen initial (CAGR) : {cagr * 100:.2f}%")
print(f"Rendement annuel ajusté (-5%) : {adjusted_cagr * 100:.2f}%")
print(f"Rendement mensuel moyen ajusté : {monthly_average_return * 100:.2f}%\n")

# Initialiser les variables pour le suivi des valeurs d'investissement
portfolio_value = initial_investment
portfolio_values = [portfolio_value]
dates = [pd.Timestamp('2024-12-09')]

# Utiliser la formule des intérêts composés pour les projections futures
while portfolio_value < 1_000_000:
    portfolio_value = portfolio_value * (1 + monthly_average_return) + monthly_contribution
    dates.append(dates[-1] + pd.DateOffset(months=1))
    portfolio_values.append(portfolio_value)

# Résultats
target_date = dates[-1]
print(f"Avec un investissement mensuel de {monthly_contribution} €, vous atteindrez 1 000 000 d'euros le {target_date.strftime('%Y-%m-%d')}.")

# Créer le DataFrame complet
investment_over_time = pd.DataFrame({'Date': dates, 'Portfolio Value': portfolio_values}).set_index('Date')

# Tracer les données
plt.figure(figsize=(10, 6))
plt.plot(investment_over_time.index, investment_over_time['Portfolio Value'], label='Évolution du portefeuille (projeté)')
plt.title('Évolution du portefeuille avec un investissement initial de 8000 € et une contribution mensuelle de 600 €')
plt.xlabel('Date')
plt.ylabel('Valeur du portefeuille (en euros)')
plt.axhline(1_000_000, color='r', linestyle='--', label='Objectif : 1M€')
plt.grid(True)
plt.legend()
plt.show()
