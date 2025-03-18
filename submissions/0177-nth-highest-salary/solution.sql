CREATE FUNCTION getNthHighestSalary(N IN NUMBER) RETURN NUMBER IS
result NUMBER;
BEGIN
    /* Write your PL/SQL query statement below */
    SELECT salary INTO result
    FROM (SELECT DISTINCT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk FROM Employee)
    WHERE rnk = N;

    RETURN result;

EXCEPTION
    -- Handle case when N-th salary does't exist (No_Data_Found)
    WHEN NO_DATA_FOUND THEN
        RETURN NULL;
END;
