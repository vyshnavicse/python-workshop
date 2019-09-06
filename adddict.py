def additem(n):
      d={}
    for i in range(n):
        rollno=input("enter rollno")
        name=input("enter name")
        branch=input("enter branch")
        d[rollno]=[name,branch]
    return d
n=int(input("enter a value"))
print(additem(n))


