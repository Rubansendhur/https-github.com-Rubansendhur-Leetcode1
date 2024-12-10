# Write your MySQL query statement below
select distinct(s.user_id) , round(COALESCE(avg(action = 'confirmed'),0),2)as confirmation_rate
from signups s left join confirmations c on 
s.user_id = c.user_id 
group by user_id
