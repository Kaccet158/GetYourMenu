import os 
from gemini_chat import GeminiBot
from rich.console import Console

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
console = Console()

menuStartMessage = "Okay let's create restaurant's menu!\nWhat should be your restaurant's menu?\n"
menuConcept = input(menuStartMessage)

with console.status(
    "[bold cyan]Crafting menu . . .[/bold cyan]", 
    spinner = "dots",
    spinner_style = "bold cyan"
    ):
    answer = GeminiFunction.ask(menuConcept)
print(answer)

while True: 
    menuEndMessage = input("Your menu looks gorgeuos! Do you want to add something? (y/n) ")
    if menuEndMessage.lower() != "n":
        menuMessage = input("Okay so what we need to change?\n")
        answer = GeminiFunction.ask(menuMessage)
        print(answer)
    else: 
        print("Okay that's all. See ya!")
        break 




        
