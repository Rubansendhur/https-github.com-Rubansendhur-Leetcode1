-- # Write your MySQL query statement below

-- select s.user_id , round(count(c.action) / count(c.user_id)) as confirmation_rate
-- from signups s 
-- left join confirmations c on
-- s.user_id = c.user_id
-- where c.action = 'confirmed' 

with confirmed_cte as(
    select user_id, count(user_id) as count_confirmed, time_stamp, action 
    from confirmations where action = 'confirmed' 
    group by user_id
),
timeout_cte as(
    select user_id, count(user_id) as total, time_stamp, action from confirmations group by user_id
)

select s.user_id , coalesce(round((c.count_confirmed / t.total),2),0)  as confirmation_rate
from signups s left join 
confirmed_cte c on s.user_id = c.user_id
left join timeout_cte t on s.user_id = t.user_id