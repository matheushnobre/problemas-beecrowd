SELECT c.name, r.rentals_date
FROM customers c
INNER JOIN rentals r ON c.id = r.id_customers
WHERE EXTRACT(YEAR FROM r.rentals_date) = 2016
AND EXTRACT(MONTH FROM r.rentals_date) = 9;