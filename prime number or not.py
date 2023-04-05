23num=int(input("Enter the Number:"))
x=num
for i in range(2,num):
    if num%i==0:
        flag=0
        break
    else:
        flag=1
    if(flag==1):
        print(num," is Prime ")
    else:
        print(num," is not Prime ")
        