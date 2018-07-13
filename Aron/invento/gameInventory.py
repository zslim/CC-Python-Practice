def display_inventory(inventory):
    for i in inventory:
        print(inventory[i], i)


def add_to_inventory(inventory, added_items):
    keys = list(inventory.keys())
    
    for i in added_items:
        for j in keys:
            if i == j:
                inventory[j] = inventory[j]+1
        if i not in inventory:
            inventory[i] = 1
    print(added_items)


def print_table(inventory, order=None):
    width_count = len(max(inventory.keys()))
    width_name = 
    if order is None:
        print("\nInventory: ")
        print("---------------------")
        print('count \titem name')
        for i in inventory:
            print('{} \t{}'.format(inventory[i], i.rjust(9)))
        print("---------------------")

    if order == "count,asc":
        print("\nInventory: ")
        print("---------------------")
        print('count \titem name')
        for i in sorted(inventory, key=inventory.get):
            print('{} \t{}'.format(inventory[i], i.rjust(9)))
        print("---------------------")

    if order == "count,desc":
        print("\nInventory: ")
        print("---------------------")
        print('count \titem name')
        for i in reversed(sorted(inventory, key=inventory.get)):
            print('{} \t{}'.format(inventory[i], i.rjust(9)))
        print("---------------------")


def export_inventory(inventory, filename="export_inventory.csv"):
    import csv
    with open(filename, 'w') as f:
        wr = csv.writer(f)
        wr.writerow(list(inventory.keys()))


def import_inventory(inventory, filename="import_inventory.csv"):
    import csv
    i_items = []
    with open(filename, 'r') as f:
        rr = csv.reader(f)
        listl = list(rr)
        i_items = listl[0]
    add_to_inv(inventory, i_items)
    print_table(inventory, "count,asc")


inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

