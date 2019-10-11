### Statistics day12_Time Series
### 시계열  분석

- 생존 분석은 고객이 이탈 하느냐 마느냐, 시계열은 동일한 변수의 시간에 따른 변동을 나타낸 데이터
- 예시 : 고객수, 가격, 온도, 전체 트렌드를 봄
- 미래를 예측하기 위함인데 패턴이 있어야 예측하기 쉬움
- 생존 분석 - 각각의 고객이 언제 빠져 나가느냐

### 자기상관

- 자기 상관 :  이전의 값과 이후의 값 사이에 상관이 존재, ** 이번 주 상품 판매량과 다음 주 상품 판매량**
- 자기상관과 마이너스이다 : 그 주에 많아 팔리면, 그 다음 주에는 적게 팔리는 형태 한쪽이 마이너스면 다른 쪽이 플러스, 평균선을 기준으로 오르락 내리락
- **상품 판매는 자기상관 마이너스임**
- 화학 공정의 품질 - 한번 올라가면 잘 안 내려가고, 한번 내려가면 잘 안 올라감. **품질 같은 경우는 자기상관 플러스, 한번 안 내려가게 조심해야 함**
- 자기 상관 플러스인지 마이너스인지 중요함

### 추세

- **장기적으로 올라가느냐 내려가느냐**
- 추세 : 연간 치즈 생산량
- 추세는 관심이 높음, 주식 시장에서도 추세로 돈을 먹는 사람이 있고, 자기 상관으로 돈을 버는 사람이 있음
- 추세 : 워렌버핏의 경우, 자기상관으로 돈을 버는 경우 - 이 주식은 내려가면 반드시 올라가고, 올라가면 반드시 내려가는 경우가 있으니 자기 상관으로 돈을 버는 것임, 추세적으로 장기적으로 돈을 벌면 돈을 못 범. 주가가 많이 움직이면 돈을 못범, 예상이 어려움

### 계절성

- 월별 음료 출고량, 자기 상관이 플러스인데 12개월 단위로 플러스임. 긴 기간에 걸친 자기 상관 이다.
- 전년 대비 많이 팔리면 많이 팔리는 상품이 있다.
- 한달 주기로 계절성이 있다. 월 소비 패턴이 계절성이 있음.

### 비정상(주가)

- non stationary(정상, 정체되어 있다고 번역을 함)
- **데이터 패턴이 계속 변한다. 비정상이라고 함**
- 분석이 어려움. 어제 오늘 패턴이 달라서
- 주식으로 돈을 많이 벌기 시작하면 내가 사고 파는데 영향을 줌, 누가 돈을 버는 줄 알고 개입해서 패턴이 변하기 시작함. 우리한테는 전략을 실행해줄 돈이 없음. 누구보다 0.1초 빨리 사면 돈을 벌 수 있음
- 분석해도 패턴이 변함. 데이터 분석으로 돈 벌기 어려움
- 엄밀한 정상은 패턴이 정말 고정적인 형태임

### 이상점 : outlier

- 이상한 점 , **한 개 정도가 튀는 것이지 원래 트랜드대로 움직이는 형태임**
- 트렌드로 볼 것이냐, 어느 한 정도 튀는 것으로 볼 것인지 확인
- 공장 화재로 생산량 갑자기 감소하는 경우 

- **데이터 분석할 때 이 트렌드는 변하지 않을 것이다라는 정상성을 가정하고 분석함**
- 발주 넣을 때 추세를 반영해서 물건을 주문함. 매출을 움직이는 많은 요소를 반영함
- 갑자기 물건 패턴이 뛰는 경우는 그 상품 프로모션 들어갔거나, 텔레비전 프로그램에 나온 경우(이상 패턴을 보이고) 아웃라이어를 반영함. 어떤 상품을 정해서 그 상품을 밀 것인지를 생각하고 발주량을 늘려서 매출을 높임 
- 주별로 상품 판매량을 보고 그 다음 늘어날 정도를 예측해서, 이게 단순한 대량 구매인지, 실제로 많이 팔리기 시작했는지에 대한 판단이 필요함

### 자기 상관 그래프 (ACF Auto Correlation Function)



- 한달 간격 상관 구해 보고 2달 간격 상관, 3달 간격 상관 을 구해서 막대 그래프를 그려봄
- 한달 전과의 상관 관계,   그래프에서 **p 0.05  위로 올라가면 상관이 있다고 봄**
- **positive한 상관이 있다. 큰 숫자로 시작해서 완만하게 떨어지는 형태임**
- 상관 0 , 모든 간격에서 상관이 0임
- **negative한 상관 : 마이너스 상관관계 있으면 마이너스 플러스 마이너스 플러스 그래프가 나옴**
- 달 별로 상관이 있다. 없다.
- 내려가는데 굉장히 천천히 내려가는 경우, 비정상 시계열의 자기 상관, 20개월, 뚜렷한 패턴 없이 안 떨어지고 계속 있는 경우 비정상이다. 추세 때문에 생기는 거, 추세가 없음.
- 정상일 때는 빨리 떨어짐.
- 자기 상관이 있구나. 자기 상관이 없구나, **positive**, **negative**
- 1개월 간격 자기 상관이 있고, **ACF 찍어보면 자기 상관 그래프를 확인할 수 있다. 12개월 주기로 자기 상관이 있다. 12개월 주기의 계절성이 있군.**
- 마이너스 곱하기 마이너스 플러스가 됨.
- 자기상관 마이너스인 경우(물건 판매), 자기 상관 플러스인 경우(공정)

### PACF

- **간접적으로 영향 주는 부분 빼버리고 직접적으로 영향 주는 부분만 계산함.**
- 1월이 3월에 주는 영향을 빼고 계산함

### 차분

- 시계열 데이터를 직전/직후 시점 간의 차이를 바꾸는 것, **차분을 하면 정상적인 데이터로 바뀌었다. 이 데이터는 선형적인 추세가 있으면 시계열이 비정상**
- 로그 변환를 하면 데이터 늘어나는 정도를 눌러줌
- 로그 변환해주고, 차분을 해주면 선형적인 패턴이 없어지겠죠
- diff = x[1:] - x[:-1] #차분

### SARIMAX

- 굉장히 복잡한 개념임.  S / AR / M
- 한 학기 분량임
- **Moving average : MA모형 데이터가 평균에서 벗어나지 않는다고 가정을 함, 고정된 평균 안에 데이터가 묶여 있다. 데이터가 평균을 따라가는 모형**
- 데이터가 평균에서 벗어난 정도가 입실론, 이 것이 다음 시점에 영향을 줌
- 데이터가 평균을 따라간다. MA 모형의 핵심가정. 다이어리 많이 팔고 덜 팔고 MA 추세를 따라감

### MA 모형

- **MA모형 데이터가 평균에서 벗어나지 않는다고 가정을 함, 고정된 평균 안에 데이터가 묶여 있다. 데이터가 평균을 따라가는 모형**
- **MA(q)파라미터를 따라감**. 다이어리 덜 팔었어요. 그 영향이 좀 갈 수 있음.
- MA - q는 평균에서 벗어났을 때 그 영향이 얼마나 가느냐. ACF를 그려보면 그 q를 맞출 수 있음
- ACF

### AR

- **AR(1)지난 달 영향을 직접 받는 것**
- AR(2) 지지난달 영향을 받는 것
- 얼마나 영향을 주는지 pacf를 보고 결정함, 대충 참고 사항임

### ARMA 모형

- ACF, PACF  모형의 파라미터를 봄
- 모두가 점점 감소하는 형태
- 1하고 1을 2번 넘어주면 됨

### ARIMA

- ARMA에 차분 d가 통합된 것
- 차분 0,1,2, 3 넣어보기

### SARIMA(p, d, q) (P, D, Q, m)

- 뒤에 대문자는 시즌을 반영한 것, m은 월
- **d는 차분, p와 q는 자기 상관,**

### SARIMAX

- SARIMA 변수에 외생 변수가 추가된 형태

### SARIMA 모형의 하이퍼 파라미터 선택

• 하이퍼 파라미터: p, d, q, P, D, Q, m

- 국소적(긴 자기상관) , **계절성, 자기상관, 소문자, 대문자** 
• 플롯, ACF, PACF 등등을 보면서 열심히 생각한다
• **여러 가지로 바꿔가며 AIC, BIC 등을 확인한다**
• **기존 데이터의 마지막 부분을 예측하여 오차(MSE)를 확인한다. 오차가 작으면 예측이 잘 된 것임**