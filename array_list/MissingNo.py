# Find the missing number in an integer array 1 to 100

def missingNumber(list):
    sum_of_hundred = 100 * 101/2
    sum_of_list = sum(list)
    missing_number = sum_of_hundred - sum_of_list
    return missing_number

hundred = range(1,100)


print(missingNumber(list(hundred)))
