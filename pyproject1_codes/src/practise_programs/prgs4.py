import PrgS1 as ps1


# Program to check if a given number is prime or not
def isPrime(num: int) -> bool:
    ct = 0
    limit: int = int(ps1.sqr_root_c(num))
    for i in range(2, limit):
        if (num % i) == 0:
            ct += 1
    return ct < 1


# Iconic Quake 3 Game algorithm
def fastInverseSquareRoot(x):
    x_half = 0.5 * x
    i = int(x)
    i = 0x5f3759df - (i >> 1)
    y = float(i)
    y *= (1.5 - x_half * y * y)
    return y


# print(isPrime(223))
# print(isPrime(64))

