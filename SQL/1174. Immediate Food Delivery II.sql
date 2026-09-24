# Write your MySQL query statement below
SELECT ROUND(AVG(order_date = customer_pref_delivery_date) * 100,2) AS immediate_percentage FROM (SELECT * , RANK() OVER (PARTITION BY customer_id ORDER BY order_date ) AS rnk FROM Delivery) AS t
WHERE rnk = 1

# RANK 在时间戳一样的时候会可能出现两个rank = 1， 最好用ROW_NUMBER()
# Window function 一般很cost， 这题可以用我最初的group 写
SELECT ROUND(AVG(order_date = customer_pref_delivery_date)*100,2) AS immediate_percentage FROM Delivery AS d
INNER JOIN  (
SELECT customer_id, MIN(order_date) AS first_order FROM Delivery
GROUP BY 1
) AS t
ON d.customer_id = t.customer_id
WHERE order_date = first_order
