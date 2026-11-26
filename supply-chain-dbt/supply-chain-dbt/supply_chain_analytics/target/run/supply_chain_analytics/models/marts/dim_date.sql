
  
    

  create  table
    "supply_chain"."analytics"."dim_date__dbt_tmp"
    
    
    
  as (
    SELECT DISTINCT
    date,

    EXTRACT(DAY FROM date) AS day,
    EXTRACT(MONTH FROM date) AS month,
    TO_CHAR(date, 'Month') AS month_name,
    EXTRACT(QUARTER FROM date) AS quarter,
    EXTRACT(YEAR FROM date) AS year,

    TO_CHAR(date, 'YYYY-MM') AS year_month,
    TO_CHAR(date, 'Mon-YY') AS month_year,

    EXTRACT(DOW FROM date) AS day_of_week,
    TO_CHAR(date, 'Day') AS day_name,

    CASE
        WHEN EXTRACT(DOW FROM date) IN (0, 6)
        THEN 'Weekend'
        ELSE 'Weekday'
    END AS day_type

FROM "supply_chain"."analytics"."stg_supply_chain"
  );
  