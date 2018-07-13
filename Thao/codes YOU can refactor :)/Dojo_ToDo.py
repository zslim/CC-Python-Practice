# With your group, write an application in Python that keeps your to-dos in one place. It should support the following features:
# -listing tasks
# -adding a new task
# -marking a task as completed
# -archive (deleting all complete tasks)

list_todo = []  # list of lists -> item-ei: [store, False] -> item[0] = store, item[1] = False
#     1. [ ] Buy some milk
#     2. [ ] Learn Python
#     3. [ ] Learn Git


def printList():
    i = 1
    for item in list_todo:
        if item[1]:  # azaz False
            mark = "x"
        else:
            mark = " "
        print(str(i) + ". [" + mark + "] " + item[0])
        i += 1  # sorszámozás


# befejezetlen, majd fejezd be!!!
"""def printArchivedList():
    for item in list_todo:
        if item[1] == "x":
            list_todo.remove(item)"""


def toDo():
    command = input("Please specify a command [list, add, mark, archive]: ")
    if command == "x":
        quit()

    elif command == "add":
        store = input("Add an item: ")
        list_todo.append([store, False])  # list-tel append-del ([store, False])
        print("Item added.")

    elif command == "list":
        print("You saved the following to-do items: ")
        printList()

    elif command == "mark":
        print("You saved the following to-do items: ")
        printList()
        index = int(input("Which one you want to mark as completed: "))
        list_todo[index-1][1] = True  # list_todo-ban az index-1-ik item-ének az 1. eleme legyen True

    elif command == "archive":
        print("All completed tasks got deleted.")
        printArchivedList()
        #list_todo.remove([store, True])


while True:
    toDo()
