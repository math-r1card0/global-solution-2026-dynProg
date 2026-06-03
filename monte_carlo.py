import numpy as np
from scipy.stats import beta
from dynamic_programming import dp_bottom_up

def run_monte_carlo(c, r, p, K=10000):
    # Calibração da distribuição Beta baseada no histórico P
    # Assumindo peso 10 para variância moderada
    alpha_params = np.clip(p * 10, 0.1, None)
    beta_params = np.clip((1 - p) * 10, 0.1, None)
    
    costs = []
    
    for _ in range(K):
        # Amostrando novo cenário de probabilidade p'
        p_prime = np.random.beta(alpha_params, beta_params)
        _, min_cost = dp_bottom_up(c, r, p_prime)
        costs.append(min_cost)
        
    costs = np.array(costs)
    
    # Métricas
    metrics = {
        'mean': np.mean(costs),
        'median': np.median(costs),
        'std': np.std(costs),
        'ci_lower': np.percentile(costs, 2.5),
        'ci_upper': np.percentile(costs, 97.5)
    }
    
    return costs, metrics