#Python Program to print all Prime Numbers in an interval:
lower=50
upper=100
print("prime numbers between",lower,"to",upper)
for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
            else:
                print(num)
