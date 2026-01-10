# Write your MySQL query statement below
with cte as (
select id,visit_date,people,
case when people <100 then 0 else 1  end as occ
from Stadium
),
cte2 as (
select id,visit_date,people,occ, id-row_number() over(partition by occ order by visit_date )
as diff
from cte
),
cte3 as (
select occ,diff,count(diff)  as cnt from cte2
group by 1 ,2
having count(diff) >=3

)
select c2.id,c2.visit_date,c2.people from cte3 c1 join cte2 c2
on c1.diff=c2.diff and c1.occ=c2.occ
