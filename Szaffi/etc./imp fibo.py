Fibo = int(input("How many numbers do you need?"))

i=0
j=1
k=0
fib=0

while i < Fibo:
    if i%10 == 0:
        print(fib)
    fib = j + k
    j = k
    k = fib
    i = i + 1