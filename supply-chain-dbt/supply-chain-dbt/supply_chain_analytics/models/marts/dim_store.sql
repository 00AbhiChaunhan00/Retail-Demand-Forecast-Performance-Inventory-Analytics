SELECT DISTINCT
    store_id
FROM {{ ref('stg_supply_chain') }}