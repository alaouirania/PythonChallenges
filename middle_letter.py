def mid(string):
    if (len(string)%2) == 0:
         return ""
    else:
        middle = int(len(string) / 2)
        return string[middle: middle + 1]
print(mid("aaa"))
