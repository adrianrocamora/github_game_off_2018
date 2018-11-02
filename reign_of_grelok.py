import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

cls()
print("Reign of Grelok")

input('')

cls()
print("> (Plains) Look Around")
print("> Go North (up)")
print("> Go South (down)")
print("> Go East (right)")
print("> Go West (left)")
print("> Inventory (spacebar)")
input('')

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
# TODO: Make this spacing variable to fill the "screen"
print("")
print("> You examine your surroundings...")
input('')
