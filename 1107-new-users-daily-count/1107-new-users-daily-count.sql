
with t as (
    select 
        user_id,  
        min(activity_date) as login_date
    from traffic 
    where activity = 'login'
    group by user_id 
)

select 
    login_date, 
    count(distinct user_id) as user_count
from t 
where login_date >= date_sub('2019-06-30', interval 90 day)
group by login_date
order by login_date