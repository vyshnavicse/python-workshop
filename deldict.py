def  additem(n):
      d={}
      for i in range(n):
         rollno=input("enter rollno")
         name=input("enter name")
         branch=input("enter branch")
         d[rollno]=[name,branch]
      return d 
n=int(input("enter a value"))
def deleteitem():
      d=additem(n)
      k=input("enter the rollno to deleted")
      d.pop(k)
      return d
print(deleteitem())
