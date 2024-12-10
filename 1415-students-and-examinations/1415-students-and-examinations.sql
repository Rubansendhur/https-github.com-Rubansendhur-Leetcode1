# Write your MySQL query statement below
select s.student_id , s.student_name , s1.subject_name , count(e.subject_name) as attended_exams
from students s CROSS JOIN Subjects s1
left join Examinations e
on
e.student_id=s.student_id 
and
e.subject_name =s1.subject_name
group by s1.subject_name,s.student_name
order by s.student_id,s1.subject_name
