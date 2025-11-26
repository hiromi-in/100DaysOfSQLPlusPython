--Revenue by product_category
SELECT product_category, SUM(price * quantity) AS revenue
FROM sales
GROUP BY product_category

--Revenue by product_name
SELECT product_name, SUM(price * quantity) AS revenue
FROM sales
GROUP BY product_name

--Revenue by country and product_category
SELECT country, product_category, ROUND(SUM(price * quantity)::numeric,2) AS revenue
FROM sales
GROUP BY country, product_category
ORDER BY country, product_category

--Revenue by week and product_category
SELECT 
    DATE_TRUNC('week', order_date)::date AS week_start,
    product_category,
    ROUND(SUM(price * quantity)::numeric, 2) AS weekly_revenue
FROM sales
GROUP BY week_start, product_category
ORDER BY week_start, product_category;
