# Exercise 4
# Pattern Printing pyramid format
# Input = Integer value var1
# Input var2 (1 for forward pyramid pattern and 0 for reverse pyramid pattern)

print("************ Pattern Pyramid Format **************")
var1=int(input("Enter the value:"))
var2=int(input("Enter 1 for Forward pattern and 0 for Reverse pattern:"))

def pattern(var1,var2):
    if var2==1:
        var3=1
        var4=var1-1
        while var3<=var1:
            for j in range(0, var4):
                print(end=" ")
            print(var3 * " * ")
            print(" \r")   # ending line after each row
            var3=var3+1
            var4=var4-1

    elif var2==0:
        var5=0
        while var1>0:
            for i in range(var5,0,-1):
                print(end=" ")
            print(var1 * " * ")
            print("\r")    # ending line after each row
            var1=var1-1
            var5=var5+1
    else:
        print("wrong pattern selection")

pattern(var1,var2)