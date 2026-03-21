import os   
menuName = "menux.txt"

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

menuConcept = input("Okay let's create restaurant's menu!\nWhat should be your reastrant's menu?\n")
print(menuConcept)
        
