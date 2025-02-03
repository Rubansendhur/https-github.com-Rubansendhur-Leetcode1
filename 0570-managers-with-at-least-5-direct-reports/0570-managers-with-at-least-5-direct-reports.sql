select e.name from employee e
join employee e1 on e.id = e1.managerid
group by e.id
having count(e1.managerid) >= 5
