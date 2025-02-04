select contest_id , 
ROUND(COUNT(r.user_id) * 100.0 / (select count(user_id) from users), 2) AS percentage
from
users u join register r on
u.user_id = r.user_id 
group by r.contest_id
order by percentage desc,contest_id


