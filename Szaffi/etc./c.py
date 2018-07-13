numbers = [1,2,56,32,51,2,8,92,15]

print(numbers)
iterations = 1
N = 9

while iterations < N:
    j=0
    while j<=N-2:
        while numbers[j]>numbers[j+1]:
            temp=numbers[j+1]
            numbers[j+1]=numbers[j]
            numbers[j]= temp            
        j=j+1
    iterations=iterations+1
print(numbers)
