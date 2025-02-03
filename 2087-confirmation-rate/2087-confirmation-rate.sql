select 
s.user_id , 
    ROUND(IFNULL(AVG(c.action = 'confirmed'), 0), 2) AS confirmation_rate
from
Signups s left join confirmations c on
s.user_id = c.user_id
group by s.user_id