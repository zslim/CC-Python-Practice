# This is the file where you must work. Write code in the functions, create new functions,
# so they work according to the specification


# Displays the inventory.
def display_inventory(inventory):
    total = 0
    print("Inventory:")
    for k in inventory:
        print("{0} {1}".format(inventory[k], k))
        total += inventory[k]
    print("Total number of items: {}".format(total))


# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    for item in added_items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1


def order_dict(dictionary, direction=None):

    list_of_items = [list(elem) for elem in dictionary.items()]
    # this was not necessary bc sort can handle tuples too

    if direction == "count,asc":
        list_of_items.sort(key=lambda x: x[1])
    elif direction == "count,desc":
        list_of_items.sort(key=lambda x: x[1], reverse=True)

    return list_of_items


# Takes your inventory and displays it in a well-organized table with
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory)
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inventory, order=None):

    inv_items = order_dict(inventory, order)
    vals = [v for k, v in inv_items]
    keys = [k for k, v in inv_items]

    width_1 = max(len("count"), len(str(max(vals)))) + 2
    width_2 = len(max(keys + ["item name"], key=len)) + 2
    width_all = width_1 + width_2 + 2

    print("Inventory:")
    print("{head1:>{wth1}s}  {head2:>{wth2}s}".format(head1 = "count", wth1 = width_1, head2 = "item name", wth2 = width_2)) # naming args of format
    print("-" * width_all)

    for i in range(len(inv_items)):
        print("{:>{}d}  {:>{}s}".format(inv_items[i][1], width_1, inv_items[i][0], width_2))

    print("-" * width_all)
    print("Total number of items: {}".format(sum(vals)))


# Imports new inventory items from a file
# The filename comes as an argument, but by default it's
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename="import_inventory.csv"):
    with open(filename) as imported:
        items_str = imported.read()
        items = items_str.split(",")
    add_to_inventory(inventory, items)


# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text
# with comma separated values (CSV).
def export_inventory(inventory, filename="export_inventory.csv"):
    inv_csv = []
    for k, v in inventory.items():
        inv_csv = inv_csv + [k] * v
    inv_csv = ",".join(inv_csv)
    with open(filename, "w+") as exported:
        exported.write(inv_csv)

inv = {"rózsaszín csatabalta": 1, "pikkelyes kesztyű": 3}

add_to_inventory(inv, ["árvíztűrő tükörfúrógép", "árvíztűrő tükörfúrógép"])

import_inventory(inv, "progbasics-python-game-inventory-zslim/import_inventory.csv")

print_table(inv, "count,desc")