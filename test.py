import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Télécharger les données du TQQQ
tqqq_data = yf.download('TQQQ', start='2001-01-01', end='2024-12-01')['Adj Close']

# Montants d'investissement
initial_investment = 6000
monthly_contribution = 500  # Montant fixe par mois

# Calculer les rendements mensuels
tqqq_returns = tqqq_data.pct_change().resample('M').last()

# Calculer le rendement annuel moyen (CAGR)
start_value = tqqq_data.iloc[0]
end_value = tqqq_data.iloc[-1]
years = (tqqq_data.index[-1].year - tqqq_data.index[0].year)
cagr = (end_value / start_value) ** (1 / years) - 1

# Réduire le rendement annuel de 5%
adjusted_cagr = cagr - 0.05
monthly_average_return = (1 + adjusted_cagr) ** (1 / 12) - 1

print(f"\nRendement annuel moyen initial (CAGR) : {cagr * 100:.2f}%")
print(f"Rendement annuel ajusté (-5%) : {adjusted_cagr * 100:.2f}%")
print(f"Rendement mensuel moyen équivalent utilisé : {monthly_average_return * 100:.2f}%\n")

# Initialiser les variables pour le suivi des valeurs d'investissement
portfolio_value = initial_investment
portfolio_values = [portfolio_value]
dates = tqqq_returns.index

# Simuler l'investissement pour les données historiques
for i in range(1, len(tqqq_returns)):
    portfolio_value *= (1 + tqqq_returns.iloc[i])  
    portfolio_value += monthly_contribution 
    portfolio_values.append(portfolio_value)


target_value = 1_500_000
future_portfolio_value = portfolio_values[-1]
future_dates = []
current_date = dates[-1] if not dates.empty else pd.Timestamp('2024-10-01')

while future_portfolio_value < target_value:
    future_portfolio_value *= (1 + monthly_average_return) 
    future_portfolio_value += monthly_contribution
    current_date += pd.DateOffset(months=1)
    future_dates.append(current_date)
    portfolio_values.append(future_portfolio_value)

# Créer une liste complète des dates
all_dates = list(dates) + future_dates

# Résultats
target_date = future_dates[-1]
print(f"Avec un investissement mensuel de {monthly_contribution} €, vous atteindrez {target_value} d'euros le {target_date.strftime('%Y-%m-%d')}.")

# Créer le DataFrame complet
investment_over_time = pd.DataFrame({'Date': all_dates, 'Portfolio Value': portfolio_values}).set_index('Date')

# Tracer les données
plt.figure(figsize=(10, 6))
plt.plot(investment_over_time.index, investment_over_time['Portfolio Value'], label='Projection jusqu\'à 1,5M€ (ajustée)')
plt.title('Évolution du portefeuille jusqu\'à atteindre 1,5M€ (ajustement de -5%)')
plt.xlabel('Date')
plt.ylabel('Valeur du portefeuille (en euros)')
plt.axhline(target_value, color='r', linestyle='--', label='1,5M€')
plt.grid(True)
plt.legend()
plt.show()
