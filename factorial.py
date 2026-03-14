n=int(input("enter the value:"))
def factorial(n):
  if(n==0 or n==1):
    return1
  else:
    fact= n * (n-1)
    return(fact)
print(f"factorial of the {n}:{fact}")
