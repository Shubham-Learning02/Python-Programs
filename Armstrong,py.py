import math
n=(int)(input("Enter a number: "))
l=len((str)(n))
t=n
c=0
sum=0
while(t!=0): 
    c=t%10 
    cc=math.pow(c,l)
    sum=sum+cc 
    t=t//10
print("Armstrong Number ") if sum==n else print("Not Armstrong Number ")