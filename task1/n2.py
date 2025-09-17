from task1.function import f


print("| x | y | z | f |")
for x in range(2):
    for y in range(2):
        for z in range(2):
            result = f(x, y, z)
            print(f'| {x} | {y} | {z} | {int(result)} |')