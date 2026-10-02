SELECT product_name, SUM(price) AS "Total Revenue per product"
FROM sales
GROUP BY product_name
ORDER BY SUM(price) DESC;
