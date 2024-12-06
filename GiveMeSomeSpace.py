def sum(n):
    return n * (n + 1) / 2
print(sum(5))

def arraysum(a):
    sum = 0
    for i in a:
        sum = sum + i
    return (sum)

a = [12, 35, 9, 10]
print(arraysum(a))

def summ(n):
    if (n <= 0):
        return 
    return n + sum(n - 1)

print(summ(5))