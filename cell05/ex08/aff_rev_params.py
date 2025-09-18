import sys
if(len(sys.argv) < 3):
    print("none")
else:
   temp = sys.argv[1:]
   for i in reversed(temp):
       print(i)