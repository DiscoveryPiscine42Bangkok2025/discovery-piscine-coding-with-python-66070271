import sys

if len(sys.argv) != 2:
    print("none")
else:
    param = sys.argv[1]
    word = input("What was the parameter? ")
    if word == param:
        print("Good job!")
    else:
        print("Nope, sorry...")