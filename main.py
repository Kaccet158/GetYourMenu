import os 
from gemini_chat import GeminiBot

#Files managment 
menuName = "menu.txt"

if os.path.exists(menuName):
    with open(menuName, "r") as file:
        menu = file.read()
else:
    print("There is no menu\nDo you want to create one? (y/n)")
    if input().lower() != "n":
        with open(menuName, "x") as file:
            menu = file.write("Yup, new menu was created!")
    else: 
        print("Well, nothing will be created...")
        exit()

#Gemini Funciotnality
GeminiFunction = GeminiBot()
menuStartMessage = "Okay let's create restaurant's menu!\nWhat should be your restaurant's menu?\n"
menuConcept = input(menuStartMessage)
answer = GeminiFunction.ask(menuConcept)
print(answer)
menuEndMessage = input("Okay, your menu  created! Do you want to add something? (y/n) ")



        
