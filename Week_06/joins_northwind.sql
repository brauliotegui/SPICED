-- Which company is the best customer (in terms of total revenue generated)?
CREATE TABLE best_customer_table AS
SELECT c.company_name, sum(od.quantity*od.unit_price) as revenue
FROM customers AS c
JOIN orders AS o ON c.customer_id = o.customer_id
JOIN order_details AS od ON od.order_id = o.order_id
GROUP BY c.company_name
ORDER BY revenue DESC
;


CREATE MATERIALIZED VIEW best_customer_materialized_view AS
SELECT c.company_name, sum(od.quantity*od.unit_price) as revenue
FROM customers AS c
JOIN orders AS o ON c.customer_id = o.customer_id
JOIN order_details AS od ON od.order_id = o.order_id
GROUP BY c.company_name
ORDER BY revenue DESC
;


SELECT *
FROM best_customer_view;
