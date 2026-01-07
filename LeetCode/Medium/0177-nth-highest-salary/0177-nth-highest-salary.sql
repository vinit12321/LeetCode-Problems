CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
with cte as (
        select 
        salary, dense_rank() over(order by salary desc) as rn 
        from Employee
    )
    select salary from cte where rn=N
    
  );
END