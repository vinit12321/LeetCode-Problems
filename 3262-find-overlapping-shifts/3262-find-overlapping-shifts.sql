/* Write your PL/SQL query statement below */
select e1.employee_id,count(*) as overlapping_shifts  from EmployeeShifts e1 inner join EmployeeShifts e2
on e1.employee_id=e2.employee_id  
where  e1.start_time<e2.start_time and  e1.end_time > e2.start_time
group by e1.employee_id 
order by employee_id