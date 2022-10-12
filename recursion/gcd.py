# find GCD
# using euclidean algorithm:
# gcd (48,18) -> 48%18 -> quotient = 2 , reminder = 12
# gcd ( 18,12) -> 18%12 -> quotient = 1, reminder = 6
# gcd (12,6) -> 12 % 6 -> quotient = 2, remainder =0 -----------> so GCD is 6

def gcd(a, b):
    if (a < 0):
        a = a*-1
    if (b < 0):
        b = b*-1
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)


print(gcd(18, 48))
