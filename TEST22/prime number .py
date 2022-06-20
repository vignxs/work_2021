x = int(input(' enter the number to check weather it is a prime number or not '))

if x>1:
    for j in range(2,x):
        if(x%j) == 0:
            print(x," is is not prime number")
            break
    else:
        print(x,'is a prime number')

else:
    print(x,' is not a prime number ')


