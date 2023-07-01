'''
Assignment One 
Write a Python program that asks the user to enter their age and then prints
"You are a minor" if their age is less than 18, "You are an adult" if their age
is greater than or equal to 18 and less than 65, and "You are a senior" if their
age is 65 or greater
'''
print("\t\t\t\tAge Check Game")
while(True):
  try:
   userAge = int(input("Enter Your Age : "))
   if(userAge<18):
     print("You are a minor because your age is:",userAge)
   elif(userAge>=18 and userAge<=64):
     print("You are a adult because your age is:",userAge)
   else:
    print("You are a senior because your age is :",userAge)
    continues = input("\tCan you Continue this game type (y or n) :")
    if(continues == "Y" or continues =='y'):
      continue
    else:
      break
    # TODO: write code...
  except Exception as e:
    print("error is : ",e)
  