import numpy as np

class BruteForceRouter:
    def __init__(self, c, r):
        self.W = np.where(c == -1, np.inf, c * (1 - r))
        self.N, self.M = c.shape
        self.min_cost = np.inf
        self.best_path = []
        self.calls = 0
        
    def solve(self, i=0, j=0, current_cost=0, current_path=None):
        self.calls += 1
        if current_path is None:
            current_path = []
            
        current_path.append((i, j))
        current_cost += self.W[i][j]
        
        # Poda: se já estourou o limite conhecido ou bateu em obstáculo
        if current_cost >= self.min_cost or self.W[i][j] == np.inf:
            return
            
        # Chegou em qualquer fronteira de destino (última linha ou coluna)
        if i == self.N - 1 or j == self.M - 1:
            if current_cost < self.min_cost:
                self.min_cost = current_cost
                self.best_path = list(current_path)
            return
            
        # Movimentos permitidos: Direita e Baixo
        if i + 1 < self.N:
            self.solve(i + 1, j, current_cost, list(current_path))
        if j + 1 < self.M:
            self.solve(i, j + 1, current_cost, list(current_path))
            
    def get_results(self):
        self.solve()
        return self.min_cost, self.best_path, self.calls