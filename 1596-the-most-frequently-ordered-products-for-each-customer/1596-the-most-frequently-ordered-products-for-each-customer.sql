/* Write your PL/SQL query statement below */

with cte as (

    select customer_id,product_id,count(*) as cnt
    from Orders 
    group by  customer_id,product_id
),
rnkOrder as (

    select customer_id,product_id,dense_rank()
    over(partition by customer_id order by cnt desc ) as rnk
    from cte
)
select 
o.customer_id,o.product_id,p.product_name
from rnkOrder o join Products p on o.product_id=p.product_id
where rnk=1
