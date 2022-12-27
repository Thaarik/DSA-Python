# Two sum. 

def twosum(input,target):
    for i in range(len(input)):
        for j in range(i+1,len(input)):
            if (input[i]==input[j]):
                continue
            elif(input[i]+input[j]==target):
                print(i,j)

input = [1,2,5,3,2,4,2,1]
target = 6

twosum(input,target)
