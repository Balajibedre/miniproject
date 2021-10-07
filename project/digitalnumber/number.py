# write a program to get sum of digital of a number
# code

def getsum(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)

    return sum
n = 999
print(getsum(n))