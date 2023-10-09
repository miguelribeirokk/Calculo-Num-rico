import numpy as np
from scipy.optimize import minimize

# Defina a função objetivo
def objective_function(x):
    return x[0]**2 + x[1]**2

# Chute inicial
x0 = [1.0, 1.0]

# Minimize a função usando o método Quasi-Newton (BFGS)
result = minimize(objective_function, x0, method='BFGS')
print("Mínimo usando o método Quasi-Newton (BFGS):", result.x)
