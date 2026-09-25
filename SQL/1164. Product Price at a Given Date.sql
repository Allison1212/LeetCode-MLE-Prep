# Write your MySQL query statement below
# My solution
SELECT DISTINCT(p.product_id) AS product_id, COALESCE(mt.new_price,10) AS price FROM Products AS p 
LEFT JOIN (SELECT * FROM (
SELECT *, ROW_NUMBER() OVER(PARTITION BY product_id ORDER BY change_date DESC) AS rowNbr FROM Products
WHERE change_date <= '2019-08-16'
) AS t
WHERE rowNbr = 1) AS mt
ON p.product_id = mt.product_id

# Better solution 
SELECT product_id, new_price AS price FROM Products
WHERE (product_id, change_date) IN (
SELECT product_id, MAX(change_date) FROM Products
WHERE change_date <= '2019-08-16'
GROUP BY 1
)
UNION 

SELECT product_id, 10 AS price FROM Products
GROUP BY product_id
HAVING MIN(change_date) > '2019-08-16'



-- FROM / JOIN
-- WHERE
-- GROUP BY
-- HAVING
-- Window Functions
-- QUALIFY
-- DISTINCT
-- ORDER BYLIMIT

