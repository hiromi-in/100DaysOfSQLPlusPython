SELECT DISTINCT product_category, COUNT(*)
FROM sales
GROUP BY product_category

/*
"Clothing"	2551
"Electronics"	2433
"Home"	2464
"Sports"	2552
*/