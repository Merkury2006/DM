def ArrowPier(x, y):
    return not x and not y


def Xor(x, y):
    return (x and not y) or (not x and y)


def f(x, y, z):
    return Xor(not x, y) or ArrowPier(z, not (x and not z))


print("x y z f fx fy fz")
fict_per = [True, True, True]
for x in range(2):
    for y in range(2):
        for z in range(2):

            result = f(x, y, z)
            per = [x, y, z]
            curResults = []

            for i in range(3): #Проходимся и меняем последовательно на not x, not y, not z, если результат хоть раз не совпал, значит переменная не фиктивная
                curPer = per.copy()
                curPer[i] = not curPer[i]
                curResult = f(*curPer)
                if curResult != result:
                    fict_per[i] = False
                curResults.append(int(curResult))

            print(f"{x} {y} {z} {int(result)} {curResults[0]}  {curResults[1]}  {curResults[2]}")

print(f"Фиктивная переменная x: {'Да' if fict_per[0] else 'Нет'}")
print(f"Фиктивная переменная y: {'Да' if fict_per[1] else 'Нет'}")
print(f"Фиктивная переменная z: {'Да' if fict_per[2] else 'Нет'}")
