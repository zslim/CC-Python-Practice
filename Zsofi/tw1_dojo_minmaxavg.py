# 1st TW week in Python
# Dojo 1.
# 13.06.2018.

vect = [-5, 23, 0, -9, 12, 99, 105, -43]

def dmax(l):
    m = l[1]
    i = 0
    for i in range(len(l)):
        if m < l[i]:
            m = l[i]
    
    return m

def dmin(l):
    m = l[1]
    i = 0
    for i in range(len(l)):
        if m > l[i]:
            m = l[i]
    
    return m

def davg(l):
    s = 0
    for i in range(len(l)):
        s = s + l[i]
    
    return s / len(l)

print("Max of list: ", dmax(vect))
print("Min of list: ", dmin(vect))
print("Avg of list: ", davg(vect))