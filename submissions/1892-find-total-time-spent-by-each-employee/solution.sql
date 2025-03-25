/* Write your PL/SQL query statement below */
SELECT 
    TO_CHAR(TRUNC(event_day)) AS "day",  -- Convert date to YYYY-MM-DD string (remove time part)
    emp_id,                              -- Grouping by employee
    SUM(out_time - in_time) AS "total_time"  -- Total time worked per employee per day
FROM Employees
GROUP BY 
    TO_CHAR(TRUNC(event_day)),  -- Group by the same expression used in SELECT
    emp_id;
