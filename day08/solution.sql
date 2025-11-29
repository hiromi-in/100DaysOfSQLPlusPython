--EXTRACT()
SELECT *
FROM sales
WHERE EXTRACT(YEAR FROM order_date) = 2024 AND EXTRACT(MONTH FROM order_date) = 1
ORDER BY order_date, country, product_name, price 

--DATE_PART()
SELECT *
FROM sales
WHERE DATE_PART('year', order_date) = 2024 AND DATE_PART('month', order_date) = 1
ORDER BY order_date, country, product_name, price 
