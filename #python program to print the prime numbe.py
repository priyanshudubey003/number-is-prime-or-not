#python program to print the prime numbers for a user provided range
#input range is provided from the user
low=int(input("Enter Lower range: "))
up=int(input("Enter upper range: "))
for n in range(low,up+1):
    if n>1:
        for i in range(2,n):
            if(n%i)==0:
                break
            else:
                print(n)