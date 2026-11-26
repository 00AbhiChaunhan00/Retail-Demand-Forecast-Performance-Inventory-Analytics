# KPI Definitions – Supply Chain Analytics

## 1. Forecast Performance KPIs

### KPI 1: Weighted Absolute Percentage Error (WAPE)

**Purpose:** Measure the overall size of forecast errors relative to actual sales.

**Formula:**

WAPE = SUM(ABS(Forecast - Actual)) / SUM(Actual) × 100

Where:
- Forecast = demand_forecast
- Actual = units_sold

**Interpretation:**
- Lower WAPE indicates smaller overall forecast errors.
- Higher WAPE indicates larger forecast errors relative to actual sales.

**Aggregation:** Calculate using total absolute error divided by total actual sales, not the average of individual row percentages.

### KPI 2: Forecast Bias %

**Purpose:** Identify whether demand forecasts are generally higher or lower than actual sales.

**Formula:**

Forecast Bias % = SUM(Forecast - Actual) / SUM(Actual) × 100

**Interpretation:**
- Positive value = Over-forecasting.
- Negative value = Under-forecasting.
- Zero = Total forecast equals total actual sales.

A positive bias does not mean every individual record is over-forecasted.

### KPI 3: Mean Absolute Error (MAE)

**Purpose:** Measure the average absolute difference between forecasted and actual units.

**Formula:**

MAE = AVG(ABS(Forecast - Actual))

**Interpretation:**
- Lower MAE indicates smaller average errors in units.
- Higher MAE indicates larger average errors in units.

The unit of measurement is units per record.

### KPI 4: Over-forecast and Under-forecast Records

**Purpose:** Understand how frequently forecasts are higher or lower than actual sales.

**Definitions:**

- Over-forecast: demand_forecast > units_sold
- Under-forecast: demand_forecast < units_sold
- Exact forecast: demand_forecast = units_sold

**Metrics:**

- Over-forecast record count
- Under-forecast record count
- Exact forecast record count
- Percentage of records in each category

These metrics describe record-level frequency, not the magnitude of forecast errors.

## 2. Inventory Analysis KPIs

### KPI 5: Inventory vs Demand Gap

**Purpose:** Compare recorded inventory with forecasted demand.

**Formula:**

Inventory-Demand Gap = inventory_level - demand_forecast

**Interpretation:**

- Positive gap = Recorded inventory is higher than forecasted demand.
- Negative gap = Recorded inventory is lower than forecasted demand.
- Zero gap = Recorded inventory equals forecasted demand.

This is a record-level comparison. It does not confirm overstock or stock-out.

### Supporting Metric: Inventory vs Actual Sales Gap

**Purpose:** Compare recorded inventory with actual units sold.

**Formula:**

Inventory-Sales Gap = inventory_level - units_sold

This metric provides an additional comparison between recorded inventory and actual sales.

It must not be interpreted as confirmed remaining stock because the dataset does not establish whether inventory_level is opening, closing or average inventory.

## 3. KPI Calculation Rules

1. Use units_sold as the actual sales measure.
2. Use demand_forecast as the forecast measure.
3. Define forecast error as demand_forecast - units_sold.
4. Use the same date and record filters when comparing KPIs.
5. Calculate WAPE and Forecast Bias from aggregated sums.
6. Do not average individual row-level percentage errors to calculate WAPE.
7. Do not sum daily inventory snapshots across dates as if they were sales or stock movements.
8. Clearly distinguish record-level metrics from aggregate business-level metrics.

## 4. KPI Limitations

- Forecast methodology and prediction horizon are unavailable.
- Inventory measurement definition is unavailable.
- Inventory gaps indicate differences, not confirmed operational problems.
- Forecast accuracy calculated as 1 - WAPE may be shown as a derived communication metric, but WAPE remains the primary error KPI.
- No KPI alone establishes the cause of forecast errors.

## 5. Final KPI List

| KPI | Measurement |
|---|---|
| WAPE | Percentage |
| Forecast Bias | Percentage |
| MAE | Units |
| Over-forecast Records | Count and percentage |
| Under-forecast Records | Count and percentage |
| Exact Forecast Records | Count and percentage |
| Inventory-Demand Gap | Units |
| Inventory-Sales Gap | Units |