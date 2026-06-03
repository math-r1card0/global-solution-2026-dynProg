import numpy as np

def calculate_effective_cost(c, r, p=None):
    """Calcula o custo efetivo. Células bloqueadas (c=-1) retornam infinito."""
    if p is None:
        p = np.ones_like(c)
    
    # Penaliza o custo, mas dá 'desconto' se o risco for alto
    W = np.where(c == -1, np.inf, c * p * (1 - r))
    return W

def dp_bottom_up(c, r, p=None):
    N, M = c.shape
    W = calculate_effective_cost(c, r, p)
    dp = np.full((N, M), np.inf)
    
    # Caso base
    dp[0][0] = W[0][0]
    
    # Preenchimento da 1ª coluna e 1ª linha
    for i in range(1, N):
        dp[i][0] = dp[i-1][0] + W[i][0]
    for j in range(1, M):
        dp[0][j] = dp[0][j-1] + W[0][j]
        
    # Preenchimento do restante da matriz
    for i in range(1, N):
        for j in range(1, M):
            if W[i][j] != np.inf:
                dp[i][j] = W[i][j] + min(dp[i-1][j], dp[i][j-1])
                
    # O destino pode ser qualquer célula da última linha ou última coluna
    min_last_row = np.min(dp[N-1, :])
    min_last_col = np.min(dp[:, M-1])
    min_cost = min(min_last_row, min_last_col)
    
    return dp, min_cost

def reconstruct_path(dp):
    N, M = dp.shape
    
    # Encontra o ponto de saída ótimo (última linha ou coluna)
    last_row_min_idx = np.argmin(dp[N-1, :])
    last_col_min_idx = np.argmin(dp[:, M-1])
    
    if dp[N-1, last_row_min_idx] < dp[last_col_min_idx, M-1]:
        curr_i, curr_j = N-1, last_row_min_idx
    else:
        curr_i, curr_j = last_col_min_idx, M-1
        
    path = [(curr_i, curr_j)]
    
    # Backtracking
    while curr_i > 0 or curr_j > 0:
        if curr_i == 0:
            curr_j -= 1
        elif curr_j == 0:
            curr_i -= 1
        else:
            if dp[curr_i-1][curr_j] < dp[curr_i][curr_j-1]:
                curr_i -= 1
            else:
                curr_j -= 1
        path.append((curr_i, curr_j))
        
    return path[::-1] # Retorna do início ao fim