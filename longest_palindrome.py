from collections import Counter


def longestpalindrome(s):
    a = Counter(s)
    result = 0
    odd = 0
    for i in a.values():
        if i / 2 >= 1:
            if i % 2 == 0:
                result += i
            else:
                result += (i-1)
                odd = max(odd, i)

    if (odd >= 1) or (1 in a.values()):
        result += 1

    return result


if __name__ == "__main__":
    print(longestpalindrome("abccccdd"))
    print(longestpalindrome("a"))
    print(longestpalindrome("bb"))
