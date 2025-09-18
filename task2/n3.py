from sympy import Eq, solve, pprint
from taskСondition import n, f0, f1, f2
from n1 import generalHomogeneousSolution
from n2 import privateHeterogeneousSolution

expression = generalHomogeneousSolution + privateHeterogeneousSolution #Общее неоднородное = общее однородное + частное неоднородное
equation0 = Eq(f0, expression.subs(n, 0)) #Составляем уравнения по н.у
equation1 = Eq(f1, expression.subs(n, 1))
equation2 = Eq(f2, expression.subs(n, 2))
coefficients = list(generalHomogeneousSolution.free_symbols - {n}) #Достаем коэффициенты C1, C2, C3
solution = solve((equation0, equation1, equation2), coefficients, dict=True) #Решаем систему уравнений
if solution:
    coefficients_solution = solution[0]
    generalHeterogeneousSolution = expression.subs(coefficients_solution) #Подставляем найденные коэффициенты и находим общее неоднородное
pprint(generalHeterogeneousSolution)
