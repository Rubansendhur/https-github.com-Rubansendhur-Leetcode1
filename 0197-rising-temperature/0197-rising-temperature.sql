# Write your MySQL query statement below
select distinct(w1.id) from weather w1 join weather w2 on 
w2.recorddate = date_sub(w1.recordDate, interval 1 day)
where w1.temperature > w2.temperature
order by w1.id