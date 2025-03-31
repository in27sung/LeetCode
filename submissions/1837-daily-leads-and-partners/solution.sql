/* Write your PL/SQL query statement below */
SELECT 
    to_char(date_id, 'yyyy-mm-dd') AS "date_id",  
    make_name, 
    COUNT(DISTINCT lead_id) AS "unique_leads", 
    COUNT(DISTINCT partner_id) AS "unique_partners"
FROM DailySales
GROUP BY date_id, make_name;

