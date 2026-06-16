# Egyptian Banking & Financial Inclusion Analysis
## Findings Report — 2011 to 2023

---

### Background

This report analyzes Egypt's banking sector and financial inclusion trends
between 2011 and 2023, with a focus on the impact of the Egyptian Pound
(EGP) float in November 2016. Data was sourced from the World Bank and
FRED, covering indicators including account ownership, inflation, GDP per
capita, exchange rate, and bank branches per 100,000 adults.

---

### Key Findings

**1. The 2016 EGP Float Was the Single Most Impactful Event**
Every indicator shows a clear inflection point at 2016. The exchange rate
collapsed from an average of 6.73 EGP/USD pre-2016 to 17.94 EGP/USD
post-2016 — a 167% depreciation. Inflation also rose from 9.42% to 15.61%
on average, the direct consequence of import costs rising after devaluation.

**2. Account Ownership More Than Doubled Post-Float**
Financial inclusion jumped from a pre-2016 mean of 13.61% to 29.0%
post-2016 — statistically significant (p = 0.0000). This reflects CBE
digital inclusion initiatives, mandatory payroll digitization, and the
expansion of mobile wallets like Meeza cards following the float.

**3. Bank Branch Density Increased Significantly**
Bank branches per 100k adults rose from 4.36 pre-2016 to 5.66 post-2016
(p = 0.0082), suggesting that despite economic pressure, banks expanded
their physical presence — possibly to capture the growing formally-banked
population.

**4. Exchange Rate Change Was Statistically Proven**
The EGP/USD shift from 6.73 to 17.94 is statistically significant
(p = 0.0014), confirming the float was a structural break, not a
gradual trend.

**5. Inflation and GDP Were Not Statistically Significant**
Despite inflation rising from 9.42% to 15.61% and GDP per capita shifting
from $3,010 to $3,267 USD, neither change was statistically provable
(p = 0.23 and p = 0.41 respectively), likely due to the small sample
size of 13 years limiting statistical power.

---

### Statistical Summary

| Indicator               | Pre-2016 Mean | Post-2016 Mean | P-Value | Significant? |
|-------------------------|---------------|----------------|---------|--------------|
| Account Ownership (%)   | 13.61         | 29.00          | 0.0000  | YES          |
| Inflation Rate (%)      | 9.42          | 15.61          | 0.2296  | NO           |
| GDP per Capita (USD)    | 3010.52       | 3267.75        | 0.4126  | NO           |
| Bank Branches per 100k  | 4.36          | 5.66           | 0.0082  | YES          |
| EGP/USD Exchange Rate   | 6.73          | 17.94          | 0.0014  | YES          |

---

### Limitations

- Sample size is small (13 years), reducing statistical power of t-tests
- Two World Bank indicators (bank capital, domestic credit) had no Egypt
  data and were dropped
- Account ownership data is surveyed only every 3 years by the World Bank
  (Findex), so interpolated values were used for missing years
- FRED exchange rate data uses annual averages, smoothing out intra-year
  volatility

---

### Data Sources

- World Bank Open Data (wbgapi) — account ownership, inflation, GDP,
  bank branches
- FRED St. Louis Fed — EGP/USD exchange rate
- Period: 2011–2023
- Country: Egypt (EGY)
