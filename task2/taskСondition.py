from sympy import symbols, solve, Eq, Function

a = 3
b = 13
c = -15

f0 = 1
f1 = 2
f2 = 3
n = symbols('n')

q = symbols('q')
equation = Eq(q**3, a * q**2 + b * q + c)
roots = solve(equation)
print("Характеристическое уравнение:", equation)
print("Корни характеристического уравнения:", roots)


