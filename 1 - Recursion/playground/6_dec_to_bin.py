from validate_data import is_non_zero

def dec_to_bin_recursion(n):
    if is_non_zero(n):
        dec_to_bin_recursion(n//2)
        print(n % 2, end=" ")


def dec_to_bin_non_recursion(n):
    remainders = []
    while is_non_zero(n):
        remainders.insert(0, str(n%2))
        n = n//2
    print(" ".join(remainders))


if __name__ == "__main__":
    n = 13
    print("Recursion : Decimal to Binary equivalent of {0} is ".format(n), end=" ")
    dec_to_bin_recursion(n)
    print()
    print("Iterative : Decimal to Binary equivalent of {0} is ".format(n), end=" ")
    dec_to_bin_non_recursion(n)
