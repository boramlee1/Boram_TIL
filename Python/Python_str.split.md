# Python str .split

```python
1. split

- 하나의 문자열을 여러 문자열로 나눠줌, 나눈 결과는 문자열의 list가 됨
- 그냥 사용 하면 빈 칸을 기준으로 나눠줌 
- '아버지가 방에 들어가신다'.split()
- ['아버지가', '방에', '들어가신다']
- 쉼표 등 특정 문자열을 기준으로 나눌 수도 있음
-'빵, 우유, 달걀'.split(',')
- 나누는 횟수도 제한할 수 있음
- '1,2,3,4,5'.split(',',2)
- ['1', '2', '3,4,5']

2. 응용

- 나눈 결과를 합쳐주고 싶더면 str.join
- ','.join('아버지가 방에 들어가신다'.split())
- '아버지가, 방에, 들어가신다'
- 나눈 결과의 공백을 제거하고 싶다면 str.strip

3. 연습문제 

- assert shorten_to_date('Monday February 2, 8pm') == 'Monday February 2'
assert shorten_to_date('Tuesday May 29, 8pm') == 'Tuesday May 29'
assert shorten_to_date('Wed September 1, 3am') == 'Wed September 1'
assert shorten_to_date('Friday May 2, 9am') == 'Friday May 2'
assert shorten_to_date('Tuesday January 29, 10pm') == 'Tuesday January 29'

- def shorten_to_date(long_date):
    return long_date.split(',')[0]