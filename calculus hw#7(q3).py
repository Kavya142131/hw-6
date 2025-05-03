import math

# Define the function to integrate
def integrand(x):
    if x == 0:
        return 0  # Avoid math domain error
    ln_x = math.log(x)
    return (1 + ln_x) * math.sqrt(1 + (x * ln_x) ** 2)

# Riemann sum approximation (midpoint rule)
def definite_integral(a, b, n=100000):
    dx = (b - a) / n
    total = 0
    for i in range(n):
        x = a + (i + 0.5) * dx  # Midpoint
        total += integrand(x) * dx
    return total

# Integration bounds
a = 0.2
b = 1

# Run the calculation
result = definite_integral(a, b)
print("Definite integral result:", round(result, 5))
