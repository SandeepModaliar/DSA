
def check_anagram_1(s, t):
    countS = {}
    countT = {}
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        countS[s[i]] = countS.get(s[i], 0) + 1
        countT[t[i]] = countT.get(t[i], 0) + 1
    for k in countS.keys():
        if countS[k] != countT.get(k, 0):
            return False
    else:
        return True


if __name__ == "__main__":
    a = "creative"
    b = "reactive"
    print("{0} is {2} of {1}".format(a, b, "an Anagram" if check_anagram_1(a,b) else "not an Anagram"))