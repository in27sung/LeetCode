/* Write your PL/SQL query statement below */
SELECT eu.unique_id, e.name 
FROM Employees e
LEFT OUTER JOIN EmployeeUNI eu
ON e.id = eu.id;
