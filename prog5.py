#Statement for the code:

#Create a  program of routine tracker in which user have to input the name then select whether to log new entry or add in the existing one or can retrieve the data which is already added. Here we have to create a file with the name of user for different activity like ( for food -> food_username.txt and for Exercise -> Exc_username.txt).

#Make sure entry of data in file should be along with current date and time.


import datetime
from pathlib import Path

def gettime():
    return datetime.datetime.now()

def log1(a):
    c=int(input("\nSelect 1 for Food and 2 for Exercise:\n"))
    if c==1:
        prewritten_tag = "Food_"
        full_filename = prewritten_tag + a
        if Path(full_filename).is_file():
            print("\nFile exist")
            #full_filename.open(,"w+")
            #h.close()
            with open (full_filename,"a+") as op:
                user_input = input("\nvalue:")
                #print("\n")
                op.write("\n" + str([str(gettime())])  + ":" +  user_input)
                op.close()

        else:
            with open(full_filename, "x") as f:
                user_input = input("\nvalue:")
                f.write(str([str(gettime())])  + ":" +  user_input)
                f.close()
        print("successfully written")

    elif c==2:
        prewritten_tag = "Exc_"
        full_filename = prewritten_tag + a
        if Path(full_filename).is_file():
            print("File exist")
            with open (full_filename,"a+") as op:
                user_input = input("\nvalue:")
                print("\n")
                op.write("\n" + str([str(gettime())])  +  user_input)
                op.close()

        else:
            with open(full_filename, "x") as f:
                user_input = input("\nExercise: ")
                f.write(str([str(gettime())])  +  user_input)
                f.close()
        print("successfully written")
    else:
        print("plz enter valid input")

def ret(a):
    e = int(input("\nSelect 1 for Food and 2 for Exercise:\n"))

    if e==1:
        prewritten_tag = "Food_"
        full_filename = prewritten_tag + a
        if Path(full_filename).is_file():
            print("\nFile exist")
            with open (full_filename,"r+") as op:
                for i in op:
                    print(i, end="")
            op.close()
    elif e==2:
        prewritten_tag = "Exc_"
        full_filename = prewritten_tag + a
        if Path(full_filename).is_file():
            print("\nFile exist")
            with open(full_filename,"r+") as op:
                for i in op:
                    print(i, end="")
            op.close()
    else:
        print("\nplz enter valid input")

print("********** Routine Tracker  ************\n")
a=str(input("\nEnter the name of user:\n"))
b=int(input("\nSelect 1 for log and 2 for retreive:\n"))
if b==1:
    log1(a)
elif b==2:
    ret(a)
else:
    print("invalid entry")