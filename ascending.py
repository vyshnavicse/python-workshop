a=19
b=42
c=23
if  a>c  and a>b:
     print(a)
     if  b>c:
          print(b)
          print(c)
     else:
          print(c)
          print(b)
elif b>a and b>c:          
      print(b)
      if c>a:
          print(c)
          print(a)
      else:
          print(a)
          print(c)
else:
     print(c)
     if b>a:
          print(b)
          print(a)
     else:
          print(a)
          print(b)
               
