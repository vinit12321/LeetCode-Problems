  SELECT request_at as Day ,round(cast(sum(CASE WHEN status!='completed' then 1 else 0 end)  as float)/COUNT(*),2)  as [Cancellation Rate]
  FROM Trips where client_id  IN (SELECT  users_id from   Users where banned='No') AND driver_id in (select distinct users_id from users where banned='No')
  and request_at between '2013-10-01' and '2013-10-03'
  group by  request_at 