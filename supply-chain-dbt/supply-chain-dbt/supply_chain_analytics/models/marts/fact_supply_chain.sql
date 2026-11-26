
SELECT
    date,
    store_id,
    product_id,
    category,
    region,

    inventory_level,
    units_sold,
    units_ordered,
    demand_forecast,

    forecast_variance,
    inventory_demand_gap,

    price,
    discount,
    competitor_pricing,

    weather_condition,
    holiday_promotion,
    seasonality

FROM {{ ref('int_supply_chain_daily') }}
