# Write your MySQL query statement below
select r.contest_id ,round(count(distinct r.user_id) / count(distinct u.user_id)  * 100 , 2) as percentage 
from users u join register r 
group by contest_id
ORDER BY 2 DESC, 1 ASC;