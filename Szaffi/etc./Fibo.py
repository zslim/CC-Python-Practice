i=0
j=1
k=0
fib=0

while i < 30:
    print(fib)
    fib = j + k
    j = k
    k = fib
    i = i + 1
else:
    print("Done!")
