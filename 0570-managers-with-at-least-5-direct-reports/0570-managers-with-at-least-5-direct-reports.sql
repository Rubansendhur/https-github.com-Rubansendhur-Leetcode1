# Write your MySQL query statement below
select e.name from employee e 
join employee e1 on 
e1.managerid = e.id 
group by e1.managerid
HAVING COUNT(e.name) >= 5 or e.name is null;
