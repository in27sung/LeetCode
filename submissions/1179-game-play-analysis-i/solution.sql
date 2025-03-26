/* Write your PL/SQL query statement below */
SELECT 
    player_id, TO_CHAR(MIN(TRUNC(event_date))) AS first_login
FROM 
    Activity
GROUP BY 
    player_id;
