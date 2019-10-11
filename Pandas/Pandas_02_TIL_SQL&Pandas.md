# SQL & Pandas

1. 데이터 읽어오기

- import pandas as pd
- url = ('https://raw.github.com/pandas-dev/pandas/master/pandas/tests/data/tips.csv')
tips = pd.read_csv(url)

2. 데이터 미리보기 

- tips.head()
- tips.columns
- tips.describe() #median(중간값) - 아웃라이어가 있어도 변하지 않는 값

3. SELECT

- tips 
- tips[['total_bill','tip']].head(5)

- 팁, 얼마나 주는지 궁금해졌다.
tips['tip_percentage'] = tips['tip'] * 100 / tips['total_bill']
- tips['tip_percentage'].mean()

4. WHERE

- tips['smoker'].unique

- tips[tips['smoker'] == 'Yes'].head(3)   #흡연자만 출력

- Pandas로 여러 조건 중첩하여 필터링 # 여성이면서 흡연자 
tips[(tips['sex'] == 'Female') & (tips['smoker'] == 'Yes')]

- 팁을 안주고 간 사람
- tips[tips['tip'] == 0]

- 컬럼 time에는 어떤 값들이 있나요?
- tips['time'].unique()

5. GROUP BY

- 요일별로 팁을 주고 간 손님 수 계산
- tips.groupby('day').size()

- 여자 손님 몇 명, 남자 손님 몇 명
- tips.groupby('sex').size()

- tips.dtypes

- 여자 손님과 남자 손님 중 누가 팁을 전체 계산액에 비해 많이 줄까요? 
- tips.groupby('sex')['tip_percentage'].mean()

- 팁은 흡연자가 많이 줄까요? 비 흡연자가 많이 줄까요?

- tips.groupby('smoker')['tip_percentage'].mean()

- 팁은 보통 여성, 흡연자가 많이 주는 것처럼 보임. 두가지 요인을 같이 살펴보기

- tips.groupby(['sex', 'smoker'])['tip_percentage'].mean()
