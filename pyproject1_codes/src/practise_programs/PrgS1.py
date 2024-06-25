# Program to find square root of a given number:

# Finding a square root using Herons formula
def sqr_root_1(n, precision: float = 1e-6) -> float:
    x0: float = float(n)
    while True:
        x1: float = (x0 + (n / x0)) / 2
        if abs(x1 - x0) < precision:
            return x1
        x0 = x1


# Finding the closest integer to the square root using modified binary search
def sqr_root_c(n: int) -> int:
    low: int = 0
    high = n
    ans: int = 1
    while low <= high:
        mid: int = int((low + high) / 2)
        if (mid * mid) <= n:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans


# print(sqr_root_1(64))
# print(sqr_root_c(64))
# print(sqr_root_1(223))
# print(sqr_root_c(223))
