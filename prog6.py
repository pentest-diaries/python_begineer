# Rock-Paper-Scissor

import datetime
from pathlib import Path
import random

print("*************** Rock-Paper-Scissor ********************")

def gettime():
    return datetime.datetime.now()

def game(n):
    name=n
    i=0
    if Path(name).is_file():
        print("\nUser file already exist")
        with open (name,"a+") as op:
            op.write("\n-------------------------------------------------------------\n")
            b = int(input("Enter no of attempts:"))  ##NO OF ATTEMPT FOR THIS PROGRAM
            h_point = 0  # human point
            c_point = 0  # computer point
            print(str([str(gettime())]))

            while i<b:
                a = int(input("Enter your choice (1:Rock 2:Paper 3:Scissor):"))
                c = random.randint(1,3)
                if a==c:
                    print("It's a Tie")
                    op.write("\n" + str([str(gettime())]) + "It's a Tie")

                # Select Rock
                elif a==1 and c==2:
                    c_point=c_point + 1
                    print("Human select Rock and Computer select Paper")
                    print("Computer Win 1 point")
                    print(f"computer_point is {c_point} and your point is {h_point} \n ")
                    op.write("\n" + str([str(gettime())]) + "Computer Win 1 point")
                elif a==1 and c==3:
                    h_point = h_point + 1
                    print("Human select Rock and Computer select Scissor")
                    print("Human Win 1 point")
                    print(f"computer_point is {c_point} and your point is {h_point} \n ")
                    op.write("\n" + str([str(gettime())]) + "Human Win 1 point")

                # Select Water
                elif a==2 and c==1:
                    print("Human select Paper and Computer select Rock")
                    print("Human Win 1 point")
                    h_point = h_point + 1
                    print(f"computer_point is {c_point} and your point is {h_point} \n ")
                    op.write("\n" + str([str(gettime())]) + "Human Win 1 point")
                elif a==2 and c==3:
                    c_point = c_point + 1
                    print("Human select Paper and Computer select Scissor")
                    print("Computer Win 1 point")
                    print(f"computer_point is {c_point} and your point is {h_point} \n ")
                    op.write("\n" + str([str(gettime())]) + "Computer Win 1 point")

                #Select Gun
                elif a==3 and c==1:
                    c_point = c_point + 1
                    print("Human select Scissor and Computer select Rock")
                    print("Computer Win 1 point")
                    print(f"computer_point is {c_point} and your point is {h_point} \n ")
                    op.write("\n" + str([str(gettime())]) + "Computer Win 1 point")
                elif a==3 and c==2:
                    h_point = h_point + 1
                    print("Human select Scissor and Computer select Paper")
                    print("Human Win 1 point")
                    print(f"computer_point is {c_point} and your point is {h_point} \n ")
                    op.write("\n" + str([str(gettime())]) + "Human Win 1 point")
                else:
                    print("You have selected the wrong choice!!!!")
                i=i+1  ### no of attempts increment
                print(f"{b-i} is left out of {b} \n")

            if c_point == h_point:
                print("Tie")
                op.write("\n" + str([str(gettime())]) + "Final result is a Tie")
                op.write(f"your point is {h_point} and computer point is {c_point}")
            elif c_point > h_point:
                print("Computer wins and you loose")
                op.write("\n" + str([str(gettime())]) + "Final result Computer wins and you loose")
                op.write(f"your point is {h_point} and computer point is {c_point}")
            else:
                print("you win and computer loose")
                op.write("\n" + str([str(gettime())]) + "Final Result you win and computer loose")
                op.write(f"your point is {h_point} and computer point is {c_point}")
        print(f"your point is {h_point} and computer point is {c_point}")
        op.close()
    else:

        with open(name,"x") as f:
           ## f.write("\n--------------------------------------------------------------\n")
            b = int(input("Enter no of attempts:"))  ##NO OF ATTEMPT FOR THIS PROGRAM
            h_point = 0  # human point
            c_point = 0  # computer point
            print(str([str(gettime())]))
            while i < b:
                a = int(input("Enter your choice (1:Rock 2:Paper 3:Scissor):"))
                c = random.randint(1, 3)
                if a == c:
                    print("It's a Tie")
                    f.write("\n" + str([str(gettime())]) + "It's a Tie")

                # Select Rock
                elif a == 1 and c == 2:
                    c_point = c_point + 1
                    print("Human select Rock and Computer select Paper")
                    print("Computer Win 1 point")
                    print(f"computer_point is {c_point} and your point is {h_point} \n ")
                    f.write("\n" + str([str(gettime())]) + "Computer Win 1 point")
                elif a == 1 and c == 3:
                    h_point = h_point + 1
                    print("Human select Rock and Computer select Scissor")
                    print("Human Win 1 point")
                    print(f"computer_point is {c_point} and your point is {h_point} \n ")
                    f.write("\n" + str([str(gettime())]) + "Human Win 1 point")

                # Select Water
                elif a == 2 and c == 1:
                    print("Human select Paper and Computer select Rock")
                    print("Human Win 1 point")
                    h_point = h_point + 1
                    print(f"computer_point is {c_point} and your point is {h_point} \n ")
                    f.write("\n" + str([str(gettime())]) + "Human Win 1 point")
                elif a == 2 and c == 3:
                    c_point = c_point + 1
                    print("Human select Paper and Computer select Scissor")
                    print("Computer Win 1 point")
                    print(f"computer_point is {c_point} and your point is {h_point} \n ")
                    f.write("\n" + str([str(gettime())]) + "Computer Win 1 point")

                # Select Gun
                elif a == 3 and c == 1:
                    c_point = c_point + 1
                    print("Human select Scissor and Computer select Rock")
                    print("Computer Win 1 point")
                    print(f"computer_point is {c_point} and your point is {h_point} \n ")
                    f.write("\n" + str([str(gettime())]) + "Computer Win 1 point")
                elif a == 3 and c == 2:
                    h_point = h_point + 1
                    print("Human select Scissor and Computer select Paper")
                    print("Human Win 1 point")
                    print(f"computer_point is {c_point} and your point is {h_point} \n ")
                    f.write("\n" + str([str(gettime())]) + "Human Win 1 point")
                else:
                    print("You have selected the wrong choice!!!!")
                i = i + 1  ### no of attempts increment
                print(f"{b - i} is left out of {b} \n")

            if c_point == h_point:
                print("Tie")
                f.write("\n" + str([str(gettime())]) + "Final result is a Tie")
                f.write(f"your point is {h_point} and computer point is {c_point}")
            elif c_point > h_point:
                print("Computer wins and you loose")
                f.write("\n" + str([str(gettime())]) + "Final result Computer wins and you loose")
                f.write(f"your point is {h_point} and computer point is {c_point}")
            else:
                print("you win and computer loose")
                f.write("\n" + str([str(gettime())]) + "Final Result you win and computer loose")
                f.write(f"your point is {h_point} and computer point is {c_point}")
        print(f"your point is {h_point} and computer point is {c_point}")
        f.close()

    print("successfully written")

n=str(input("Enter your name:"))
game(n)