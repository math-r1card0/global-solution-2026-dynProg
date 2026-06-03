import time
import tracemalloc
import numpy as np
from brute_force import BruteForceRouter
from dynamic_programming import dp_bottom_up

def generate_mock_grid(N, M):
    """Gera matrizes sintéticas de custo e risco para os testes."""
    c = np.random.uniform(1, 10, size=(N, M))
    r = np.random.uniform(0, 1, size=(N, M))
    # Adicionando um pequeno grau de bloqueios aleatórios
    if N > 3:
        c[1][1] = -1 
    return c, r

def measure_performance(algorithm_func, *args, is_class=False):
    """Mede tempo (ms) e memória (MB) de um algoritmo."""
    tracemalloc.start()
    start_time = time.perf_counter()
    
    if is_class:
        instance = algorithm_func(*args)
        min_cost, path, calls = instance.get_results()
        iterations = calls
    else:
        # Assumindo que a DP roda iterativamente em N*M passos
        dp_matrix, min_cost = algorithm_func(*args)
        iterations = args[0].size 
        
    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    exec_time_ms = (end_time - start_time) * 1000
    peak_memory_mb = peak / (1024 * 1024)
    
    return exec_time_ms, peak_memory_mb, iterations

def run_scalability_tests():
    """Roda os testes de escalabilidade empírica exigidos."""
    # Tamanhos exigidos pela FIAP: N=M=3, 5, 10, 20, 50, 100
    sizes = [3, 5, 10, 20, 50, 100] 
    
    print(f"{'N=M':<5} | {'Algo':<15} | {'Tempo (ms)':<12} | {'Memória (MB)':<12} | {'Iterações'}")
    print("-" * 65)
    
    for size in sizes:
        c, r = generate_mock_grid(size, size)
        
        # 1. Programação Dinâmica
        t_dp, m_dp, i_dp = measure_performance(dp_bottom_up, c, r)
        print(f"{size:<5} | {'DP Bottom-up':<15} | {t_dp:<12.4f} | {m_dp:<12.6f} | {i_dp}")
        
        # 2. Força Bruta (Executar apenas para N <= 5 para evitar travamento)
        if size <= 5:
            t_fb, m_fb, i_fb = measure_performance(BruteForceRouter, c, r, is_class=True)
            print(f"{size:<5} | {'Força Bruta':<15} | {t_fb:<12.4f} | {m_fb:<12.6f} | {i_fb}")
        else:
             print(f"{size:<5} | {'Força Bruta':<15} | {'---':<12} | {'---':<12} | {'ESTOUROU'}")
        
        print("-" * 65)

if __name__ == "__main__":
    run_scalability_tests()