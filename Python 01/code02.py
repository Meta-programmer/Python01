# Read a number from input, find the first decimal number bigger than input, which is a multiple of 10.
# only if and else and elif must be used

x = int(input())
if x % 10 == 0:
    print(x + 10)
else :
    y = 10 - (x % 10)
    print(x+y)
