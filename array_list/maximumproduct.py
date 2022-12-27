def maximumproduct(input):
    maxnumber = input[0]
    secondmaxnumber = 0
    for i in range(len(input)):
        if maxnumber<input[i]:
            secondmaxnumber=maxnumber
            maxnumber = input[i]
    print(maxnumber*secondmaxnumber)
    print(f"pairs: ({secondmaxnumber},{maxnumber})")

maximumproduct([1,20,30,44,5,56,57,8,9,10,58])

