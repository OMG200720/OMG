num = int(input("enter number:"))
if num >1:
    for i in range (2,num):
        if num %i ==0:
            print("not prime")
            break;
        else:
            print("prime number")
else:
    print("not a prime number")
