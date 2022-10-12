# convert decimal to binary


def dectobin(n):
    assert int(n) == n, "Argument must be integer"
    if n//2 == 0:
        return 1
    return ((dectobin(int(n)//2)*10)+int(n) % 2)


print(dectobin(13))
