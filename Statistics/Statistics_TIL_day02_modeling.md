### Statistics day02_modeling

### 분포의 시각화
- !pip install seaborn
- import seaborn

1. 이항 분포의 히스토그램 그리기

- from numpy.randaom import binomial
- x = binomial(10, .4) # 앞면이 .4인 동전 10개 던졌을 때 앞면 몇 개 나오는지?
- seaborn.distplot(x)

2. 실습

- 아래 각 분포로 데이터 만들어서 seaborn.distplot 그려보세요. 

- 이산 (기하분포, 음이항분포, 포아송분포)
- 연속 (균등분포, 정규분포, 지수분포)

- from numpy.random import binomial, geometric, negative_binomial
- x = geometric(1.0, 100)
- seaborn.distplot(x)

- x = negative_binomial(3, .4, 100)
- seaborn.distplot(x)

- from numpy.random import normal
- x = normal(10, 3)
- import numpy
- numpy.mean(x)
- numpy.std(x)
- seaborn.distplot(x)

3. 리트리버 분포

- retriver(10, .4, 100)
- 개판 = []
  for i in range(100):
    한계 = 10
    짜증확률 = .4

    옐로카드 = 0
    기간 = 0
    while 옐로카드 < 한계:
        짜증 =  binomial(1, 짜증확률)
        if 짜증 == 1:
            옐로카드 += 1
        else:
            옐로카드 = 0
        기간 += 1
    개판.append(기간)
seaborn.distplot(개판)

- 연기력 = normal(50, 15, 100) 평균 50, 표준편차 15인 배우 100명
- seaborn.distplot(연기력)

4. 연기의 영향이 매출의 평균에 영향을 미치는 모형

- 연기의영향 = 100 * 연기력 + 20000
- 매출 = normal(연기의영향, 800)
- seaborn.jointplot(연기력, 매출)

5. 연기의 영향이 매출의 표준편차에 영향을 미치는 모형

- 연기의영향 = 100 * 연기력
- 매출 = normal(20000, 연기의 영향)
- seaborn.jointplot(연기력, 매출)
