
  
    

  create  table
    "supply_chain"."analytics"."dim_store__dbt_tmp"
    
    
    
  as (
    SELECT DISTINCT
    store_id
FROM "supply_chain"."analytics"."stg_supply_chain"
  );
  