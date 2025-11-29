### Day8: Show orders in January 2024.  



Today's target also was filters for a date column.
SQL: Used EXTRACT().
Python: Simple filter. (df\[df\[column\_name]==value])
Comment: It was almost the same as yesterday so I reused the commands I wrote yesterday. I just changed the inside of WHERE clause in SQL or values in some variables in Python.



#### ChatGPT Qs:

* How to get year from date time column in postgresql?
* Can you refine this?

df\_january = df\[(df\['order\_date'] >='2024-01-01') and (df\['order\_date'] < '2024-01-31')].sort\_values(\['order\_date', 'country', 'product\_name', 'price'])

