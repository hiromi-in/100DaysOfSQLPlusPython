SELECT *
FROM sales
WHERE product_category = 'Electronics'
ORDER BY country, order_date, product_name, price 