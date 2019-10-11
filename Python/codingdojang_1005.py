# python 코딩도장_1005

# 재귀호출

def hello(count):
    if count == 0:  # 종료 조건을 만듬. count가 0이면 다시 hello 함수를 호출하지 않고 끝냄
        return

    print('Hello, world!', count)

    count -= 1  # count를 1 감소시킨 뒤
    hello(count)  # 다시 hello에 넣음

hello(10)

# 재귀호출로 회문 판별하기

def is_palindrome(word):
    if len(word) < 2:
        return True

    if word[0] != word[-1]:
        return False
    return is_palindrome(word[1:-1])


print(is_palindrome('hello'))
print(is_palindrome('level'))

# fibonacci

def fibonacci(n):
    a, b = 1, 0
    for i in range(n):
        a, b = b, a + b
    return b

print(fibonacci)

# lambda(식 형태로 되어 있다)

def plus_ten(x):
    return x+10
print(plus_ten(1))

lambda x:x+10 

plus_ten = lambda x: x+10
print(plus_ten(1))

(lambda x: x+10)(1)

y=10
(lambda x : x+y)(1)

def plus_ten(x):
    return x+10

list(map(plus_ten, [1,2,3]))

print(list(map(plus_ten, [1,2,3])))

list(map(lambda x: x+10,[1,2,3]))
print(list(map(lambda x: x+10,[1,2,3])))

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
z= list(map(lambda x: str(x) if x % 3 ==0 else x,a))
print(z)

b = list(map(lambda x:str(x) if x == 1 else float(x) if x ==2 else x+10, a ))
print(b)

def f(x):
    if x == 1:
        return str(x)
    elif x ==2:
        return float(x)
    else:
        return x+10
x = list(map(f,a))     # f 함수 내용을 a 모든 값에 적용한다.
print(x)

# map에 객체를 여러개 넣기

d =[1,2,3,4,5]
e= [2,4,6,8,10]

g= list(map(lambda x,y: x *y, d,e))
print(g)

# filter(함수, 반복 가능한 객체)

def f(x):
    return x > 5 and x < 10

a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
j = list(filter(f,a))
print(j)

a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
k= list(filter(lambda x: x > 5 and x < 10,a))
print(k)

# reduce 반복가능한 객체의 각 요소를 지정된 함수로 처리한된 이전 결과와 누적해서 변환하는 함수

def f(x,y):
    return x+y

a = [1, 2, 3, 4, 5]
from functools import reduce
s= reduce(f,a)

print(s)

w= reduce(lambda x,y:x+y,a)
print(w)

# 참고 : 리스트(딕셔너리, 셋) 표현식으로 처리할 수 있는 경우(comprehension)

a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
u= [i for i in a if i > 5 and i <10]
print(u)




