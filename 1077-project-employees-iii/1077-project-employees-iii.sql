# Write your MySQL query statement below
with cte as 
(select e.employee_id,p.project_id,experience_years,
dense_rank() over(partition by p.project_id order by experience_years desc) as rnk
from Project p join Employee e 
on p.employee_id=e.employee_id
)
select project_id,employee_id from cte where rnk=1