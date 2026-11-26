# Data Quality Validation Report

## 1. Dataset Overview

- Total records: 73,100
- Total columns: 15
- Expected columns: 15
- Missing expected columns: []
- Unexpected columns: []
- Date range: 2022-01-01 00:00:00 to 2024-01-01 00:00:00
- Unique dates: 731

## 2. Missing Values

| Column | Missing Values |
|---|---:|
| date | 0 |
| store_id | 0 |
| product_id | 0 |
| category | 0 |
| region | 0 |
| inventory_level | 0 |
| units_sold | 0 |
| units_ordered | 0 |
| demand_forecast | 0 |
| price | 0 |
| discount | 0 |
| weather_condition | 0 |
| holiday_promotion | 0 |
| competitor_pricing | 0 |
| seasonality | 0 |

## 3. Duplicate Checks

- Fully duplicated rows: 0
- Duplicate date-store-product keys: 0

## 4. Unique Entity Counts

| Attribute | Unique Values |
|---|---:|
| store_id | 5 |
| product_id | 20 |
| category | 5 |
| region | 4 |

## 5. Mapping Consistency

- Product IDs appearing with multiple categories: 20
- Store IDs appearing with multiple regions: 5

## 6. Data Types

| Column | Data Type |
|---|---|
| date | str |
| store_id | str |
| product_id | str |
| category | str |
| region | str |
| inventory_level | int64 |
| units_sold | int64 |
| units_ordered | int64 |
| demand_forecast | float64 |
| price | float64 |
| discount | int64 |
| weather_condition | str |
| holiday_promotion | int64 |
| competitor_pricing | float64 |
| seasonality | str |

## 7. Numeric Value Checks

| Column | Invalid Values | Negative Values |
|---|---:|---:|
| inventory_level | 0 | 0 |
| units_sold | 0 | 0 |
| units_ordered | 0 | 0 |
| demand_forecast | 0 | 0 |
| price | 0 | 0 |
| discount | 0 | 0 |
| competitor_pricing | 0 | 0 |

## 8. Validation Notes

- These checks identify structural and value-quality issues.
- Negative values require business-context review; they are not automatically treated as errors.
- Product-category and store-region mappings are checked for consistency, not assumed to be master-data relationships.
- Forecast methodology and inventory measurement definitions cannot be verified from these checks alone.

## 9. Overall Data Quality Assessment

### Passed Checks

- Dataset contains 73,100 records and 15 columns.
- No missing values were identified.
- No fully duplicated records were identified.
- No duplicate date-store-product business keys were identified.
- No invalid dates were identified.
- No invalid or negative values were identified in the checked numeric columns.
- Dataset covers the period from 2022-01-01 to 2024-01-01.

### Data Modeling Issue

- All 20 product IDs appear with multiple recorded categories.
- All 5 store IDs appear with multiple recorded regions.
- Product-category and store-region relationships cannot be treated as fixed one-to-one mappings.
- Category and region will therefore remain attributes in the fact table rather than attributes of the product and store dimensions.

### Final Assessment

The dataset passed the structural checks performed in this validation exercise. However, passing these checks does not guarantee that every business field is semantically accurate.

The inconsistent entity mappings require careful treatment during data modeling. Further business-context validation is also required for inventory definitions, ordering information and forecast methodology.

The dataset is suitable for descriptive demand-versus-forecast analysis, subject to the documented limitations.