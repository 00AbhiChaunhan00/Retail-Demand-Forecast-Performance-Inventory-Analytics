SELECT
    CAST(date AS DATE) AS date,
    store_id,
    product_id,
    category,
    region,
    inventory_level,
    units_sold,
    units_ordered,
    demand_forecast,
    price,
    discount,
    weather_condition,
    holiday_promotion,
    competitor_pricing,
    seasonality

FROM "supply_chain"."public"."stg_supply_chain"