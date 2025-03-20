/* Write your PL/SQL query statement below */
SELECT d.name AS Department, e.name AS Employee, e.Salary AS Salary
FROM (
    SELECT e.*, DENSE_RANK() OVER (PARTITION BY e.departmentId ORDER BY e.salary DESC) AS rnk
    FROM Employee e
) e
JOIN Department d ON e.departmentId = d.id
WHERE e.rnk = 1;
