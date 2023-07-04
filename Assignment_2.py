#vowels list create
vowels = "aeiouAEIOU"
def remove_vowels(text):
    consterd = 'Enterd text constructor is : '
    return consterd+''.join([
      # declare the variable first = x
      x
      # write the text in loop 
      for x in text 
      #check the text vowels is  not
      if x not in vowels])+'\n'
def check_vowels(text):
  volwe = 'Enterd text vowels is : '
  return volwe+''.join([
      # declare the variable first = x
      x
      # write the text in loop 
      for x in text 
      #check the text vowels is  not
      if x in vowels])+'\n'
  
while True:
  #get the user input 
  input_string = input("Enter the text to filtering vowels & constructor")
  # calling the function
  output_string = remove_vowels(input_string)
  # calling the function
  otp=check_vowels(input_string)
  #print the result
  print(output_string,otp)
  # countinue function create 
  continueGame = input("\nCan You Continue this Game type = y or n"
  )
  #check user continue or not
  if continueGame == "Y" or continueGame == "y":
    continue
  else:
    break

