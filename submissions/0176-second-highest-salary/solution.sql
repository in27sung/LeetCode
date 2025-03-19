/* Write your PL/SQL query statement below */
SELECT 
    (SELECT salary
    FROM (
        SELECT DISTINCT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS rn 
        FROM Employee
    )
    WHERE rn = 2
    ) AS SecondHighestSalary
FROM DUAL;
