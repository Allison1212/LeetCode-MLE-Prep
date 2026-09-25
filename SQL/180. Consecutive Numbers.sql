# Write your MySQL query statement below
SELECT DISTINCT num AS ConsecutiveNums FROM (
SELECT *, LAG(num,1) OVER(ORDER BY id) AS prev,
LEAD(num,1) OVER(ORDER BY id) AS next FROM Logs 
) AS t 
WHERE t.num = prev and t.num = next

# 这里主要特殊的是3个连续的这样就可以看前一个和后一个