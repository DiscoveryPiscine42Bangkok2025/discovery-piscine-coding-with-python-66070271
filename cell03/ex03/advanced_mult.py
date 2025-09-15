num = 0
while(num <= 10):
    num1 = 0
    count = 0
    print(f"Table de {num} : ",end=" ")
    while(count <= 10):
        print(num1,end=" ")
        count += 1
        num1 += num
    print("")
    num += 1