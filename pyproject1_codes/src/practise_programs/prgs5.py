# Factorial

# Iterative:
def calc_fact_itr(x) -> int:
    f = 1
    if x == 0 or x == 1:
        return f
    while x >= 2:
        f *= x
        x -= 1
    return f


# Recursive:
def calc_fact_rec(x) -> int:
    if x == 0 or x == 1:
        return x
    return x * calc_fact_rec(x - 1)


# Iterative fast
def calc_fact_itr2(x) -> int:
    l = 1
    h = x
    ans = 1
    while h > l:
        ans *= h * l
        h -= 1
        l += 1
    if x % 2 != 0:
        ans *= l
    return ans


# Recursive fast
def calc_fact_rec2(x) -> int:
    return _calc_fact(1, x, x)


def _calc_fact(s, h, v) -> int:
    if s >= h:
        return 1 if (v % 2 == 0) else s
    return s * h * _calc_fact(s + 1, h - 1, v)


# -----------------------------------------------------------

# Fibonacci
def fibonacci_itr(r) -> None:
    n1 = 0
    n2 = 1
    print("0, 1, ", end='')
    for i in range(0, r - 1):
        c = n1 + n2
        print(f'{c}, ', end='')
        n1 = n2
        n2 = c
    print(n1 + n2)


def fibonacci_rec(r: int) -> None:
    print('0, 1, ', end='')
    _fibo_rec(0, 1, r)


def _fibo_rec(n1, n2, r: int) -> None:
    if r == 1:
        print(n1 + n2)
        return
    c = n1 + n2
    print(f'{c}, ', end='')
    _fibo_rec(n2, c, r - 1)


# print("------")
# fibonacci_rec(13)
# print("-------")







