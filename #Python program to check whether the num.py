#Python program to check whether the number is a palidrome number or not:
orig=int(input("Enter number:"))#121
num=orig
rev=0
digit=0
while num>0:
    digit=num%10 #1
    rev=rev*10+digit #121
    num=num//10#12//10-0

if orig==rev:
    print(orig, "is a palindrome number")
else:
    print(orig,"is alpalindrome number")
