SELECT 
    id AS product_id,
    name AS product_name,
    category,
    price
FROM
    {{source('raw_data','products')}}