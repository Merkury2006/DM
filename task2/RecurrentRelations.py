from sympy import symbols, solve, pprint, Eq, Pow, preorder_traversal


class RecurrentRelation:
    def __init__(self, a, b, c, f0, f1, f2, d_expr, d_func):
        self.a = a
        self.b = b
        self.c = c
        self.f0 = f0
        self.f1 = f1
        self.f2 = f2
        self.n = symbols("n")
        self.d_expr = d_expr
        self.d_func = d_func

        self.q = symbols("q")
        self.roots = None
        self.characteristic_equation = None
        self.homogeneous_solution = None
        self.particular_solution = None
        self.general_solution = None

    """Все решение"""
    def solve_completely(self):
        self.make_characteristic_equation()
        self.find_roots()
        self.find_homogeneous_solution()
        self.find_particular_solution()
        self.find_general_solution()
        self.print_solution()




    """Часть 1"""
    def make_characteristic_equation(self):
        if self.characteristic_equation is not None:
            return self.characteristic_equation

        equation = self.q ** 3 - self.a * self.q ** 2 - self.b * self.q - self.c  # Решение характеристического уравнения
        self.characteristic_equation = equation
        return self.characteristic_equation

    def find_roots(self): #Находит корни характеристического уравнения
        if self.roots is not None:
            return self.roots

        equation = self.make_characteristic_equation()
        roots = solve(equation, self.q)
        roots.sort()

        self.roots = roots
        return self.roots

    def find_homogeneous_solution(self): #Находит общее решение однородного уравнения
        if self.homogeneous_solution is not None:
            return self.homogeneous_solution

        roots = self.find_roots()
        i = 0
        homogeneous_solution = 0  # (an)общее однородное

        while i < len(roots):
            r = roots[i]
            multiplicity = roots.count(r)

            if multiplicity == 1:  # k = 1
                c = symbols(f'C{i + 1}')
                homogeneous_solution += (c * r ** self.n)
            else:  # k = 2
                for j in range(multiplicity):  # Последовательно прибавляем C по другой формуле
                    c = symbols(f'C{i + j + 1}')
                    homogeneous_solution += (c * self.n ** j * r ** self.n)

            i += multiplicity

        self.homogeneous_solution = homogeneous_solution
        return self.homogeneous_solution



    """Часть 2"""
    def find_particular_solution(self): #Находит частное решение неоднородного уравнения
        if self.particular_solution is not None:
            return self.particular_solution

        roots = self.find_roots()
        t = None
        polynom = self.d_expr

        for curExp in preorder_traversal(self.d_expr):  # Проходимся по всему выражению, если находим показательную функцию, то запомением ее основание и оставляем только полином
            if isinstance(curExp, Pow) and curExp.base.is_constant() and curExp.exp == self.n:
                t = curExp.base
                polynom = self.d_expr / curExp
                break

        m = polynom.as_poly(self.n).degree() if polynom.is_polynomial(self.n) else 0 # Либо степень полинома, либо 0
        t = 1 if t is None else t  # Либо найденное основание показательной функции, либо 1
        s = sum(1 for root in roots if root == t)  # Кол-во корней, совпадающих с t

        coefficients = symbols([f'{chr(i + 65)}' for i in range(m + 1)])  # Формируем список символов для полинома
        Qm_n = sum(coefficients[i] * self.n ** i for i in range(m + 1))  # Формируем полином с символами

        self.particular_solution = self.solve_particular_coefficients(Qm_n * t ** self.n * self.n ** s) # Qm(n) * t^n * n^s
        return self.particular_solution

    def solve_particular_coefficients(self, expression):
        f_n0 = expression.subs(n, self.n)  # Последовательно подставляем n, n+1, n+2, n+3
        f_n1 = expression.subs(n, self.n + 1)
        f_n2 = expression.subs(n, self.n + 2)
        f_n3 = expression.subs(n, self.n + 3)
        equation = Eq(f_n3, self.a * f_n2 + self.b * f_n1 + self.c * f_n0 + self.d_expr)  # Записываем уравнение
        coefficients = list(expression.free_symbols - {n})  # Вычисляем список коэффициентов, которые нужно найти, кроме n
        solution = solve(equation, coefficients, dict=True)

        coefficients_solution = solution[0]
        privateHeterogeneousSolution = expression.subs(coefficients_solution)
        return privateHeterogeneousSolution




    """Часть 3"""
    def find_general_solution(self): #Находит общее решение (однородное + частное)
        if self.general_solution is not None:
            return self.general_solution

        homogeneous_solution = self.find_homogeneous_solution()
        particular_solution = self.find_particular_solution()
        expression = homogeneous_solution + particular_solution # Общее неоднородное = общее однородное + частное неоднородное

        equation0 = Eq(self.f0, expression.subs(n, 0))  # Составляем уравнения по н.у
        equation1 = Eq(self.f1, expression.subs(n, 1))
        equation2 = Eq(self.f2, expression.subs(n, 2))

        coefficients = list(homogeneous_solution.free_symbols - {n})  # Достаем коэффициенты C1, C2, C3

        solution = solve((equation0, equation1, equation2), coefficients, dict=True)  # Решаем систему уравнений

        coefficients_solution = solution[0]
        generalSolution = expression.subs(coefficients_solution)  # Подставляем найденные коэффициенты и находим общее неоднородное

        self.general_solution = generalSolution
        return self.general_solution




    """Часть 4"""
    def f_recursive(self, n): #Проверка по рекурсии
        if n == 0:
            return self.f0
        if n == 1:
            return self.f1
        if n == 2:
            return self.f2

        return self.a * self.f_recursive(n - 1) + self.b * self.f_recursive(n - 2) + self.c * self.f_recursive(n - 3) + self.d_func(n - 3)

    def get_numeric_solution(self, n): #Проверка через общее неоднородное
        return self.general_solution.subs(self.n, n)




    """Вывод"""
    def print_solution(self):
        characteristic_equation = self.make_characteristic_equation()
        roots = self.find_roots()
        homogeneous_solution = self.find_homogeneous_solution()
        particular_solution = self.find_particular_solution()
        general_solution = self.find_general_solution()

        print("=" * 50)
        print("РЕШЕНИЕ РЕКУРРЕНТНОГО СООТНОШЕНИЯ")
        print("=" * 50)

        print(f"\nКоэффициенты: a={self.a}, b={self.b}, c={self.c}")
        print(f"Начальные условия: f(0)={self.f0}, f(1)={self.f1}, f(2)={self.f2}")

        print("\nХарактеристическое уравнение:")
        pprint(Eq(characteristic_equation, 0))

        print(f"\nКорни характеристического уравнения: ")
        pprint(roots)

        print("\nОбщее решение однородного уравнения ЛОРС:")
        pprint(homogeneous_solution)

        print("\nЧастное решение неоднородного уравнения ЛНРС:")
        pprint(particular_solution)

        print("\nОбщее решение неоднородного уравнения:")
        pprint(general_solution)

        print("\nПроверка:")
        for i in range(5):
            pprint(f'{self.f_recursive(i)} | {self.get_numeric_solution(i)}') #1 способ | 2 способ через общее неоднородное


if __name__ == "__main__":
    n = symbols('n')
    recurrence = RecurrentRelation(a=3, b=13, c=-15, f0=1, f1=2, f2=3, d_expr=Pow(2, n), d_func=lambda n: 2 ** n)
    recurrence.solve_completely()