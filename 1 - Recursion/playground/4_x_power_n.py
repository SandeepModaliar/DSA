def x_power_n_recursion(x, n):
    if n == 1 :
        return x
    else:
        return x * x_power_n_recursion(x, n-1)

def x_power_n_tail_recursion(x, n, res):
    if n == 0:
        return res
    else:
        return x_power_n_tail_recursion(x, n-1, res*x)


if __name__ == "__main__":
    x = 2
    n = 10
    print("{0} Power {1} is {2} using Recursion".format(x,n,x_power_n_recursion(x,n)))

    print("{0} Power {1} is {2} using Tail Recursion".format(x,n,x_power_n_tail_recursion(x,n,1)))