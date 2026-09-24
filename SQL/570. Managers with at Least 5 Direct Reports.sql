# Write your MySQL query statement below
SELECT name FROM Employee AS e
INNER JOIN 
(SELECT managerId, COUNT(*) AS nbr_direct_report FROM Employee
GROUP BY 1
HAVING nbr_direct_report >=5) AS m
ON m.managerId = e.id