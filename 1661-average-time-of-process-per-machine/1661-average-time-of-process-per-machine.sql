# Write your MySQL query statement below

with start_cte as(
    select machine_id, process_id, timestamp as start_time from activity where activity_type = 'start'
    group by machine_id, process_id
),
 end_cte as(
    select machine_id, process_id, timestamp as end_time from activity where activity_type = 'end'
    group by machine_id, process_id
)

select s.machine_id, round(avg(e.end_time - s.start_time),3) as processing_time 
from start_cte s join end_cte e
on s.machine_id = e.machine_id
and
s.process_id = e.process_id
group by machine_id