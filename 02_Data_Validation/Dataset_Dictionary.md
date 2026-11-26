# Dataset Dictionary

## 1. Dataset Overview

| Attribute | Details |
|---|---|
| Dataset | Retail Store Inventory Forecasting |
| Total Records | 73,100 |
| Total Columns | 15 |
| Date Range | 2022-01-01 to 2024-01-01 |
| Unique Dates | 731 |
| Stores | 5 |
| Products | 20 |
| Record Grain | Date × Store ID × Product ID |

## 2. Column Definitions

| Column | Business Meaning | Expected Analytical Type |
|---|---|---|
| date | Date associated with the inventory and sales record | DATE |
| store_id | Identifier of the store | VARCHAR |
| product_id | Identifier of the product | VARCHAR |
| category | Recorded product category | VARCHAR |
| region | Recorded store region | VARCHAR |
| inventory_level | Inventory quantity recorded for the product and store on that date | INTEGER |
| units_sold | Actual units sold during the recorded period | INTEGER |
| units_ordered | Units ordered for replenishment or inventory supply | INTEGER |
| demand_forecast | Forecasted demand for the recorded product and store | INTEGER |
| price | Recorded selling price of the product | DECIMAL |
| discount | Discount value recorded for the product | DECIMAL |
| weather_condition | Weather condition recorded for the date and location | VARCHAR |
| holiday_promotion | Indicator of holiday or promotional activity | VARCHAR / BOOLEAN |
| competitor_pricing | Recorded competitor price | DECIMAL |
| seasonality | Seasonality label recorded in the dataset | VARCHAR |

Note: Expected analytical types are logical types for analysis. Verify actual source data types before finalizing the schema documentation.

## 3. Dataset Grain

One record represents:

**One date + one store + one product.**

For example, a record represents the inventory, sales and forecast information for a particular product at a particular store on a particular date.

The expected unique key is:

`date + store_id + product_id`

## 4. Important Analytical Fields

### Actual Demand
- `units_sold`
- Represents actual recorded sales.
- Used as the actual-demand measure in forecast comparisons.

### Forecasted Demand
- `demand_forecast`
- Represents the forecasted demand.
- Compared against actual units sold.

### Inventory and Ordering
- `inventory_level`
- `units_ordered`
- Used to investigate recorded inventory and ordering patterns.

### Grouping Attributes
- `store_id`
- `product_id`
- `category`
- `region`

Used to compare forecast performance across recorded groups.

### Additional Variables
- `price`
- `discount`
- `weather_condition`
- `holiday_promotion`
- `competitor_pricing`
- `seasonality`

Used for exploratory analysis of possible associations with sales and forecast errors.

## 5. Data Interpretation Limitations

- Product IDs do not have a consistent one-to-one mapping with categories.
- Store IDs do not have a consistent one-to-one mapping with regions.
- Therefore, category and region must be treated as recorded row-level attributes, not permanent product or store master attributes.
- The dataset does not establish whether inventory is opening stock, closing stock or average stock.
- The exact definition of units_ordered is not independently verified.
- The forecast generation method and prediction horizon are not available.
- Seasonality labels must be validated before interpreting them as actual calendar seasons.

## 6. Validation Status

The dataset structure and record grain have been reviewed.

Detailed checks for missing values, duplicates, data types, value ranges and inconsistent mappings will be documented separately in `Data_Quality_Report.md`.