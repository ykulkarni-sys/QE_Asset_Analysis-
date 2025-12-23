# Quantitative Easing and Asset Prices

## Project Overview
This project analyzes the effects of U.S. Federal Reserve quantitative easing (QE) on financial markets by examining the relationship between central bank balance sheet expansion and asset prices. Using publicly available Federal Reserve Economic Data (FRED), the project studies how large-scale asset purchases transmit to long-term interest rates, equity markets, and housing prices.

The objective is to empirically evaluate whether expansions in the Federal Reserve’s balance sheet are associated with lower long-term yields and higher asset prices, consistent with standard monetary policy transmission mechanisms.

---

## Economic Motivation
When short-term interest rates reach the zero lower bound, central banks turn to non-conventional monetary policy tools such as quantitative easing. By purchasing long-term Treasury securities and mortgage-backed securities, the Federal Reserve increases demand for these assets, raising their prices and lowering their yields. Lower long-term interest rates are expected to ease financial conditions, encourage portfolio rebalancing toward riskier assets, and stimulate aggregate demand through investment, consumption, and wealth effects.

This project empirically tests these mechanisms using macro-financial time-series data.

---

## Data
All data are sourced from the Federal Reserve Economic Data (FRED) database:

- WALCL: Federal Reserve total assets (proxy for QE intensity)
- DGS10: 10-Year Treasury constant maturity yield
- SP500: S&P 500 index
- CSUSHPINSA: Case-Shiller U.S. National Home Price Index

The data are cleaned, aligned, and analyzed at a consistent frequency.

---

## Methodology
The analysis proceeds in the following steps:

1. Collection of raw macro-financial time series using the FRED API  
2. Visualization of raw and normalized data to examine co-movement  
3. Correlation analysis to measure linear relationships between QE and asset prices  
4. Regression analysis using lagged QE variables to study dynamic transmission effects  
5. Statistical inference using coefficient estimates and p-values  

Both levels and changes in variables are examined to improve interpretability and reduce non-stationarity concerns.

---

## Key Findings
- Expansions in the Federal Reserve’s balance sheet are positively associated with equity and housing prices.
- The relationship between QE and long-term Treasury yields is weaker and statistically insignificant, consistent with mixed empirical findings in the literature.
- Lagged regressions suggest QE effects on asset prices may materialize with delays rather than immediately.

---

## Tools and Skills Demonstrated
- Python (pandas, numpy, matplotlib, statsmodels)
- Time-series data analysis
- Econometric modeling and interpretation
- Macroeconomic and financial theory
- Data visualization and communication of results

---

## How to Run
1. Obtain a FRED API key from the Federal Reserve Bank of St. Louis
2. Store the API key locally or as an environment variable (not included in this repository)
3. Run the notebook or Python script from top to bottom

---

## Notes
API keys are intentionally excluded from this repository for security reasons.

---

## Author
Yodha Kulkarni  
Economics & Data Analytics Student  
Interests: Monetary Policy, Financial Markets, Applied Econometrics, Data Science
