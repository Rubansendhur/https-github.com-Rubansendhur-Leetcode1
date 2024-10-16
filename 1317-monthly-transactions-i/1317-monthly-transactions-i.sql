# Write your MySQL query statement below
select 
    substr(trans_date,1,7) as month , 
    country , 
    count(id) as trans_count , 
    SUM(CASE WHEN state = 'approved' THEN 1 ELSE 0 END) AS approved_count, 
    sum(amount) as trans_total_amount , 
    sum(case when state = 'approved' then amount else 0 END)as approved_total_amount  
from 
    transactions
group by 
    country, month;