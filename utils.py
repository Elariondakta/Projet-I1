import platform, os

def clear():
    if platform.system() == "Windows": ##Dans les cas ou on est sur Windaube 
        os.system("cls")
    else:   ##Dans le cas ou on est sur Mac os ou Linux
        os.system("clear")