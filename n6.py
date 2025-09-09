from function import f

conjunctions = []
disjunctions = []

for x in range(2):
    for y in range(2):
        for z in range(2):
            if (f(x, y, z)):
                conjunctions.append(f"({'x' if x else '¬x'} ∧ {'y' if y else '¬y'} ∧ {'z' if z else '¬z'})")
            else:
                disjunctions.append(f"({'¬x' if x else 'x'} ∨ {'¬y' if y else 'y'} ∨ {'¬z' if z else 'z'})")

sdnf = " ∨ ".join(conjunctions)
sknf = " ∧ ".join(disjunctions)

print("СДНФ: " + sdnf)
print("СКНФ: " + sknf)

print("-" * 100)
print("| x | y | z | f |")
for x in range(2):
    for y in range(2):
        for z in range(2):
            result = f(x, y, z)
            print(f'| {x} | {y} | {z} | {int(result)} |')