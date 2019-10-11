## Python2
```python

# 계승 구하기
# 입력
n = 3

# 계산
factorial = 1
for i in range(1,n+1):
    factorial *= i

# 출력
print(factorial)

# 성적 총합 & 평균 구하기
my_scores = [30, 90, 80, 40, 50]

# 성적 총합 구하기
total_score = 0
for i in range(0,4):
    total_score += my_scores[i]
print(total_score)

# 평균 구하기
total_score = 0
for i in range(0,4):
    total_score += my_scores[i]

average_score = 0
average_score = total_score / len(my_scores)
print(average_score)



# 추상화
# n = 1
# factorial = 1
# for i in range(1, n+1):
#      factorial *= x
# print(factorial)

# result = factorial(1)

# print(result)
# print(factorial(1))
# print(factorial(2))
# print(factorial(3))
# print(factorial(4))
# print(factorial(5))


n = 1
factorial = 1
# for * in range(1, n+1):
#    factorial *= x
#   print(factorial)

n = 1
# accumulator = 1
# for * in range(1, n+1):
#    accumulator *= x
# print(accumulator)


# def factorial(n):
#    accumulator = 1
#   for * in range(1, n+1):
#        accumulator *= x
#    return accumulator
# print(factorial(1))


# def factorial(n):
#    accumulator = 1
#    for * in range(1, n+1)
#        accumulator *= x
#    return accumulator
# print(factorial(1))


def double(n):
    return n * 2


print(double(1))
print(double(2))

# 함수(Function)
# 몸으로 외우기

# 연습문제
scores = [80, 100, 70, 90, 40]

#1. Total 함수 만들기


def total(scores):
    return 0


print(total([80]))


def total(scores):
    return 80


print(total([80]))


def total(scores):
     total_score = 80
     return total_score


print(total([80]))


def total(scores):
    total_score = 0
    total_score += scores[0]
    return total_score


print(total([80]))


def total(scores):
    total_score = 0
    total_score += scores[0]
    total_score += scores[1]
    return total_score


print(total([80, 10]))


def total(scores):
    total_score = 0
    for i in [0,1]:
        total_score += scores[i]
    return total_score

print(total([80,10]))

scores = [80, 100, 70, 90, 40]


def total(scores):
    total_score = 0
    for i in range(len(scores)):
        total_score += scores[i]
    return total_score


print(total([80, 100, 70, 90, 40]))
print(total(scores))


# 2.average 함수 만들기

scores = [80, 100, 70, 90, 40]

def average(scores):
    average_score = 0

    for i in range(0, 4):
        average_score += scores[i] / len(scores)
    return average_score


print(average(scores))


# 성적 총점, 평균 구하기 2

class_scores = [
    [30, 90, 80, 40, 50],
    [100, 100, 100, 100, 100],
    [90, 90, 30, 30, 20]
    ]


def class_total(class_scores):
    total_score = 0
    for i in range(len(class_scores)):
        total_score += total(class_scores[i])
    return total_score


print('총점:', class_total(class_scores))


def class_average(scores):
    total_length = 0
    for i in range(len(class_scores)):
        total_length += len(class_scores[i])
    return class_total(scores) / total_length


print('평균:', class_average(class_scores))

# 누산
# 모두 더하기

# 입력
#numbers = [1, 3, 5, 7, 9]

# 초기값
#accumulator = 0

# 누산
# for i in range(0,len(numbers)):
#    accumulator += numbers[i]

# 출력
# print(accumulator)

# 모두 더하기 2

# 입력
#numbers = [1, 3, 5, 7, 9]

# 초기값
#accumulator = 0

# 누산
# for number in numbers:
#    accumulator += number

# 출력
# print(accumulator)

# 모두 곱하기
# 입력
# numbers = [1, 3, 5, 7, 9]

# 초기값
# accumulator = 1

# 누산
# for i in range(0,len(numbers)):
#    accumulator *= numbers

# 출력
# print(accumulator)

# 모두 곱하기2

# 입력
# numbers = [1, 3, 5, 7, 9]

# 초기값
# accumulator = 1

# 누산
# for number in numbers:
#   accumulator *= number

# 출력
# print(accumulator)



# 함수

# 2배
# def(double)(n):
#    return n * 2
# print(double(1))
# print(double(2))

# 더하기
def add(x,y):
    return x + y
print(add(1,3))

# 계승
def factorial(n):
    accumulator = 1
    for i in range(1, n+1):
        accumulator *=i
        return accumulator

for i in range(1, 10+1):
    print(factorial(i))







