/* Write your PL/SQL query statement below */
SELECT user_id, name, mail
FROM Users
WHere REGEXP_LIKE(mail, '^[A-Za-z][A-Za-z0-9_\.\-]*@leetcode\.com$');
