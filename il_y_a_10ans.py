import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Télécharger les données du TQQQ
tqqq_data = yf.download('TQQQ', start='2021-01-01', end='2024-12-01')['Adj Close']



# Montants d'investissement
initial_investment = 6000  # Investissement initial
monthly_contribution = 600  # Montant fixe par mois

# Calculer les rendements mensuels
tqqq_returns = tqqq_data.pct_change().resample('M').last()

# Initialiser les variables pour le suivi des valeurs d'investissement
portfolio_value = initial_investment
portfolio_values = [portfolio_value]
dates = tqqq_returns.index

# Simuler l'investissement pour les données historiques
for i in range(1, len(tqqq_returns)):
    portfolio_value *= (1 + tqqq_returns.iloc[i])  # Croissance selon le rendement réel
    portfolio_value += monthly_contribution  # Ajouter la contribution mensuelle
    portfolio_values.append(portfolio_value)

# Résultats
final_portfolio_value = portfolio_values[-1]
print(f"Valeur du portefeuille aujourd'hui (Décembre 2024) : {final_portfolio_value:.2f} €")

# Créer un DataFrame pour les visualisations
investment_over_time = pd.DataFrame({'Date': dates, 'Portfolio Value': portfolio_values}).set_index('Date')

# Tracer l'évolution du portefeuille
plt.figure(figsize=(10, 6))
plt.plot(investment_over_time.index, investment_over_time['Portfolio Value'], label='Évolution du portefeuille')
plt.title('Simulation d\'un investissement dans le TQQQ (2014 - 2024)')
plt.xlabel('Date')
plt.ylabel('Valeur du portefeuille (en euros)')
plt.grid(True)
plt.legend()
plt.show()
