CREATE VIEW vw_products
AS
SELECT p.product_id,p.product_name,b.brand_name,c.category_name, p.model_year, p.list_price AS [cost_price]
FROM production.products p
JOIN production.brands b ON p.brand_id = b.brand_id
JOIN production.categories c ON p.category_id = c.category_id