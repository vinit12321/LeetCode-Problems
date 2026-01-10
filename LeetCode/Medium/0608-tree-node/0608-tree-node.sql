# Write your MySQL query statement below
with cte as(
select 
t.id,j.p_id,count(*) as cnt
from Tree t left join Tree j 
on t.id=j.p_id
group by t.id,j.p_id

)

select 
t.id,
case when t.p_id is null then 'Root'
when c.cnt>1 then 'Inner'
else 'Leaf' end as type
from Tree t join cte c on
t.id=c.id