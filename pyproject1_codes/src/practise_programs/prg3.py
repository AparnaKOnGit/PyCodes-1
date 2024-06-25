# Swap 2 variables without using 3rd variable

# Strings
def swap_strings():
    xs = 'SBI'
    ys = 'Begumpet'
    print(xs, ys)
    # Using Unpacking
    xs, ys = ys, xs
    print(xs, ys)


# Integers
def swap_integers():
    xi = 44
    yi = -57
    print(xi, yi)
    # Using XOR
    xi = xi ^ yi
    yi = xi ^ yi
    xi = xi ^ yi
    print(xi, yi)


# Float/Double
def swap_decimals():
    xd = 37.7877782
    yd = 0.376754469
    print(xd, yd)
    xd = xd * yd
    yd = xd / yd
    xd = xd / yd
    print(xd, yd)
