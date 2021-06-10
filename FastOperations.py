def func():
    print(True * 1)
    print(False * 1)
    print((True * 2 + False) * -True)


print(func())


def fast_mul(a, b):
    result = 0
    while a != 0:
        if a % 2 == 1:
            result += b
        a = int(a / 2)
        b = b * 2
    return result


def fast_pow(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return fast_pow(a, int(n / 2)) * fast_pow(a, int(n / 2))
    if n % 2 == 1:
        return fast_pow(a, n - 1) * a


print(fast_mul(123, 123))
print(fast_pow(2, 16))