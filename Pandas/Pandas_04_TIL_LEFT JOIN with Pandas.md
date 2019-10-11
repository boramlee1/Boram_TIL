# LEFT JOIN with Pandas

1. 데이터 읽기

- import pandas as pd
- orders = pd.read_csv('https://raw.githubusercontent.com/dataitgirls3/Data/master/Orders.csv')

2. 데이터 확인하기
- customers.head(2)
- orders.head(2)
- orderDetails.head(2)
- products.head(2)

3. 고객 별 주문수를 알려주세요.

- customers_orders = customers.merge(orders, how='left',on='CustomerID')
- customers_orders.head(5)

- customers_num_orders = customers_order.groupby('CustomerID')['OrderID'].count

- customers_num_orders.sort_values()

- customers_num_orders =
customers_order.groupby('CustomerID')['OrderID'].size() #size()와 count()의 차이 #size 는 NaN 값을 count 하지만 count 는 그렇지 않음

- Q1. 1번 고객이 진짜 주문을 한번도 안했는지 확인해볼까요

- customers_orders[(customers_orders['CustomerID'] ==1)]     

- Q2. 고객 중 동명이인이 있나요?

- Same_name=customers_order.groupby('CustomerName').sum()
Same_name

4. 1996년 10월 동안 고객 별 주문 수를 계산하세요.

- 10월 주문만 뽑기
- orders_october = orders.set_index('OrderDate').loc['1996-10-01':'1996-10-31',:]
- orders_october.head(2)

- orders_october = orders_october.reset_index()   # row를 추가한 후에 reset index를 통해 index를 0부터 새롭게 지정한다. # reset_index를 이용해서 index를 리셋하는 것을 많이 사용한다.
- orders_october 

- customers_orders_october = customers.merge(orders_october,how='left', on='CustomerID')

- customers_num_orders_october = customers_orders_october.groupby('CustomerID')['OrderID'].count()
- customers_num_orders_october.sort_values()

5. 고객 별 주문금액을 알려주세요.\
**step1. 주문 별 금액 계산**

- orders_detail = orders.merge(orderDetails, how='inner', on='OrderID').merge(products, how='inner', on='ProductID')[['OrderID', 'CustomerID', 'OrderDate', 'OrderDetailID', 'Quantity', 'Price']]

- orders_detail['total_price'] = orders_detail['Quantity'] * orders_detail['Price']

- price_by_order = orders_detail.groupby(['OrderID', 'CustomerID', 'OrderDate'])['total_price'].sum().reset_index()

- price_by_order.head(5)

- orders_detail[orders_detail['OrderID'] == 10248]['total_price'].sum()\
\
**Step2. 고객 데이터와 붙이기**

- customers_price_by_order =customers.merge(price_by_order, how='left', on = 'CustomerID') 
- customers_price_by_order.head(2)

- customers_price_by_order['total_price'] = customers_price_by_order['total_price'].fillna(0)

- price_by_customers = customers_price_by_order.groupby('CustomerID')['total_price'].fillna(0)
- price_by_customers

6. 1996년 10월 동안 고객 별 주문 금액을 계산하세요. 10월 중 주문을 한 번도 하지 않은 고객 목록을 주세요.\
\
**Step1. 10월 주문 별 금액 계산**

- price_by_order_october = price_by_order.set_index('OrderDate').loc['1996-10-01':'1996-10-30',:].reset_index()\
\
**Step2. 고객 데이터와 붙이기**
- customers_price_by_order_october = customers.merge(price_by_order_october, how='left', on='CustomerID')
