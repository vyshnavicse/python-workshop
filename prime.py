n=int(input("enter a number"))
i=1
j=0
while i<=n:
     if n%i==0:
          j+=1
     i+=1
     
if j==2:
     print("given number is prime")
else:
     print("given number is not a prime")
     
