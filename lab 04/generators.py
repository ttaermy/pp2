#1
def sqs_n(N):
    num = 0
    while num <= N :
        yield num ** 2
        num += 1

for square in sqs_n(N):
    print(square)


#2
def even_n(n):
    num = 0
    while num <= n:
        if num % 2 == 0:
            yield num
        num += 1

n = int(input())
print(", ".join(map(str, even_n(n))))


#3
def dvs(n):
    num = 0
    my_iter = iter(range(n+1))
    for num in my_iter:
        if num % 3 == 0 or num % 4 == 0:
            yield num

n = int(input())
print(", ".join(map(str, dvs(n))))


#4
def squares(a, b):
    for num in range(a, b + 1):
        yield num ** 2

a, b = map(int, input(). split())
print(", ".join(map(str, squares(a, b))))


#5
def down(n):
    num = n
    while num >= 0:
        yield num
        num -= 1

n = int(input())
print(", ".join(map(str, down(n))))