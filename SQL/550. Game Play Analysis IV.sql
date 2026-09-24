# Write your MySQL query statement below
# My solution - 有点想复杂了
SELECT ROUND(COUNT(CASE WHEN rnk = 2 AND diff = 1 THEN 1 END)/COUNT(DISTINCT player_id),2) AS fraction FROM (SELECT *, RANK() OVER(PARTITION BY player_id ORDER BY event_date) AS rnk,
DATEDIFF(event_date, LAG(event_date, 1) OVER(PARTITION BY player_id ORDER BY event_date)) AS diff FROM Activity 
) AS t


# 先找到first log date 然后用join
SELECT ROUND(SUM(DATEDIFF(event_date,first_date) = 1)/COUNT(DISTINCT a.player_id),2) AS fraction FROM Activity AS a
LEFT JOIN (
SELECT player_id, MIN(event_date) AS first_date FROM Activity
GROUP BY 1
) AS f
ON a.player_id = f.player_id

# DATEDIFF = date1-date2