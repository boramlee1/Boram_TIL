### Python_assert

```python 
# input
scores = [80, 100, 70, 90, 40]

# initial state

total_score = 0

# Computing

#for i in range(0, len(scores)):
#total_score += scores[i]

for score in scores:
    total_score += score
print(total_score)

average_score = total_score / len(scores)
print(average_score)

# Output

print('Total_score:', total_score)
print('Average_score:', average_score)
print('actual', total_score)

# Test

# total

def test_total():
    assert total([80]) == 80


def total():
    pass


def test_total():
    assert total([80]) == 80


def total(scores):
    pass


def test_total():
    assert total([80]) == 80


def total(scores):
    return 80


def test_total():
    assert total([80]) == 80


def total(scores):
    return scores[0]


def test_total():
    assert total([80]) == 80


# average

def test_average():
    assert average([80,100]) == 90


def average():
    pass


def test_average():
    assert average([80,100]) == 90


def average(scores):
    pass

def test_average():
    assert average([80,100]) == 90


def average(scores):
    return 90


def test_average(scores):
    return scores[0]


def test_average():
    assert average([80,100]) == 90



# 구구단 프로그램 테스트 코드.

def multiply(a,b):
    return a * b
assert 2 * 4 == 8
assert 8 * 9 == 72

def test_multiply():
    assert multiply(2, 4) == 8
    assert multiply(10, 9) == 90

    for i in range(2,10):
        for j in range(1,10):
            print(i * j)


