# Given two integers a and b, which can be positive or negative,
# find the sum of all the numbers between including them too and return it.
# If the two numbers are equal return a or b.

# Note: a and b are not ordered!


def get_sum(a, b):
    # good luck!
    i = 0

    if a == b:
        return a

    if a > b:
        temp = a
        a = b
        b = temp

    for x in range(a, b+1):
        i += x

    return i


print(get_sum(-1, 2))
