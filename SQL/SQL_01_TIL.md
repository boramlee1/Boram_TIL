
# 문제풀이1
```SQL
# Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name). If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.

select CITY,LENGTH(CITY)
FROM STATION
GROUP BY CITY
ORDER BY LENGTH(CITY) DESC 
LIMIT 1;

select CITY,LENGTH(CITY)
FROM STATION
GROUP BY CITY
ORDER BY LENGTH(CITY) ASC 
LIMIT 1;

# 문제풀이 2
SELECT AVG(CASE WHEN quantity IS NULL THEN 0 ELSE quantity END)
AS avgnull0 FROM sample51;

# 내부 처리 순서
WHERE 구 → GROUP BY 구 → HAVING 구 → SELECT 구 → ORDER BY 

# 집계함수 사용할 경우 HAVING 구로 검색 조건 지정
SELECT name, COUNT(name) FROM sample51
GROUP BY name HAVING COUNT(name) = 1;

# GROUP BY
SELECT name, quantity FROM sample51 GROUP BY name, quantity;

# 결과값 정렬
SELECT name, COUNT(name),SUM(quantity)
FROM sample2 GROUP BY name ORDER BY SUM(quantity) DESC;

# OrderID 10249번에 들어있는 상품명, 납품한 업체 이름, 업체가 소속된 국가를 모두 출력하세요.
[링크](https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all)

SELECT o.OrderID, p.ProductName, s.ShipperName, sp.Country
FROM Orders AS o 
	 INNER JOIN OrderDetails AS od ON o.OrderID= od.OrderID
	 INNER JOIN Products AS p ON p.ProductID = od.ProductID
     INNER JOIN Suppliers AS sp ON sp.SupplierID = p.SupplierID 
     INNER JOIN Shippers AS s ON s.ShipperID = o.ShipperID
WHERE o.OrderID = 10249
 
 # 가입 고객 정보가 있는데, 주문을 한 번도 하지 않은 고객에게 첫 구매를 유도하기 위해서 이런 고객을 대상으로 다양한 프로모션을 시도 해 볼 수 있겠지요? 이럴 때 LEFT JOIN을 사용할 수 있음

SELECT  o.OrderID, c.CustomerID, c.CustomerName
FROM Customers as c LEFT JOIN Orders AS o ON o.CustomerID = c.CustomerID
WHERE OrderID is null

