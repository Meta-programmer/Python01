# In this program, you read two numbers from the input and print a larger number in the output.
# The first input line contains the first number. The second input line contains the second number.
# It is guaranteed that the input numbers are positive integers. If two input numbers are not equal, print one of them.

x = int(input())
y = int(input())
if x > y:
    print(x)
elif y > x:
    print(y)
else :
    print(x or y)
