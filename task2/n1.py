from taskСondition import a, b, c, n
from sympy import symbols, solve, pprint, Eq

q = symbols('q')

equation = q**3 - a * q**2 - b * q - c #Решение характеристического уравнения
roots = solve(equation, q)

roots.sort()
i = 0
generalHomogeneousSolution = 0 #(an)общее однородное

while i < len(roots):
    r = roots[i]
    multiplicity = roots.count(r)

    if multiplicity == 1: #k = 1
        c = symbols(f'C{i + 1}')
        generalHomogeneousSolution += (c * r**n)
    else: #k = 2
        for j in range(multiplicity): #Последовательно прибавляем C по другой формуле
            c = symbols(f'C{i + j + 1}')
            generalHomogeneousSolution += (c * n**j * r**n)

    i += multiplicity


print("Характеристическое уравнение:")
pprint(Eq(equation, 0))
print()
print("Корни характеристического уравнения:", end=' ')
pprint(roots)
print()
print("Общее решение ЛОРС:")

pprint(generalHomogeneousSolution)