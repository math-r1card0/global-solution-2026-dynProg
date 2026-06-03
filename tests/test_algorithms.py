import numpy as np
import pytest
from src.brute_force import BruteForceRouter
from src.dynamic_programming import dp_bottom_up

def test_dp_matches_brute_force():
    """Testa se a Programação Dinâmica acha o mesmo custo ótimo que a Força Bruta em grades pequenas."""
    # Grade 4x4 sem obstáculos
    c = np.array([
        [1, 2, 3, 1],
        [4, 5, 6, 1],
        [7, 8, 9, 1],
        [1, 1, 1, 1]
    ], dtype=float)
    
    r = np.zeros((4, 4)) # Risco 0 para simplificar o cálculo efetivo
    
    # Executa FB
    fb = BruteForceRouter(c, r)
    min_cost_fb, _, _ = fb.get_results()
    
    # Executa DP
    _, min_cost_dp = dp_bottom_up(c, r)
    
    # O assert do Pytest garante que as respostas batem
    assert np.isclose(min_cost_fb, min_cost_dp), f"Erro: FB={min_cost_fb}, mas DP={min_cost_dp}"

def test_dp_with_blocked_cells():
    """Testa se o algoritmo respeita células bloqueadas (custo = -1)."""
    c = np.array([
        [1, -1, 1],
        [1, -1, 1],
        [1,  1, 1]
    ], dtype=float)
    
    r = np.zeros((3, 3))
    
    # A rota é forçada a dar a volta por baixo
    _, min_cost_dp = dp_bottom_up(c, r)
    
    # O caminho deve ser (0,0)->(1,0)->(2,0)->(2,1)->(2,2) = 1+1+1+1+1 = 5
    assert min_cost_dp == 5.0