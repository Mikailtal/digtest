n=5

choice=int(input("Enter user choice"))

if choice==1 or choice==2:
    for i in range(0,n):
            for j in range(0,i):
                print(" ",end="")
            for j in range(0,n-i):
                print("*",end=" ")
            print("\r")
    if choice==2:
        for i in range(2,n+1):

                for j in range(0,n-i):
                    print(" ",end="")
                for j in range(0, i):
                    print("-", end=" ")
                print("\r")
else:
    print('Invalid Input')