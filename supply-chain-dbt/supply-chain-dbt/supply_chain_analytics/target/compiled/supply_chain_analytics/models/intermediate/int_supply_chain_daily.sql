SELECT
    *,
    units_sold - demand_forecast AS forecast_variance,
    inventory_level - demand_forecast AS inventory_demand_gap

FROM "supply_chain"."analytics"."stg_supply_chain"