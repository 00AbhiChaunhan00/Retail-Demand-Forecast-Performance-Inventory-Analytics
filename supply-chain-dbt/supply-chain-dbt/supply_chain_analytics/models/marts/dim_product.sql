SELECT DISTINCT
    product_id
FROM {{ ref('stg_supply_chain') }}