# Write your MySQL query statement below
SELECT customer_id FROM Customer AS c
GROUP BY 1
HAVING COUNT(DISTINCT c.product_key) = (SELECT COUNT(DISTINCT product_key) FROM Product)