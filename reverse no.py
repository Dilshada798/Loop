num=int(input("enter the number"))
# num1=int(input())
rev=0
while num>0:
    rev=(rev*10)+num%10
    num=num//10
print(rev)
print()



