-- Write your query below
select user_id, max(time_stamp) as last_stamp
from (select * from logins where extract(YEAR from time_stamp::timestamp)=2020)
group by user_id;
