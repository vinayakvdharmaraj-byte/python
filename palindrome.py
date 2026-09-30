n=int(input("enter the number :"))
rev=0
org=n
while(org>0):
    r=org%10
    rev=(rev*10)+r
    org=org//10
print(f"reverse of this number is {rev}")
if rev==n:
    print(f"{n} is a palindrome")
else:
    print(f"{n} is not a palindrome")