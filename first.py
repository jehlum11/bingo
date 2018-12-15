def add(a, b):
    z = a + b
    print('\nAddition of {} and {} equals to {}.\n'.format(a, b, z))


def mul(a, b):
    z = a * b
    print('\nMultiplication of {} and {} equals to {}.\n'.format(a, b, z))


def sub(a, b):
    z = a - b
    print('\nSubtraction of {} and {} equals to {}.\n'.format(a, b, z))


def div(a, b):
    if b == 0:
        print("[INFO] A division by zero is not possible, please give appropriate values.")
    else:
        z = a / b
        print('\nDivision of {} and {} equals to {}.\n'.format(a, b, z))
