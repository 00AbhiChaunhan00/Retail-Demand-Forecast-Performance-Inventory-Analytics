# Supply Chain Demand, Forecast & Inventory Analytics

## 1. Business Scenario

A retail business manages inventory across multiple stores and product categories. Accurate demand forecasting is important for planning inventory and ensuring that stock levels remain aligned with expected customer demand.

However, differences between forecasted demand and actual sales can create planning challenges. Overestimating demand may contribute to excess inventory, while underestimating demand may increase the risk of insufficient stock.

The business wants to understand how accurately demand is being forecasted and whether recorded inventory levels appear aligned with actual demand.

**Note:** This is an analytical business case study using a retail inventory forecasting dataset, not verified operational data from a named company.

## 2. Business Problem

The primary problem being investigated is:

**Is the demand forecasting process consistently overestimating or underestimating actual sales, and what patterns can be identified in forecast errors and inventory levels?**

The analysis will investigate the direction, magnitude and distribution of forecast errors, along with the relationship between recorded inventory and actual demand.

## 3. Business Objectives

1. Measure the difference between forecasted demand and actual units sold.
2. Identify whether forecasts show consistent over-forecasting or under-forecasting.
3. Identify periods and recorded product, category and regional groups with relatively high forecast errors.
4. Examine whether recorded inventory levels are aligned with actual demand.
5. Translate analytical findings into practical recommendations for demand planning and inventory monitoring.

## 4. Key Business Questions

- How close is forecasted demand to actual sales?
- Is the business consistently over-forecasting or under-forecasting?
- During which months or dates are forecast errors relatively high?
- Which recorded product, category or regional groups show larger forecast errors?
- How does recorded inventory compare with actual demand?
- Are any available dataset variables associated with differences in forecast errors?

## 5. Expected Business Outcomes

- A clear measurement of forecast performance.
- Identification of forecast bias and periods with larger errors.
- Visibility into inventory-demand gaps.
- Evidence-based recommendations for monitoring demand and inventory planning.

## 6. Scope and Limitations

This analysis uses historical records from 2022 to 2024.

The dataset does not provide verified stock-out events, replenishment lead times, purchase order receipt dates or the forecasting model's methodology and prediction horizon.

Therefore:
- Forecast errors will be measured, but the underlying forecasting model cannot be evaluated completely.
- Inventory-demand gaps will be investigated as indicators, not confirmed stock-outs or overstock.
- Category and region will be treated as recorded row-level attributes because their mappings to product IDs and store IDs are not consistent.
- Relationships between variables will not automatically be interpreted as causal effects.

## 7. Analytical Approach

The project will follow an evidence-first approach:

1. Understand and validate the dataset.
2. Define business KPIs.
3. Identify potential problems through exploratory analysis.
4. Investigate patterns using SQL and Python.
5. Build Power BI dashboards to communicate findings.
6. Develop practical recommendations supported by the analysis.