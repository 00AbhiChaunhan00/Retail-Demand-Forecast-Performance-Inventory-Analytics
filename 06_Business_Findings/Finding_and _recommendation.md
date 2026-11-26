# Project 3 – Business Questions, Findings & Recommendations
## Interview Quick Notes

**Project:** Retail Demand, Forecast Performance & Inventory Analytics

### 1. Is the demand forecast overestimating actual demand?

**Finding:** Yes. Total forecast was around **10.35M units**, while actual demand was around **9.98M units**. This created a positive forecast bias of **3.71%** and WAPE of **6.09%**.

**Recommendation:** Review the forecasting process and test a bias correction using historical data before applying it to future forecasts.

### 2. Is overforecasting happening regularly or only in a few months?

**Finding:** It is a recurring pattern. The monthly forecast error stayed positive across 2022–2023. In Python, all **731 daily average errors** were positive, and the statistical test supported a positive average forecast error.

**Recommendation:** Monitor forecast bias and WAPE every month, and investigate months where the error increases.

### 3. Which products or store–product combinations have higher forecast errors?

**Finding:** The issue is widespread. All **20 products** and all **100 store–product combinations** had positive average forecast errors. Product P0018 had the highest product-level bias (**3.94%**); S001–P0001 had the highest average error among the combinations shown (**5.80 units**).

**Recommendation:** Start reviewing the highest-error products and store–product combinations, but continue monitoring the full range because the bias is not limited to a few items.

### 4. Is most of the forecast error coming from a small number of products?

**Finding:** No. The top five products contributed only **25.31%** of total absolute forecast error, while the top ten contributed **50.36%**. The error was spread fairly evenly across the 20 products.

**Recommendation:** Do not focus only on one or two products. Improve the overall forecasting process and use product-level rankings to decide where to investigate first.

### 5. Do weather, promotions, or seasons explain the higher forecast error?

**Finding:** No clear driver was identified. Forecast performance was very similar across promotion and non-promotion periods. WAPE differences were also small across weather conditions (**6.03%–6.14%**) and seasons (**6.01%–6.16%**).

**Recommendation:** Do not change the forecast model based on these small differences alone. Keep monitoring these factors and test them further if stronger evidence appears.

### 6. Do the inventory results show a possible planning issue?

**Finding:** The dashboard showed an average recorded inventory of **274.48 units** and an average inventory-versus-forecast gap of **132.95 units**. Units ordered were also lower than total units sold. These are signals worth investigating, but the available data does not confirm actual stockouts or overstock.

**Recommendation:** Collect opening and closing stock, stock receipts, supplier lead times, safety stock, and stockout records. Then measure inventory cover and confirmed stockout or excess-stock events.

---

## Overall Conclusion

The main finding was that the demand forecast consistently overestimated actual demand. The overall bias was **+3.71%**, and the pattern appeared across months, products, and store–product combinations. Weather, promotions, and seasonality did not show a clear explanation for the issue. Inventory indicators suggested areas for further investigation, but more operational data was needed to confirm stock problems.

## Final Business Recommendation

I would recommend reviewing and backtesting the forecasting process to reduce the consistent overestimation, monitoring forecast bias at product–store level every month, and improving inventory data before making stock-related decisions.

---

## Short Interview Answer

“The main business problem was the gap between forecasted demand and actual sales. I found that the forecast was consistently overestimating demand by around 3.71%. This pattern appeared across the observed months, products, and store–product combinations. I also checked weather, promotions, and seasonality, but none showed a major difference in forecast performance. My recommendation was to review and backtest the forecasting process, monitor forecast bias at product–store level, and collect better inventory movement data before concluding that stockouts or overstock were happening.”
