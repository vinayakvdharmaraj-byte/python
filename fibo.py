n=int(input("Enter the number:"))
x,y=0,1
count=0
if n<=0:
    print("Enter a positive number...")
elif n==1:
    print("Fibonacci sequence upto",n,":")
    print(x)
else:
    print("Fibonacci sequence:")
while count<n:
    print(x)
    z=x+y
    x=y
    y=z
    count+=1