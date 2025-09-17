def ArrowPier(x, y):
    return not x and not y

def Xor(x, y):
    return (x and not y) or (not x and y)

def f(x, y, z):
    return Xor(not x, y) or ArrowPier(z, not (x and not z))
