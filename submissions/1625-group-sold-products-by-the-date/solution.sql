/* Write your PL/SQL query statement below */
SELECT 
    TO_CHAR(TRUNC(sell_date)) AS sell_date, 
    COUNT(DISTINCT product) AS num_sold, 
    LISTAGG(product, ',') WITHIN GROUP (ORDER BY product) AS products
FROM (
    SELECT DISTINCT sell_date, product
    FROM Activities
)
GROUP BY 
    sell_date
ORDER BY 
    sell_date;
