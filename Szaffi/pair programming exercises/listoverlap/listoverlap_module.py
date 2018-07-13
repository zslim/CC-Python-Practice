from random import randint, sample


def listoverlap(list1, list2):
    s1 = set(list1)
    s2 = set(list2)
    return list(s1 & s2)


def main():
    l1 = sample(range(100), randint(1, 20))
    l2 = sample(range(100), randint(1, 20))
    return listoverlap(l1, l2)


if __name__ == '__main__':
    main()
