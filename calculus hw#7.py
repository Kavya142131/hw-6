import math
import random

# Define limits
a = 0
b = (7 * math.pi) / 6

# Define the line function
def line(x):
    return (-3 / (7 * math.pi)) * x

# Define the function f(x) = sin(x)
def f(x):
    return math.sin(x)

# === Definite Integral using Riemann Sum ===
def integrate_riemann(n=100000):
    dx = (b - a) / n
    total_area = 0
    for i in range(n):
        x = a + i * dx
        height = f(x) - line(x)
        total_area += height * dx
    return total_area

# === Monte Carlo Simulation ===
def monte_carlo(n=100000):
    ymin = 0
    ymax = 1.1  # max(sin(x)) is 1, and line is negative, so 1.1 is safe

    count_inside = 0
    for _ in range(n):
        x = random.uniform(a, b)
        y = random.uniform(line(x), f(x))  # always y between line and sin(x)
        if y >= line(x) and y <= f(x):
            count_inside += 1

    rect_area = (b - a) * (ymax - ymin)
    return rect_area * (count_inside / n)

# === Run both methods ===
print("Area using Riemann Sum:", round(integrate_riemann(), 4))
print("Area using Monte Carlo:", round(monte_carlo(), 4))

