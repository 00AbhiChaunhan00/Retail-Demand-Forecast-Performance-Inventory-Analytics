
import pandas as pd
from pathlib import Path

# 1. File paths
project_path = Path(r"C:\Users\Abhishek\Downloads\Resume_Project\Project 3")

csv_path = project_path / "project3_retail_inventory_validated.csv"
report_path = project_path / "02_Data_Validation" / "Data_Quality_Report.md"

# 2. Load dataset
df = pd.read_csv(csv_path)

# 3. Basic information
rows, columns = df.shape
expected_columns = [
    "date", "store_id", "product_id", "category", "region",
    "inventory_level", "units_sold", "units_ordered",
    "demand_forecast", "price", "discount",
    "weather_condition", "holiday_promotion",
    "competitor_pricing", "seasonality"
]

# 4. Missing values
missing = df.isnull().sum()

# 5. Duplicate checks
duplicate_rows = df.duplicated().sum()

key_columns = ["date", "store_id", "product_id"]
key_duplicates = df.duplicated(subset=key_columns).sum()

# 6. Date validation
dates = pd.to_datetime(df["date"], errors="coerce")
invalid_dates = dates.isna().sum()

valid_dates = dates.dropna()
date_min = valid_dates.min() if len(valid_dates) else "Not available"
date_max = valid_dates.max() if len(valid_dates) else "Not available"
unique_dates = valid_dates.nunique()

# 7. Unique values
unique_counts = {
    col: df[col].nunique(dropna=True)
    for col in [
        "store_id", "product_id", "category", "region"
    ]
}

# 8. Product-category and store-region mapping checks
product_category = (
    df.groupby("product_id")["category"].nunique()
    if {"product_id", "category"}.issubset(df.columns)
    else pd.Series(dtype=int)
)

store_region = (
    df.groupby("store_id")["region"].nunique()
    if {"store_id", "region"}.issubset(df.columns)
    else pd.Series(dtype=int)
)

products_multiple_categories = (
    (product_category > 1).sum()
)

stores_multiple_regions = (
    (store_region > 1).sum()
)

# 9. Data types
data_types = df.dtypes.astype(str)

# 10. Numeric validation
numeric_columns = [
    "inventory_level", "units_sold", "units_ordered",
    "demand_forecast", "price", "discount", "competitor_pricing"
]

numeric_results = {}

for col in numeric_columns:
    if col in df.columns:
        converted = pd.to_numeric(df[col], errors="coerce")
        invalid_count = (converted.isna() & df[col].notna()).sum()
        negative_count = (converted < 0).sum()

        numeric_results[col] = {
            "invalid_values": int(invalid_count),
            "negative_values": int(negative_count)
        }

# 11. Missing and unexpected columns
missing_columns = sorted(set(expected_columns) - set(df.columns))
unexpected_columns = sorted(set(df.columns) - set(expected_columns))

# 12. Build report
report = []

report.append("# Data Quality Validation Report\n")
report.append("## 1. Dataset Overview\n")
report.append(f"- Total records: {rows:,}")
report.append(f"- Total columns: {columns}")
report.append(f"- Expected columns: {len(expected_columns)}")
report.append(f"- Missing expected columns: {missing_columns}")
report.append(f"- Unexpected columns: {unexpected_columns}")
report.append(f"- Date range: {date_min} to {date_max}")
report.append(f"- Unique dates: {unique_dates}\n")

report.append("## 2. Missing Values\n")
report.append("| Column | Missing Values |")
report.append("|---|---:|")

for col, count in missing.items():
    report.append(f"| {col} | {count} |")

report.append("\n## 3. Duplicate Checks\n")
report.append(f"- Fully duplicated rows: {duplicate_rows}")
report.append(f"- Duplicate date-store-product keys: {key_duplicates}\n")

report.append("## 4. Unique Entity Counts\n")
report.append("| Attribute | Unique Values |")
report.append("|---|---:|")

for col, count in unique_counts.items():
    report.append(f"| {col} | {count} |")

report.append("\n## 5. Mapping Consistency\n")
report.append(
    f"- Product IDs appearing with multiple categories: "
    f"{products_multiple_categories}"
)
report.append(
    f"- Store IDs appearing with multiple regions: "
    f"{stores_multiple_regions}\n"
)

report.append("## 6. Data Types\n")
report.append("| Column | Data Type |")
report.append("|---|---|")

for col, dtype in data_types.items():
    report.append(f"| {col} | {dtype} |")

report.append("\n## 7. Numeric Value Checks\n")
report.append("| Column | Invalid Values | Negative Values |")
report.append("|---|---:|---:|")

for col, result in numeric_results.items():
    report.append(
        f"| {col} | {result['invalid_values']} | "
        f"{result['negative_values']} |"
    )

report.append("\n## 8. Validation Notes\n")
report.append(
    "- These checks identify structural and value-quality issues."
)
report.append(
    "- Negative values require business-context review; "
    "they are not automatically treated as errors."
)
report.append(
    "- Product-category and store-region mappings are checked "
    "for consistency, not assumed to be master-data relationships."
)
report.append(
    "- Forecast methodology and inventory measurement definitions "
    "cannot be verified from these checks alone."
)

report_path.write_text("\n".join(report), encoding="utf-8")

# 13. Print results
print("\n========== DATA QUALITY VALIDATION ==========")
print("Dataset shape:", df.shape)
print("Duplicate rows:", duplicate_rows)
print("Duplicate business keys:", key_duplicates)
print("Invalid dates:", invalid_dates)
print("Date range:", date_min, "to", date_max)
print("\nMissing values:\n", missing)
print("\nUnique counts:\n", unique_counts)
print("\nProducts with multiple categories:", products_multiple_categories)
print("Stores with multiple regions:", stores_multiple_regions)
print("\nNumeric checks:", numeric_results)
print("\nReport saved at:", report_path)
