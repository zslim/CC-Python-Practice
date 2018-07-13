#numbers = [-5, 23, 0, -9, 12, 99, 105, -43]
numbers = [-5, 23, 0, "dupa", -9, 12, 99, [2, 44], None, 105, -43]
print(numbers.index(23))


def sumOfNum(numbers):
    i = 0
    for number in numbers:
        if type(number) == int:
            i += number
        elif type(number) == list:
            i += sumOfNum(number)
    return i


print(sumOfNum(numbers))


def avgOfNum(numbers):
    i = 0
    for number in numbers:
        i += number
        average = i/(len(numbers))
    print(average)


#avgOfNum(numbers)


def minOfNum(numbers):
    mini = numbers[0]
    for number in numbers:
        if mini > number:
            mini = number
    print(mini)


#minOfNum(numbers)


def maxOfNum(numbers):
    maxi = numbers[0]
    for number in numbers:
        if maxi < number:
            maxi = number
    print(maxi)


#maxOfNum(numbers)
