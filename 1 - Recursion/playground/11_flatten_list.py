def flatten_recursion(my_list):
    res_list =  []
    for item in my_list:
        if isinstance(item, list):
            res_list.extend(flatten_recursion(item))
        else:
            res_list.append(item)
    return res_list

if __name__ == "__main__":
    my_list = [10,[20,[30,[40],35],50],60]
    print(flatten_recursion(my_list))