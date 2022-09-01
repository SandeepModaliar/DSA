
def string_reverse_recursion(s : str, low : int, high : int) -> str:
    if low >= high:
        return s
    else:
        s[low] , s[high] = s[high] , s[low]
        return string_reverse_recursion(s, low + 1, high -1)

if __name__ == "__main__":
    my_str = "sandeep"
    print(string_reverse_recursion(list(my_str), 0, len(my_str) - 1))