# Pandas 101

* import pandas as pd
* import numpy as np
* 판다스는 대소문자 구별

1. Object Creation(객체 생성)\
\
**[Series]**
* s = pd.Series([1, 2, 3, 4, 5, np.nan, 8])
* len(s) #s의 길이\
\
**[Dataframe]**
* df = pd.DataFrame({'A': 1, 
                   'B': 'String',
                   'C': s,
                   'D': pd.Series([2, 3, 4, 5, 6, 7, 8])})
\
\
**[DataFrame df의 길이]**

* len(df)
* df.dtypes
\
\
**[Read data from outside]**

* house_price = pd.read_csv
* len(house_price)
* house_price.columns

2. Viewing DAta(데이터 확인하기)
\
\
**[데이터의 일부를 눈으로 확인하기]**

* df.tail() #끝에서 마지막 5줄 불러옴
* df.head()
* df.head(2)
* df.columns
* house_price.columns
* df.values
* df.describe()
* house_price.describe()
* df.T
* df.sort_index(axis=0, ascending=False)
* df.sort_index(axis=1, ascending=False) #축별로 정렬
* df.sort_index()
* df.sort_values(by='D', ascending=False)
* house_price.sort_values(by='SalePrice', ascending=False)

3. Selection(선택)
* 'df['C']
\
\
**[Selection by Label]**

* df.loc[index, column]
* df.loc['20190801':'20190803',['A','B']]



