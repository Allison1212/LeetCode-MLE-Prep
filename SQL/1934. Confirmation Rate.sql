# Write your MySQL query statement below

-- # My solution
-- SELECT res.user_id, COALESCE(confirmation_rate, 0.00) AS confirmation_rate FROM Signups AS res
-- LEFT JOIN(
-- SELECT user_id, ROUND(SUM(CASE WHEN action = 'confirmed' THEN 1 ELSE 0 END) / COUNT(*),2) AS  confirmation_rate FROM Confirmations
-- GROUP BY 1
-- ) AS agg
-- ON res.user_id = agg.user_id

# COALESCE
# Both below works
# ROUND(COUNT(CASE WHEN action = 'confirmed' THEN 1 END) / COUNT(*),2)
# ROUND(SUM(CASE WHEN action = 'confirmed' THEN 1 ELSE 0 END) / COUNT(*),2)
# Final col names 

# Optimal 用average
SELECT s.user_id, COALESCE(ROUND(AVG(action = 'confirmed'),2),0) AS confirmation_rate FROM Signups AS s
LEFT JOIN Confirmations AS c
ON s.user_id = c.user_id
GROUP BY 1
