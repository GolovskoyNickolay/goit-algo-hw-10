import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad


# Визначення функції
def f(x):
    return x ** 2


# Межі інтегрування
a = 0  # Нижня межа
b = 2  # Верхня межа


# Метод Монте-Карло для обчислення інтегралу
def monte_carlo_integration(f, a, b, num_samples=10000):
    x_random = np.random.uniform(a, b, num_samples)  # Випадкові точки на відрізку [a, b]
    y_random = f(x_random)  # Обчислення значення функції для випадкових точок
    integral_value = (b - a) * np.mean(y_random)  # Інтеграл як середнє значення функції
    return integral_value


# Обчислення інтегралу методом Монте-Карло
monte_carlo_result = monte_carlo_integration(f, a, b)

# Аналітичне обчислення інтегралу за допомогою scipy
analytical_result, _ = quad(f, a, b)

# Порівняння результатів
print(monte_carlo_result, analytical_result)
