
def is_odd(n):
    return n%2 == 1

def some_recursion_hof(f, my_list : list[int], i) -> list[bool]:
    if i == len(my_list):
        return False
    else:
        if f(my_list[i]):
            return True
        else:
            return some_recursion_hof(f, my_list, i + 1)


if __name__ == "__main__":
    my_list = [2,4,6,9]
    print(some_recursion_hof(is_odd, my_list, 0))