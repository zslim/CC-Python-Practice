numbers = [-5, 23, 0, -9, 12, 99, 105, -43]


def minimum(num_list):
    lenght = len(num_list)
    j = 0
    while j < lenght-1:
        if num_list[j] < num_list[j+1]:
            temp_min = num_list[j]
            num_list[j+1] = temp_min
            j = j + 1
        else:
            j = j + 1

    if temp_min < num_list[-1]:
            print(temp_min)
    else:
        print(num_list[-1])


def maximum(num_list):
    lenght = len(num_list)
    j = 0
    while j < lenght-1:
        if num_list[j] > num_list[j+1]:
            temp_min = num_list[j]
            num_list[j+1] = temp_min
            j = j + 1
        else:
            j = j + 1

    if temp_min > num_list[-1]:
            print(temp_min)
    else:
        print(num_list[-1])


def avarage(num_list):
    lenght = len(num_list)
    j = 0
    sum = 0
    while j < lenght:
        sum = sum + num_list[j]
        j = j + 1
    print(sum/lenght)

minimum(numbers)
maximum(numbers)
avarage(numbers)