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
def updateitem():
      d=additem(n)
      rollno=input("enter rollno to update ")
      name=input("enter name to update" )
      branch=input("enter branchto update ")
      d.update({rollno:[name,branch]})
      return d
print(updateitem())

