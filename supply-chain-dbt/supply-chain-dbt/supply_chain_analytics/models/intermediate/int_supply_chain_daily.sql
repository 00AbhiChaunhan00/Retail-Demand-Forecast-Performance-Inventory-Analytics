
SELECT
    *,
    units_sold - demand_forecast AS forecast_variance,
    inventory_level - demand_forecast AS inventory_demand_gap

FROM {{ ref('stg_supply_chain') }}
