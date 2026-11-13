-- Write your query below
select distinct seller_name
from seller
where seller_id not in (select distinct seller_id from orders where extract(year from sale_date)=2020);