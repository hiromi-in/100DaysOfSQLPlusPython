### Day6: Select all orders from USA.

Today's target also was aggregation with some filters.
SQL: Used where clause and case when statement.
Python: groupby().count() function.
Comment: It is getting more involving so being able to create some variables help a lot for easier read.



#### ChatGPT Qs:

* how to resolve this issue? ERROR: 集約関数の呼び出しを入れ子にすることはできません LINE 2: SELECT SUM(CASE WHEN price >= AVG(price) THEN 1 END) AS Over...
* why do we need to use window function?
* What is wrong with this? df\['country'=='USA']
* I only need one column from this; df\[df\['country'] == 'USA'].groupby('quantity').count()
* How to order by the result? print(df\[df\['country'] == 'USA'].groupby('product\_name')\['country'].count())
* Can you convert this to python code? SELECT SUM(CASE WHEN price >= avg\_price THEN 1 END) AS over\_\_or\_on\_avg\_count, SUM(CASE WHEN price < avg\_price THEN 1 END) AS under\_avg\_count FROM ( SELECT price, AVG(price) OVER () AS avg\_price FROM sales WHERE country = 'USA' ) t
* Can we make a dataframe?
* How to do list in markdown



