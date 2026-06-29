# Write your MySQL query statement below

select e.name from employee e
join employee e1 on
e.id = e1.managerid 
group by e1.managerid
having count(e1.name) >= 5 or e.name is null