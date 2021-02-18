print("*********Welcome in the world of calculator*********")
print("Enter you name: ")
name = str(input())
print("**** Welcome*****", name, "Enjoy the calculator")
print("enter first no:")
c1 = int(input())
print("enter second no:")
c2 = int(input())
print("enter operator + - * /:")
c3 = input()
if c3 == '+':
    num = c1 + c2
    print("the sum result:", num)
elif c3 == '-':
    num = c1 - c2
    print("the subtract result:", num)
elif c3 == '*':
    num = c1 * c2
    print("the multiply result:", num)
elif c3 == '/':
    num = c1 / c2
    print("the divide result:", num)
else:
    print("you have selected the wrong operator")
