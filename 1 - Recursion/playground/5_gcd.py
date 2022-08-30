from validate_data import is_zero


def gcd_recursion(a, b):
    if is_zero(b):
        return a
    elif a < b:
        return gcd_recursion(b, a)
    else:
        return gcd_recursion(b, a % b)


def gcd_with_out_recursion(a,b):
    if a < b:
        a, b = b, a
    while True:
        if is_zero(b):
            return a
        t = a
        a = b
        b = t % b
    return a


if __name__ == "__main__":
    m = 48
    n = 18
    print("GCD of {0} and {1} is {2} ".format(m, n, gcd_recursion(m, n)))
    print("GCD of {0} and {1} is {2} ".format(m, n, gcd_with_out_recursion(m, n)))

