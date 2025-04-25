select o.ship_city as cidade, sum(od.unit_price)as total_cidade
from orders as o
left join order_details as od
on o.order_id = od.order_id
group by cidade
order by total_cidade desc;