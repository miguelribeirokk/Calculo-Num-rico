import numpy as np
from scipy.optimize import minimize

# Defina a função objetivo
def objective_function(x):
    return x[0]**2 + (x[1] - 2)**2

# Defina o Jacobiano da função objetivo
def objective_jacobian(x):
    return np.array([2 * x[0], 2 * (x[1] - 2)])

# Chute inicial
x0 = [1.0, 1.0]

# Minimize a função usando o método de Newton-CG
result = minimize(objective_function, x0, method='Newton-CG', jac=objective_jacobian)
print("Resultado da otimização:")
print("x =", result.x)
print("Valor mínimo da função =", result.fun)
