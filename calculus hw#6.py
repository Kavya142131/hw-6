import math

# Trapezoidal rule function
def trapezoidal(f, a, b, n=1000):
    h = (b - a) / n
    total = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        total += f(a + i * h)
    return total * h

# Q1.a: ∫₄⁹ 3√x dx
def f_a(x):
    return 3 * math.sqrt(x)
result_a = trapezoidal(f_a, 4, 9)
print("Q1.a:", result_a)

# Q1.b: ∫₁⁶ ln(x) dx
def f_b(x):
    return math.log(x)
result_b = trapezoidal(f_b, 1, 6)
print("Q1.b:", result_b)

# Q1.c: ∫₀¹ arccos(x) dx
def f_c(x):
    return math.acos(x)
result_c = trapezoidal(f_c, 0, 1)
print("Q1.c:", result_c)

# Q1.d: ∫₋¹¹ π * cos(πx/2) dx
def f_d(x):
    return math.pi * math.cos(math.pi * x / 2)
result_d = trapezoidal(f_d, -1, 1)
print("Q1.d:", result_d)

