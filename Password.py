import string
import random

length=int(input("Enter length of password:-"))

print('''
      Choose a character set for creating Strong Password:-
      1. Digits
      2. Special Characters
      3. Letters
      4. Exit
      ''')

character=""
while(True):
    choice=int(input("Enter your choice:-"))
    
    if(choice==1):
        character+=string.digits
        
    elif(choice==2):
        character+=string.punctuation    
    
    elif(choice==3):
        character+=string.ascii_letters
        
    elif(choice==4):
        break
    
    else:
        print("Enter valid inputs")

password=[]

for i in range(length):
    randomchar=random.choice(character)
    password.append(randomchar)

print("The random Passowrd is "+"".join(password))