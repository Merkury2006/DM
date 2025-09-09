def ArrowPier(x, y):
    return not x and not y


def Xor(x, y):
    return (x and not y) or (not x and y)


def f(x, y, z):
    return Xor(not x, y) or ArrowPier(z, not (x and not z))


def dual_f(x, y, z):
    return not f(not x, not y, not z)


conjunctions = []
for x in range(2):
    for y in range(2):
        for z in range(2):
            result = not f(not x, not y, not z) #Использую преобразование СДНФ
            if (result):
                conjunctions.append(f"({'x' if x else '¬x'} ∧ {'y' if y else '¬y'} ∧ {'z' if z else '¬z'})")

dual_transformed_f = " ∨ ".join(conjunctions)
print(dual_transformed_f)