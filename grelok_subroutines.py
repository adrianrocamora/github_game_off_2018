import os

# Start
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def routine_010():
    cls()
    print("Reign of Grelok")
    input('')

def routine_100():
    cls()
    print("> (Plains) Look Around (l)")
    print("> Go North (n)")
    print("> Go South (s)")
    print("> Go East (e)")
    print("> Go West (w)")
    print("> Inventory (i)")
    print("")
    print("")
    key = input("")
    return key

def routine_100_map(x):
    return {
        'l' : 17,      # Use base codes for each state in FSM?
        'n' : '> Going North',
        's' : '> Going South',
        'e' : '> Going East',
        'w' : '> Going West',
        'i' : '> Checking inventory',
    } [x]

# Plain
def routine_101():
    cls()
    print("You are standing in a wide plain. Foothills")
    print("stretch to the north, where clouds gather")
    print("around an ominous peak. A dirt path winds")
    print("from a lonely chape to the east, through the")
    print("plains where you're standing, and south ")
    print("into a hustling town. Wispy mists gather")
    print("over marshland in the west, where a thin")
    print("tower stands alone in the bog.")
    print("")
    print("")
    print("> You examine your surroundings...")
    key = input("")
    cls()
    return key


