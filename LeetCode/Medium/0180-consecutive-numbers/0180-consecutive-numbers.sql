-- Write your PostgreSQL query statement below
with cte as (
select id,num,row_number() over(partition by num order by id) as rw,
id-row_number() over(partition by num order by id) as diff
from Logs
)
select distinct num as ConsecutiveNums from cte
group by num,diff
having count(*) >=3