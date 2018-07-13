#every def func() is a new kata

def is_sorted_and_how(arr):
    if arr == sorted(arr):
        return "yes, ascending"
    elif arr == (sorted(arr))[::-1]:
        return "yes, descending"
    else:
        return "no"

def diamond(n):
    if n > 0 and n % 2 == 1:
        diamond = ""
        for i in range(n):
            diamond += " " * abs((n/2) - i)
            diamond += "*" * (n - abs((n-1) - 2 * i))
            diamond += "\n"
        return diamond
    else:
        return None

def sort_by_length(arr):
    return sorted(arr,key = len)

def get_middle(s):
    if len(s) % 2==0:        
        return s[(len(s)/2)-1]+s[len(s)/2]
    else:
        return s[((len(s)+1)/2)-1]

import math

def is_square(n):
    try:
        num = math.sqrt(n)
        if num == int(num):
            return True
        else:
            return False        
    except ValueError:
        return False

def high_and_low(numbers):
    numi = numbers.replace(" ",",")
    numero = numi.split(",")
    numio = list(map(int,numero))
    x = max(numio)
    y = min(numio)
    d = str(x),str(y)
    final = " ".join(d)    
    return final

def min_max(lst):
    x = min(lst)
    y = max(lst)
    d = [x, y]
    
    return d

def calculate_years(money, i, t, des_sum):   
    
    if money == des_sum:
        return 0
    y = 0
    temp_money = money
    while temp_money < des_sum:
        interest = temp_money*i
        taxed = interest - (interest*t)
        temp_money = temp_money+taxed      
        y += 1
        continue        
        
    return y

def digitize(n): 
    t = map(int,reversed(str(n)))    
    return t

def get_sum(a,b):
    if a ==b:
        return a
    if b < a:
        x=list(range(b,a+1))
        return sum(x)
    else:
        x=list(range(a,b+1))
        return sum(x)

def no_space(x):
    y = x.replace(" ","")
    return y

