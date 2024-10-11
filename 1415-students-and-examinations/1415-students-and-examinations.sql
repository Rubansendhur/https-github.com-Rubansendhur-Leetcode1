# Write your MySQL query statement below
#select count(e.subject_name) from Examinations e join ex.student_id on Examinations 
#where e.subject_name = ex.subject_name group by e.subject_name;

# Write your MySQL query statement below

select distinct s.student_id, s.student_name, s1.subject_name, count(e.student_id) as attended_exams
from students s cross join subjects s1
left join examinations e on
s.student_id = e.student_id and s1.subject_name = e.subject_name 
group by s.student_id, s.student_name, s1.subject_name
order by s.student_id,s1.subject_name



