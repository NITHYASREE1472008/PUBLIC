a = int(input("enter the digit:"))
s=0
while(a>0):
  r=a%10
  s=s+r
  a=a//10
print("sum of the digits= ",s)
