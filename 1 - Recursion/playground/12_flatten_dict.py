
def flatten_dict_recursion(my_dict):
    res_dict = {}
    for key, value  in my_dict.items():
        if isinstance(value, dict):
            temp_dict = flatten_dict_recursion(value)
            for k,v in temp_dict.items():
                res_dict[k] = temp_dict[k]
        else:
            res_dict[key] = value
    return res_dict


if __name__ == "__main__":
    my_dict = {"sno" : 1, "name" : "sandeep", "address" : {"city" : "chittoor", "state" : "ap", "country" : "india", "location" : {"d.no" : "24-10/46-1"}}}
    print(flatten_dict_recursion(my_dict))