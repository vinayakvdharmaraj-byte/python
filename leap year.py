y=int(input("enter the final year :"))
print("future leap years from 2021 :")
for i in range(2021,y+1):
    if((i%4==0) and (i%100!=0) or (i%400==0)):
        print(i)