

p = "5549"
c = 3


while c>0:
 
 a = int(input("Enter the password: "))
 
 if a == p:
     print("sucessfully entered")

 else:
  c = c-1
  print("You Entered Wrong password")
  print(f"{c} attempt left")
  
