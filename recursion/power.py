# calculate power of a number

def power(x, n):

    if n == 0:
        return 1
    elif n < 0:
        return 1/(power(x, n+1)*x)
    else:
        return power(x, n-1)*x


print(power(4, -1))
