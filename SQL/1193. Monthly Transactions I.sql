# Write your MySQL query statement below

# 我的solution
SELECT DATE_FORMAT(trans_date, '%Y-%m') AS month, 
country, 
COUNT(*) AS trans_count, 
COUNT(CASE WHEN state = 'approved' THEN 1 END) AS approved_count,
SUM(amount) AS trans_total_amount,
SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 END) AS approved_total_amount
FROM Transactions
GROUP BY 1,2


# Further improve 炫技

SELECT LEFT(trans_date,7) AS month, 
country, 
COUNT(*) AS trans_count, 
SUM(state = 'approved') AS approved_count,
SUM(amount) AS trans_total_amount,
SUM(IF (state = 'approved', amount,0)) AS approved_total_amount
FROM Transactions
GROUP BY 1,2

# 几个不常见的syntax
# DATE_FORMAT(trans_date, '%Y-%m')
# LEFT(trans_date,7)
# sum（boolean operation） 直接true 返回1
# sum （if（condition， true， false）） 的写法