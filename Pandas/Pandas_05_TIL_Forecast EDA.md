# Forecast EDA, 예측 컴피티션

1. 데이터 읽어오기

- %matplotlib inline     # 시각화 
- import pandas as pd
- train = pd.read.csv('funda_train.csv')

2. 상점 별 매출 예측 

- train.dtypes   # 데이터의 타입
- len(train)
- train['card_company'].unique()
- print('Length of Train: ' + str(len(train)))
print('Store Id: ' + str(len(train['store_id'].unique())))
print('Type of Business: ' + str(len(train['type_of_business'].unique())))
print('Card Id: ' + str(len(train['card_id'].unique())))
print('Transacted Date: ' + str(len(train['transacted_date'].unique()))) # str.get()  메소드는 전달된 위치에서 요소를 가져오는 데 사용

- 데이터가 언제부터 언제까지 있었는지? min(), max()함수
- print('first date of log: ' +train['transacted_date'].min())
- print('last date of log): ' +train['transacted_date'].max()) 

3. Missing Values

- train.isnull().sum() * 100 / len(train) # region에는 30%, type_of_business에는 60% 정도 null

4. Outlier

- train['amount'].describe()
- print(train['amount'].min())
- print(train['amount'].quantile(0.01))
- print(train['amount'].quantile(0.99))
- print(train['amount'].max())

5. Winsorize   #아웃라이어 극단값 보정, 경계값 너머의 값을 경계값으로 보정 # 경계값 너머의 값을 모두 제거해 버리는 Trim, Truncation

- amount_min = train['amount'].quantile(0.01)
- amount_max = train['amount'].quantile(0.99)
- train['amount_winsorized'] = train['amount'].apply(lambda x: max(min(x,  amount_max), amount_min)) 
- lambda 익명 함수로 간단하게 함수를 만들어서 사용할 때 사용, 익명함수라는 말 그대로 일반적으로는 변수에 할당하지 않고 사용 
- apply는 map과 다르게 전체 column에 해당 함수를 적용
- train.head(2)
- train['amount_winsorized'].hist()  #히스토그램

6. Seasonality

- yearly seasonality, monthly seasonality가 명확하게 보이는 데이터인가?
- train = train.reset_index()

- transaction_day = train.groupby(['transacted_date']).agg({'index':'size', 'amount':'sum'}).reset_index()
- 날짜별로 인덱스 크기와 amount합계를 출력해서 리스트를 만들어라. 좋은 기능이네 
- agg 만약 원하는 그룹연산이 없는 경우 함수를 만들고 이 함수를 agg에 전달함. 또는 **여러가지 그룹연산을 동시에 하고 싶은 경우 함수 이름 문자열의 리스트를 전달** 

- transaction_day.head(2)

- transaction_day.plot(x='transacted_date', y='index', figsize=(15,7)) #figsize 사이즈 조절

- 주 단위 Seasonality는 명확하게 보이네요. 그런데 매출이 저렇게 푹 꺼진데는 무슨일이 있었던 걸까요?

- transaction_day.set_index('transacted_date').loc['2019-01-01':,:].plot(y='index', figsize=(15,7))
