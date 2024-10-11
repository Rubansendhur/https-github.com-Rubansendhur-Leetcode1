# Write your MySQL query statement below
select w.id from weather w
join weather w1 on
w.recorddate = date_add(w1.recordDate, INTERVAL 1 DAY) 
where w.temperature > w1.temperature