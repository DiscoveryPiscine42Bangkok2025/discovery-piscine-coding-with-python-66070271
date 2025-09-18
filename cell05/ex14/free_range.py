import sys

args = sys.argv[1:]

if len(args) != 2:  
    print("none")
else:
    try:
        start = int(args[0])
        end = int(args[1])
        arr = list(range(start, end + 1))  
        print(arr)
    except ValueError:
        print("none") 