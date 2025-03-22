/* Write your PL/SQL query statement below */
DELETE FROM Person
WHERE id NOT IN (
    SELECT id FROM (
        SELECT id, ROW_NUMBER() OVER (PARTITION BY email ORDER BY id ASC) AS rnk
        FROM Person
    )
    WHERE rnk = 1
);
