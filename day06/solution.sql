--Total number of orders from the US
SELECT COUNT(*) AS Number_of_orders
FROM sales
WHERE country = 'USA'

--Number of orders from the US by product category
SELECT product_category, COUNT(*) AS Number_of_orders
FROM sales
WHERE country = 'USA'
GROUP BY product_category

--Number of orders from the US by item quantity
SELECT quantity, COUNT(*) AS Number_of_orders
FROM sales
WHERE country = 'USA'
GROUP BY quantity
ORDER BY quantity

--Number of orders from the US by product name
SELECT product_name, COUNT(*) AS Number_of_orders
FROM sales
WHERE country = 'USA'
GROUP BY product_name
ORDER BY COUNT(*) DESC

--Number of orders from the US in comparison of average
SELECT 
    SUM(CASE WHEN price >= avg_price THEN 1 END) AS over__or_on_avg_count,
    SUM(CASE WHEN price <  avg_price THEN 1 END) AS under_avg_count
FROM (
    SELECT price, AVG(price) OVER () AS avg_price
    FROM sales
	WHERE country = 'USA'
) t


