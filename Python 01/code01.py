***
In this code user will enter a 3 digit number,
and the double of the reverse will be shown in the output
***

var = int(input())
y = str(var // 10)
y = str(int(y) % 10)
w = int(str(var % 10)+str(y)+str(var // 100))
w = w*2
print(w)
