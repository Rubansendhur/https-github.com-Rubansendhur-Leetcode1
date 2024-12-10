# Write your MySQL query statement below
select e.name , b.bonus from Employee e 
left join bonus b on
e.empid = b.empid
having bonus < 1000 or bonus is null