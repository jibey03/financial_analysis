import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.optimize import minimize

# Télécharger les données des ETF et de l'action Air Liquide
etfs = ['SPY', 'QQQ', 'TQQQ']
data = yf.download(etfs, start='2015-01-01', end='2020-01-01')['Adj Close']


# Fonction pour calculer le rendement attendu du portefeuille
def portfolio_return(weights, returns):
    return np.sum(returns.mean() * weights) * 252

# Fonction pour calculer la volatilité du portefeuille
def portfolio_volatility(weights, returns):
    return np.sqrt(np.dot(weights.T, np.dot(returns.cov() * 252, weights)))

# Fonction pour l'optimisation avec une contrainte de poids (sommes des poids = 1)
def optimize_portfolio(returns):
    num_assets = len(returns.columns)
    
    # Fonction objectif à minimiser (ici, la volatilité)
    def objective(weights):
        return portfolio_volatility(weights, returns)
    
    # Contraintes : la somme des poids doit être égale à 1
    constraints = {'type': 'eq', 'fun': lambda weights: np.sum(weights) - 1}
    
    # Borne sur les poids (les poids doivent être entre 0 et 1)
    bounds = tuple((0, 1) for asset in range(num_assets))
    
    # Poids initiaux (on commence avec un portefeuille égalitaire)
    initial_weights = num_assets * [1. / num_assets]
    
    # Minimisation de la volatilité sous contrainte de poids
    optimal_solution = minimize(objective, initial_weights, bounds=bounds, constraints=constraints)
    
    return optimal_solution.x

# Calcul des rendements quotidiens
returns = data.pct_change()

# Trouver les poids optimaux pour minimiser le risque (volatilité)
optimal_weights = optimize_portfolio(returns)

# Afficher les poids optimaux
optimal_weights_percentage = optimal_weights * 100
for i, etf in enumerate(etfs):
    print(f"Allocation optimale pour {etf}: {optimal_weights_percentage[i]:.2f}%")
