print("******** Welcome in the world of guessing topper percentage *********")
n=0
m=9
while n<9:
    in1 = int(input("Enter your Guess Percentage of Topper:"))
    if in1>85:
        print("Entered Percentage is higher than the percentage scored by Topper")
        m=m-1
        print("How many attempts left:", m)
        n=n+1
        continue
    elif in1<85:
        print("Entered Percentage is Lower than the percentage scored by Topper")
        m=m-1
        print("How many attempts left:", m)
        n=n+1
        continue
    else:
        print("Entered Percentage is a perfect guess")
        m=m-1
        if n==0:
            n=n+1
        else:
            break
        break
print("Number of count used:",n)
##print("How many attempts left:",m)


