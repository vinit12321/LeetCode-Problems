CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      select distinct salary as getNthHighestSalary from 
      (select *, dense_rank() over(order by salary desc) as rn
      from Employee ) a where a.rn=N
  );
END