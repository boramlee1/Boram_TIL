### Python_1 

```python

# TDD(Test Driven Development)
# Red - Green - Refactoring
# f(x,y)
# Factorial
# f(1) 1
# f(2) 2
# f(3) 6
# f(4) 24
# F(5) 120

# 변수

name = 'Anne'
score = 100
print(name,score)

# 여러 변수

score1 = 80
score2 = 90
score3 = 70
print(name, score1, score2, score3)

# 리스트

scores = [80, 90, 70]
print(name, scores[0], scores[1], scores[2])

# 모두 더하기

total_score = scores[0] + scores[1] + scores[2]
print(total_score)

# 다시 할당

total_score = 0
print(total_score)

# 우아하게 모두 더하기(새로운 함수)

total_score = sum(scores)
print(total_score)

# 리스트에 있는 점수  개수 구하기(length)
subjects_count = len(scores)
print(subjects_count)

# 평균 점수 구하기
average_score = sum(scores)/len(scores)
print(average_score)

# 최소, 최대 점수 구하기
min_score = min(scores)
max_score = max(scores)
print(min_score, max_score)

# 리스트 일부 얻기

scores = [10, 20, 30, 40, 50, 60]
some_scores = scores[2:4]
print(some_scores)

some_scores = scores[:4]
print(some_scores)

some_scores = scores[2:]
print(some_scores)

some_scores = scores[:]
print(some_scores)

# 거꾸로 값 얻기

some_scores = scores[::-1]    # 전체를 역순으로 출력해라
print(some_scores)

some_scores = scores[2:4:-1]  #2번째에서 4번째로 역순 갈수 없음
print(some_scores)

some_scores = scores[4:2:-1]  #4번째에서 뒤로 2번째에 해당되는 숫자
print(some_scores)



# <Python 1.1>

# 누산(Accumulation)
# age = 13
# age = 14
# age = 13+1
# age = age +1
# new_age = age +1
# age = new_age
# age = age + 1
# age += 1
# age -= 1
# age *= 2
# age /= 2
# age //= 2    # 몫
# age %= 2     # 나머지

# factorial = 1 * 2 * ... * n
# factorial = 1
# factorial  *2 = 2
# factorial *= n
# 초기값 factorial = 1
# 누산 : x는 1부터 n까지
# factorial *= x
# factorial = 1
# for in range(1, n+1):
#    factorial *= x

# factorial = 1
# for x in[1,2,3]:
#   factorial *= x

# For-loop 로 반복 = 누산

# 초기값 지정
# 코드를 반복 입력 = 누산
# 계산 결과 출력 및 확인


# 연습문제
# total score 구하기

scores = [80, 100, 70, 90, 40]

total_score = 0
total_score += scores[0] + scores[1] + scores[2] + scores[3] + scores[4]
print(total_score)

# total score 개수 구하기

total_score = 0
total_score += len(scores)
print(total_score)

# 누산으로 풀어보기

total_score = 0
total_score += scores[0]
total_score += scores[1]
total_score += scores[2]

scores = [80, 100, 70, 90, 40]

total_score = 0
for i in [0 , 1, 2, 3, 4]:
    total_score += scores[i]
print(total_score)

for i in range(0,4):
    total_score += scores[i]
print(total_score)


                