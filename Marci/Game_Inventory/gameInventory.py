# This is the file where you must work. Write code in the functions, create new functions, 
# so they work according to the specification

# Displays the inventory.
def display_inventory(inventory):
    #inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    total = 0
    print("Inventory:")
    for i in inventory:
        print("{:>3}    {:>20}".format(inventory[i], i))
        total += inventory[i]
    print("Total number of items: {}".format(total))


# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    #dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    for item in added_items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1


def width_calculator(inventory):
    width = 0
    lenght = ""
    for item in inventory:
        if len(lenght) < len(item):
            width = len(item)
            lenght = item
    return width

def inventory_printer(inventory, quantities, width):
    counter = 0
    items = inventory.keys()
    for i in inventory:
        left = quantities[counter]
        right = inventory.get(i)
        width -= len(str(left))
        print("{}{}".format(left, right.rjust(width+5)))
        width += len(str(left))
        counter += 1


def order_inventory(inventory, order, width):
    width = width
    quantities = inventory.values()
    if order == "count,desc":
        quantities = (sorted(quantities, reverse=True))
        inventory_printer(inventory, quantities, width)
    if order == "count,asc":
        quantities = sorted(quantities)
        inventory_printer(inventory,quantities,width)
    
  #  quantity_list = []
  #  for quantity, item in enumerate(inventory):
  #      quantity_list.append(item)
  #  sorted(quantity_list)
  #  print(quantity_list)



# Takes your inventory and displays it in a well-organized table with 
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory) 
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inventory, order=None):
    print("Inventory:")
    widht = width_calculator(inventory)
    if order == None:
        for i in inventory:
            print("{:>3}    {:>10}".format(inventory[i], i))
            total += inventory[i]
        print("Total number of items: {}".format(total))
    else:
        quantities = order_inventory(inventory, order, widht)




# Imports new inventory items from a file
# The filename comes as an argument, but by default it's 
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename="import_inventory.csv"):
    with open(filename) as imported:
        items = imported.read()
        items = items.split(",")
    add_to_inventory(inventory, items)




# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text 
# with comma separated values (CSV).
def export_inventory(inventory, filename="export_inventory.csv"):
    pass


inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
added_items = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
add_to_inventory(inventory, added_items)
#display_inventory(inventory)
print_table(inventory, "count,asc") #input order parameter