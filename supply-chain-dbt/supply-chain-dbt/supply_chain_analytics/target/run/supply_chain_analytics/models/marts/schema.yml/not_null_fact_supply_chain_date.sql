
    
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select date
from "supply_chain"."analytics"."fact_supply_chain"
where date is null



  
  
      
    ) dbt_internal_test