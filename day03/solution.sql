--The number of all orders
SELECT COUNT(*) Orders
FROM sales;

--Count by country
SELECT country, COUNT(*) count
FROM sales
GROUP BY country;

--Count by price
WITH t AS (
    SELECT 
        COUNT(*) FILTER (WHERE price >= 0   AND price < 50)  AS less_than_50,
        COUNT(*) FILTER (WHERE price >= 50  AND price < 100) AS from_50_to_99,
        COUNT(*) FILTER (WHERE price >= 100 AND price < 150) AS from_100_to_149,
        COUNT(*) FILTER (WHERE price >= 150 AND price < 200) AS from_150_to_199,
        COUNT(*) FILTER (WHERE price >= 200 AND price < 250) AS from_200_to_249,
        COUNT(*) FILTER (WHERE price >= 250 AND price < 300) AS more_than_250
    FROM sales
)
SELECT 'less_than_50'   AS price_range, less_than_50   AS count FROM t UNION ALL
SELECT 'from_50_to_99',  from_50_to_99                 FROM t UNION ALL
SELECT 'from_100_to_149', from_100_to_149              FROM t UNION ALL
SELECT 'from_150_to_199', from_150_to_199              FROM t UNION ALL
SELECT 'from_200_to_249', from_200_to_249              FROM t UNION ALL
SELECT 'more_than_250', more_than_250              FROM t;

--Count by order month
SELECT COUNT(*) FILTER(WHERE EXTRACT(MONTH FROM order_date) = 1 ) AS January
     , COUNT(*) FILTER(WHERE EXTRACT(MONTH FROM order_date) = 2 ) AS February
	 , COUNT(*) FILTER(WHERE EXTRACT(MONTH FROM order_date) = 3 ) AS March
FROM sales;

--Count by quantity
WITH t AS (
    SELECT 
        COUNT(*) FILTER (WHERE quantity<= 4)  AS less_than_4,
        COUNT(*) FILTER (WHERE quantity >= 4  AND quantity < 7 ) AS from_4_to_6,
	    COUNT(*) FILTER (WHERE quantity >= 7  AND quantity <= 10)  AS from_7_to_10
    FROM sales
)
SELECT 'less_than_4'   AS qyantity_range, less_than_4   AS count FROM t UNION ALL
SELECT 'from_4_to_6',  from_4_to_6                 FROM t UNION ALL
SELECT 'from_7_to_10', from_7_to_10              FROM t ;
