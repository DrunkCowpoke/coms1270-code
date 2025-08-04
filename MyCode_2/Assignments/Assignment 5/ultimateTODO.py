# Trevor Bentley             7-26-2025
# Assignment 5: Ultimate to do list

# Assignment 5: uses a task tracker that lets users move taks across dictionaries



import sys
# Not asked for but sys.exit has been removed from loadList and saveList to improve user friendliness
# Technically theres no use for sys function but I dont want to Deviate too far

import pickle

def printTitleMaterial():
    print("The Ultimate TODO List!")
    print()
# ----- To Do list Req Header
    print("By: Trevor Bentley")
    print("[COM S 1270 1]")
    print()

# ----- Given Initilization ------
def initList():

    todoList = {}
    todoList["backlog"] = []
    todoList["todo"] = []
    todoList["in_progress"] = []
    todoList["in_review"] = []
    todoList["done"] = []

    return todoList

# ----- Checking contents -----
def checkIfListEmpty(todoList):

    if (len(todoList["backlog"]) > 0 or 
        len(todoList["todo"]) > 0 or
        len(todoList["in_progress"]) > 0 or
        len(todoList["in_review"]) > 0 or
        len(todoList["done"]) > 0):

        return False
    
    return True

# ----- Gotta be able to save -----
def saveList(todoList):

    try:
        listName = input("Enter List Name (Exclude .lst Extension): ")
        with open("./" + listName + ".lst", "wb") as pickle_file:
            pickle.dump(todoList, pickle_file)
    except:
        print("I dont know how to tell you this but...")
        print("(saveList): ./{0}.lst is not a valid file name!".format(listName))

        return None

# ----- List Access -----
def loadList():

    try:
        listName = input("Enter List Name (Exclude .lst Extension): ")
        with open("./" + listName + ".lst", "rb") as pickle_file:
            todoList = pickle.load(pickle_file)
    except:
        print(f"Buddy, you gotta make Lists first: ./{listName}.lst was not found!")
        return None
    
    return todoList

def checkItem(item, todoList):

    itemFound = False
    keyName = ""
    index = -1
    
# ---- For loop to find item and indexing for list -----
    for key in todoList:
        if item in todoList[key]:
            itemFound = True
            keyName = key
            index = todoList[key].index(item)
            break

    return itemFound, keyName, index

# ----- Ah i see heres the not found / add item -----
def addItem(item, toList, todoList):

# ----- Refrence to check item so i dont break everything -----
    itemFound, keyName, index = checkItem(item, todoList)

    if not itemFound:
        todoList[toList].append(item)
    else:
        print(f"hey '{item}' is already in '{keyName}' list at {index}.")

    return todoList

def deleteItem(item, todoList):

    itemFound, keyName, index = checkItem(item, todoList)

    if itemFound:
        del todoList[keyName][index]
        print("We won't be hearing form him again")
    else:
        print(f"So uh,'{item}', is not there to remove.")

    return itemFound, todoList

# ----- No idea why I'm using the del fxn -----
def moveItem(item, toList, todoList):

    itemFound, todoList = deleteItem(item, todoList)

    if itemFound:
        todoList = addItem(item, toList, todoList)
        print("Alright its been Re-Homed.")

    return todoList

def printTODOList(todoList):

    for key in todoList:
        print(f"{key}: {todoList[key]}")

    return None

def runApplication(todoList):

    while True:
        print("-----------------------------------------------------------------")
        choice = input("APPLICATION MENU: [a]dd to backlog, [m]ove item, [d]elete item, [s]ave list, or [q]uit to main menu?: ")
        print()

# ----- No idea what im doing here hopefully this puts it in the right list-----
        if choice == "a":
            item = input("Enter Your Task: ")
            todoList = addItem(item, "backlog", todoList)
            print()
            printTODOList(todoList)

# ----- Category Changer -----
        elif choice == "m":
            if not checkIfListEmpty(todoList):
                item = input("Enter a task to move: ")
                itemFound, _, _ = checkItem(item, todoList)

                while not itemFound:
                    print(f"So, '{item}', was not found in any list.")
                    item = input("Enter a task to move: ")
                    itemFound, _, _ = checkItem(item, todoList)

                toList = input(f"Enter the list to move '{item}' to: ")
                while toList not in todoList:
                    print(f"So, '{toList}', is not a valid list.")
                    toList = input(f"Enter the list to move '{item}' to: ")

                todoList = moveItem(item, toList, todoList)
            else:
                print("Nothing here to relocate.")

            print()
            printTODOList(todoList)

# ----- Deletion Seleection -----            
        elif choice == "d":
            if not checkIfListEmpty(todoList):
                item = input("Enter a task to delete: ")
                _, todoList = deleteItem(item, todoList)
            else:
                print("No tasks to delete!")

            print()
            printTODOList(todoList)

# ----- Saving -----
        elif choice == "s":
            saveList(todoList)
            print("Saving List...")
            print()
            printTODOList(todoList)

# ----- Quit to menu -----
        elif choice == "q":
            print("Returning to MAIN MENU...")
            print()
            break

# ----- Invalid Input -----
        else:
            print("ERROR: Please enter [a], [m], [d], [s], or [q].")
            print()

    return todoList

# ----- Main FXN -----
def main():

    taskOver = False

    printTitleMaterial()

    while taskOver == False:
        print("-----------------------------------------------------------------")
        choice = input("MAIN MENU: [n]ew list, [l]oad list, or [q]uit?: ")
        print()
        if choice == "n": 
            todoList = initList()

            printTODOList(todoList)
            
            runApplication(todoList)
        elif choice == "l":
            todoList = loadList()

            printTODOList(todoList)
            
            runApplication(todoList)
        elif choice == "q":
            taskOver = True
            print("Goodbye!")
            print()
        else:
            print("Please enter [n], [l], or [q]...")
            print()

if __name__ == "__main__":
    main()