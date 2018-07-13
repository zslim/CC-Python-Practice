def get_most_played(file_name):
    llist = []
    with open(file_name, 'r') as f:
        rows = f.readlines()
        for i in rows:
            row = i.split('\t')
            llist.append(float(row[1]))
        llist = max(llist)
        for j in rows:
            row = j.split('\t')
            if float(row[1]) == llist:
                return row[0]


def sum_sold(file_name):
    copies = 0
    with open(file_name, 'r') as f:
        rows = f.readlines()
        for i in rows:
            row = i.split('\t')
            copies += float(row[1])
    return copies


def get_selling_avg(file_name):
    copies = 0
    count = 0
    with open(file_name, 'r') as f:
        rows = f.readlines()
        for i in rows:
            row = i.split('\t')
            copies += float(row[1])
            count += 1
    return copies / count


def get_date_avg(file_name):
    years = 0
    count = 0
    with open(file_name, 'r') as f:
        rows = f.readlines()
        for i in rows:
            row = i.split('\t')
            years += int(row[2])
            count += 1
    return int(years / count) + (years % count > 0)


def get_game(file_name, title):
    llist = []
    with open(file_name, 'r') as f:
        rows = f.readlines()
        for i in rows:
            row = i.split('\t')
            if title == row[0]:
                llist.append(str(row[0]))
                llist.append(float(row[1]))
                llist.append(int(row[2]))
                llist.append(str(row[3]))
                llist.append(str(row[4].rstrip('\n')))
    return llist
