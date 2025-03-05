def catAndMouse(x, y, z):
    step1 = abs(z - x)
    step2 = abs(z - y)
    if step1 == step2:
        return "Mouse C"
    elif step1 < step2:
        return "Cat A"
    elif step2 < step1:
        return "Cat B"
