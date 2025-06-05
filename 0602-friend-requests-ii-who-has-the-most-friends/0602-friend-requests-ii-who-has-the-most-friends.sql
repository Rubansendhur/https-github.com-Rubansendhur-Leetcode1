# Write your MySQL query statement below

with cte as
(select requester_id as id 
from
RequestAccepted 
Union all
select (accepter_id) as id 
from
RequestAccepted)

select id, count(id) as num
from cte
group by id
order by num desc
limit 1

