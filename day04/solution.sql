--By customer_id
SELECT COUNT(DISTINCT customer_id) AS Number_of_customers
FROM sales

--By country
SELECT country, COUNT(DISTINCT customer_id) AS Number_of_customers
FROM sales
GROUP BY country