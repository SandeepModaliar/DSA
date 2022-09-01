
def product_of_array_recursion(i : int, my_list : list[int]) -> int :
    if i == len(my_list):
        return 1
    else:
        return my_list[i] * product_of_array_recursion(i + 1, my_list)


if __name__ == "__main__":
    my_list = [1,2,3,4]
    print(product_of_array_recursion(0, my_list))
