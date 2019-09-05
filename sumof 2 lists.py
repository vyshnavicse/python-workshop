l1=[10,20,30,40]
l2=[50,60,70,80]
k=len(l1)
l=[]
if len(l2)==k:
     for i in range(k):
          t=l1[i]+l2[i]
          l.append(t)
     print(l)
else:
     print("addition not possible")
     
          
