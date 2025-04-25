SELECT o.ship_city AS cidade,
       SUM(od.unit_price) AS total_cidade
FROM orders AS o
LEFT JOIN order_details AS od
       ON o.order_id = od.order_id
GROUP BY cidade
ORDER BY total_cidade DESC;
