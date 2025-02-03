select a.machine_id, round(avg(a1.timestamp - a.timestamp),3) as processing_time from
activity a join activity a1 on
a.process_id = a1.process_id and a.machine_id = a1.machine_id
and 
a.activity_type = 'Start' and a1.activity_type = 'end'
group by machine_id
order by machine_id
