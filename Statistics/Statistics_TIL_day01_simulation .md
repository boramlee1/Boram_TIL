### Statistics day01_simulation

- 확률
- 통계학의 필요성 : 불확실한 상황에서 의사결정 , 불확실성을 없애기 줄이기 위해 통계학이 필요 
- 변수의 종류 : 연속형 vs 범주형(이산형)
- 관찰 vs 잠재 
- 시뮬레이션 : 확률 -> 데이터
- 추정 : 확률 <-데이터 

1. 대표값 : 최빈값, 평균, 중간값

- import numpy
- numpy.mean(x)     # 평균
- x = [100, 100, 100, 120, 200, 300, 300, 400, 500, 500, 600, 610, 700, 800, 900]
- numpy.median(x)   # 중간값, 미들
- mod(x)            # 최빈값
- from scipy.stats import mode

2. 산포도(범위, 분산, 표준편차, 사분위수)

- numpy.min(x)      # 최소값
- numpy.max(x)      # 최대값
- numpy.var(x)      # 분산
- numpy.std(x)      # 표준편차
- numpy.quantile(x, .25) # 1사분위수(25% 지점)
- numpy.quantile(x, .5)
- numpy.quantile(x, .75) # 3사분위수(75% 지점)

- x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 100]

**[이산 확률 분포] : 이항분포, 다항분포, 초기하 분포, 기하 분포, 음이항 분포, 포아송 분포**

- 확률 분포 : 각각의 경우의 비율이 어떻게 되는가?
- 간단한 형태의 확률 분포 수식으로 만들 수도 있음
- 이런 수식에서는 모수(parameter)라는 한 두가지 수치로 분포가 결정 
- 그렇지 않은 분포들도 존재 

3. 이항 분포(binomial distribution)

- 2가지 경우만 존재(동전의 앞뒷면) P, 1-P
- n번 했을 때 몇 번 나오는가? 
- from numpy.random import binomial
- help(binomial)
- x = binomial(100, .3. 30)   # 고객의 구매율이 30%라고 했을 때 100명 방문, 30일 시뮬레이션 # 몇 명이 구매? 30명 온다고 30인분 준비하면 안됨
- 몬테카를로 시뮬레이션. agent based modeling : 각각의 행동은 알지만 전체를 모아놨을 때 어떻게 행동할지 모르겠다. 

- min(x)    # 16
- max(x)    # 42
- x
- 수익 = 0
  준비 = 20
  for 고객수 in x:
      if 고객수 <= 준비:
            수익 = 수익 + (준비-고객수) * -10000  (#1만원 손해 본다고 가정)
            수익 = 수익 + 고객수 * 1000
      else :
         수익 = 수익 + 준비 * 1000 
 수익                         

 - 보험료 = 300
   지급액 = 1000
   고객 = 지급액 /10
   장사 = 100
   사망자 = binomial(고객, .1, 장사)    # 고객 10%로 사망할 것이다
   매출 = 보험료 * 고객
   지급 = 지급액 * 사망자
   매출 - 지급
   numpy.mean(매출-지급)

-  binomial(100, .3)     # 100명 중에 30%

- 초기하 분포(hypergeometric distribution)
- 흰 공이 ngood개, 검은 공이 nbad개 있는 항아리에서
- 공을 nsample개를 뽑으면, 흰 공이 몇 개 나오는가?
- 예) 버스에 남자가 20명, 여자가 10명이 타고 있다. 이 중 9명을 무작위로 골랐을 때 남녀는 각각 몇 명일까?
   
4. 기하 분포(geometric distribution) : 성공률이 P%일 때, 성공할 때까지의 총 시도 횟수

- 이탈률이 5%인 고객이 가입해서 이탈 할때까지의 기간 
- binomial(1, .05) # 고객이 이탈할 확률 5%

- 이탈 성공 = 0
  기간 = 0
  while 이탈성공 == 0:
        이탈성공 =  binomial(1. .05)
        기간 = 기간 + 1
  기간 

- from numpy.random import geometric

- 기간 : geometric(.05, 100) # 이탈률 5%일 때 100명의 고객이 며칠 후 이탈하는가? 

5. 음이항 분포(Negative binomial distribution)

- 기하 분포의 일반화
- 성공률이 p일 때 n번 성공할 때까지 시도했을 때 총 시도 횟수
- 앞면이 나올 때까지 3번, 10번 계속 던짐 

- negative_binomial(1, .05, 100)
- numpy.sum(기간 * 0.5 -10)
- numpy.sum(기간 * 1 -100)
- numpy.sum(기간 * 0.5 - 10)

    짜증 = 0 
    기간 = 0 
    while 짜증 < 3:              # 3번째 이하는 참는다
        사건 = binomial(1, .05)  # 5% 확률로 사건 발생
        if 사건 == 1:            # 사건이 나면
            짜증 = 짜증 + 1       # 짜증이 증가
        기간 = 기간 + 1
    기간 

- 강아지 100마리 일 경우
    폭발 = []
    for i in range(100):
        짜증 = 0
        기간 = 0
        while 짜증 < 3:             # 3번째는 못참는다
            사건 = binomial(1, .05) # 5%의 확률로 사건 발생
            if 사건 == 1:           # 사건이 나면
                짜증 = 짜증 + 1      # 짜증이 증가
        기간 = 기간 + 1
        폭발.append(기간)

- from numpy.random import negative_binomial
- negative_binomial(3, .05, 100)   # 100마리 리트리버, 5% 확률로 짜증, 3번 나면 폭발 

- 실습 
- 우리 리트리버는 10%의 확률로 짜증이 납니다. 이틀 연속으로 짜증이 나면 화를 냅니다. 리트리버가 화를 낼 때까지 기간을 시뮬레이션 해보세요.


6. poisson 분포 

- 평균적으로 L번 일어나는 일어나는 일이 X번 일어날 확률의 분포
- 이항 분포에서 n이 크고 p가 작으면 포아송 분포와 비슷해짐
- 예) 1시간에 평균 10명의 고객이 방문한다고 할 때 시간 당 방문 고객 수 
- from numpy.random import poisson
- binomial(100, .3, 50)   # 100명의 고객이 30%로 50일간 방문
- poisson(30,50)     # 하루 평균 30명이 방문할 때 50일간 방문 일수


**[연속 확률 분포]**

- 균등 분포, 정규 분포, 지수 분포

7. 균등 분포

- 

- from numpy.random import uniform
- uniform(10,20) # 최소값 10에서 최대값 20까지 사이에서 균등하게
- uniform(1,10)  # 최소값 1에서 최대값 10까지 사이에서 균등하게 
- x = uniform(-1,1,1000)
- y = uniform(-1,1,1000) 
- numpy.mean(numpy.abs(x) + numpy.abs(y) < 1)

- x = uniform(-1, 1, 10000)
- y = uniform(-1, 1, 10000)
- numpy.mean(x ** 2 + y ** 2 <1) * 4  

8. 정규분포(가장 많이 쓰임)

- 평균 m, 분산 s
2을 모수로 하는 연속 확률 분포
- 이항 분포에서 n이 커지면 정규 분포와 비슷해진다

- from numpy.random import normal
- 기간 = geometric(.05, 100)
- 하루매출 = normal(50,20,100) # 고객 100명 평균 50만원, 표준편차 20만원 
- 기간 * 하루매출

9. 두 개의 정규분포가 섞여 있을 때 

- 유저집단 = binomial(1, .1, 100) #헤비 유저 10%
- 총매출 =[]
  for 유저 in 유저집단:
      if 유저 == 0:    #라이트 유저
         매출 = normal(30,10)
      else: #헤비 유저
            매출 = normal(100,10)
      총매출.append(매출)
총매출

- numpy.mean(normal(10, 2, 100))
- 총매출

10. 다항분포(multinomial distribution)

- 여러가지 경우가 존재
- 각각의 확률이 p(단 합은,1)
- n번 했을 때 각 경우가 몇 번 나오는가?
- 한국, 중국, 일본 고객들이 각각 50%, 30%, 20%일 때, 100명의 고객이 방문 하면 국가별 고객 수는 몇 명씩일까?

- from numpy.random import multinomial 
- multinomial(10,[.5,.2,.2,.1])
- multinomial(10, [.3, .7])
- binomial(10,.3)  # 주사위 10개 던졌을 때 30% 앞면
- 한국, 중국, 일본, 고객들이 각각 50%, 30%, 20% 일때, 100명의 고객이 방문
- multinomial(100,[.5,.3,.2])
- multinomial(100,[.5,.3,.2],30) # 동전 100개 던지는 것을 30번 함
- 평균으로의 회귀 : 어차피 확률이 50% 내외로 나옴

11. 지수분포(도착) : 정해진 시간 동안 몇 번 일어났는지, 다음 고객이 도착할 때까지 얼마나 걸리는지

- 평균적으로 B시간마다 일어나는 일이 다음에 일어날 때까지 시간
- 시간당 평균 L번 일어나는 사건의 포아송 분포는 B = 1/L 시간마다 일어나는 지수 분포

- from numpy.random import exponential
- exponential(30)  
- 카페 고객 도착하는 시간, 몇 명의 고객을 놓칠지 시뮬레이션 

- 리드타임 = 10
  exponential(30,100) < 리드타임 

- 알바 = 10
  리드타임 = 10 / 알바
  numpy.mean(exponential(30,100) < 리드타임)  #리드타임 이내 도착 고객 비율 

* 분포 추측하기 

12. 몬테카를로 법 Monte Carlo method
- 확률 분포에 따라 각각의 경우 추출한다
- 각 경우의 결과를 계산한다
- 경우별 결과를 더하거나 평균낸다

- 몬테카를로 법을 이용한 비용 편익 분석 
- 광고 비용: 1억원
- 광고가 전달되는 고객 수
- 고객의 구매율
- 고객의 구매액