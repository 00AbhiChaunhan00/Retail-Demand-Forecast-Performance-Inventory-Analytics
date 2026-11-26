
  
    

  create  table
    "supply_chain"."analytics"."dim_product__dbt_tmp"
    
    
    
  as (
    SELECT DISTINCT
    product_id
FROM "supply_chain"."analytics"."stg_supply_chain"
  );
  