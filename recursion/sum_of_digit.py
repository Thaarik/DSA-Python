# FInd the sum of digits os positive integer number using recursion

def sumofdigit(n):
    assert n >= 0 and int(n) == n, "NUmber must be positive integer"
    if n // 10 == 0:
        return int(n)
    else:
        return (sumofdigit(int(n)//10)+int(n) % 10)


print(sumofdigit(22232))
