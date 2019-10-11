# INNER JOIN with Pandas
- import pandas as pd

1. 데이터 읽기

- orders = pd.read_csv('https://raw.githubusercontent.com/dataitgirls3/Data/master/Orders.csv')

2. 데이터 확인하기

- print('columns in Orders:' + str(list(orders.columns)))
- print('columns in OrderDetails:' + str(list(orderDetails.columns)))
- print(list(orders.columns))
- print(len(orders))
- print(len(orderDetails))
- orders.head(2)
- ordersDetails.head(2)
- orderDetails
- product.head(2)

3. 분석의 목표

- orders -> orderDetails -> products 테이블을 묶어서 order 당 몇 개의 상품을 주문하는지, 종류는 얼마나 다양한지, 총 가격은 얼마인지 등을 구해보자.

- Order 한 개에 얼마나 다양한 물건들이 들어있는가?
- order_orderDetails = orders.merge(orderDetails, how='inner', on='OrderID')
- order_orderDetails.head(2)

- product_per_order = order_orderDetails.groupby('OrderID').size()
product_per_order
- product_per_order.mean()

- Order 한 개에 총 몇 개의 물건이 들어 있는가?

- num_items_per_order = order_orderDetails.groupby('OrderID')['Quantity'].sum()
num_items_per_order
num_items_per_order.mean()

- 주문마다 총 가격

- order_all_price = order_orderDetails.merge(products, how='inner',on='ProductID')
order_all_price 
- order_all_price.head(2)

- 컬럼 필요한 것만 추리기
- 주문마다 총 가격 

 - order_all_part = order_all[['OrderID', 'OrderDate', 'Quantity', 'ProductID', 'CategoryID', 'Price']]

- total_price = order_all_part['Price'] * order_all_part['Quantity']
- order_all_part['TotalPricePerProduct'] = total_price

- price_per_order = order_all_part.groupby('OrderID')['TotalPricePerProduct'].sum()
price_per_order

- 총 가격이 1000불 이상인 주문만 뽑아주세요.

- price_per_order[price_per_order >= 1000]

4. 문제풀이

- Q1. Products의 CategoryID와 Categories 테이블을 이용해서, 어떤 카테고리의 상품이 가장 많이 주문되었는지 구하세요.

- categories.head(2)
- order_all_price_categories= order_all_price.merge(categories,how='inner', on='CategoryID')

- order_all_price_categories.head(2)

- most_order=order_all_price_categories.groupby('CategoryName').size()
- most_order

- Q2. Orders 테이블의 OrderDate를 이용해, 어떤 날에 주문이 가장 많았는지 알려주세요.

- Order_day=order_all_price_categories.groupby('OrderDate')['Quantity'].sum() 
- Order_day

- Order_day.max()

- Q3. Orders 테이블의 OrderDate를 이용해, 어떤 날에 매출금액이 가장 높았는지 알려주세요.

- order_all_price_categories['total_price']=order_all_price_categories['Price']*order_all_price_categories['Quantity']

- order_all_price_categories.groupby('OrderDate')['total_price'].sum() #날짜 별로 합계 , 최고 매출 금액

- order_all_price_categories.sort_values(by='total_price',ascending=False).head(3)   #고객 아이디별로 날짜별 최고 매출 금액
