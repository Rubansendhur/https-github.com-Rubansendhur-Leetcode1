SELECT distinct(w.id) 
FROM Weather w
join weather w1 on 
w1.recorddate = Date_sub(w.recorddate, INTERVAL 1 DAY)
where 
w.temperature > w1.temperature 
order by w.id