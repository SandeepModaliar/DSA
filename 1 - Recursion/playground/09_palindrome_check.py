
def palindrome_check_recursion(s : str, low : int, high : int) -> bool :
    if low >= high :
        return True
    else:
        if s[low] == s[high]:
            return palindrome_check_recursion(s, low + 1, high - 1)
        else:
            return False


if __name__ == "__main__":
    my_str = "emadMMdame"
    print(palindrome_check_recursion(my_str, 0, len(my_str) -1))
