from sympy import symbols, Pow, preorder_traversal, Eq, solve, pprint
from n1 import roots
from taskСondition import d, n, a, b, c

def makePrivateHeterogeneousExpression(expression, variable, roots):
    t = None
    polynom = expression

    for curExp in preorder_traversal(expression): #Проходимся по всему выражению, если находим показательную функцию, то запомением ее основание и оставляем только полином
        if (isinstance(curExp, Pow) and curExp.base.is_constant() and curExp.exp == variable):
            t = curExp.base
            polynom = expression / curExp
            break

    m = (polynom.as_poly(variable).degree() if polynom.is_polynomial(variable) else 0) #Либо степень полинома, либо 0
    t = (1 if t is None else t) #Либо найденное основание показательной функции, либо 1
    s = sum(1 for root in roots if root == t) #Кол-во корней, совпадающих с t

    coefficients = symbols([f'{chr(i + 65)}' for i in range(m + 1)]) #Формируем список символов для полинома
    Qm_n= sum(coefficients[i] * variable ** i for i in range(m + 1)) #Формируем полином с символами

    return Qm_n * t ** variable * variable ** s #Qm(n) * t^n * n^s


def solvePrivateHeterogeneousExpression(expression, variable):
    n = variable
    f_n0 = expression.subs(n, n)  #Последовательно подставляем n, n+1, n+2, n+3
    f_n1 = expression.subs(n, n + 1)
    f_n2 = expression.subs(n, n + 2)
    f_n3 = expression.subs(n, n + 3)
    equation = Eq(f_n3, a * f_n2 + b * f_n1 + c * f_n0 + d) #Записываем уравнение
    coefficients = list(expression.free_symbols - {n}) #Вычисляем список коэффициентов, которые нужно найти, кроме n
    solution = solve(equation, coefficients, dict=True)

    if solution:
        coefficients_solution = solution[0]
        privateHeterogeneousSolution = expression.subs(coefficients_solution)
        return privateHeterogeneousSolution
    return None


privateHeterogeneousExpression = makePrivateHeterogeneousExpression(d, n, roots)
privateHeterogeneousSolution = solvePrivateHeterogeneousExpression(privateHeterogeneousExpression, n)
print("Частное решение ЛНРС:")
pprint(privateHeterogeneousSolution)
