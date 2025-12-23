import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from fredapi import Fred

fred = Fred(api_key='your_fred_api_key')

walcl = fred.get_series('WALCL')
dgs10 = fred.get_series('DGS10')
sp500 = fred.get_series('SP500')
housing = fred.get_series('CSUSHPINSA')

data = pd.DataFrame({
    'WALCL': walcl,
    'DGS10': dgs10,
    'SP500': sp500,
    'Housing': housing
})
data.index = pd.to_datetime(data.index)
data.head()

data.ffill(inplace=True)
data = data.resample('ME').last()
data.info()

data_norm = (data - data.min()) / (data.max() - data.min())

plt.figure(figsize=(12,6))
for col in ['WALCL','SP500','Housing']:
    plt.plot(data_norm.index, data_norm[col], label=col)
plt.title('Normalized Data')
plt.legend()
plt.show()
plt.close()

corr = data_norm[['WALCL', 'DGS10', 'SP500', 'Housing']].corr()
print(corr)

plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Matrix of Normalized Series')
plt.show()

df = data.copy()

df['dWALCL'] = df['WALCL'].pct_change()
df['dSP500'] = df['SP500'].pct_change()
df['dHousing'] = df['Housing'].pct_change()
df['dDGS10'] = df['DGS10'].diff()

df = df.dropna()

df['dWALCL_lag1'] = df['dWALCL'].shift(1)
df['dWALCL_lag3'] = df['dWALCL'].shift(3)
df['dWALCL_lag6'] = df['dWALCL'].shift(6)

df = df.dropna()

import statsmodels.api as sm

X = sm.add_constant(df[['dWALCL_lag1', 'dWALCL_lag3', 'dWALCL_lag6']])

results = {}

for var in ['dSP500', 'dDGS10', 'dHousing']:
    model = sm.OLS(df[var], X).fit()
    results[var] = model
    print(f'\nRegression results for {var}\n')
    print(model.summary())

outcomes = ['dSP500', 'dDGS10', 'dHousing']
lags = ['dWALCL_lag1', 'dWALCL_lag3', 'dWALCL_lag6']

summary_table = pd.DataFrame(columns=pd.MultiIndex.from_product([outcomes, ['coef', 'pval']]))

for var in outcomes:
    model = sm.OLS(df[var], X).fit()
    for lag in lags:
        summary_table.loc[lag, (var, 'coef')] = model.params[lag]
        summary_table.loc[lag, (var, 'pval')] = model.pvalues[lag]

summary_table

lags = ['dWALCL_lag1', 'dWALCL_lag3', 'dWALCL_lag6']
markets = ['dSP500', 'dDGS10', 'dHousing']

plt.figure(figsize=(10,6))

for market in markets:
    coefs = [summary_table.loc[lag, (market, 'coef')] for lag in lags]
    plt.plot([1,3,6], coefs, marker='o', label=market)

plt.xticks([1,3,6], ['1 Month', '3 Months', '6 Months'])
plt.xlabel('QE Lag')
plt.ylabel('Coefficient on Market')
plt.title('Lagged Effect of QE on Different Markets')
plt.legend()
plt.grid(True)
plt.show()

display_table = summary_table.copy()
display_table = display_table.round(3)

def highlight_significant(val, pval):
    if pval < 0.05:
        return f"{val}*"
    return str(val)

for market in ['dSP500', 'dDGS10', 'dHousing']:
    for lag in display_table.index:
        coef = display_table.loc[lag, (market, 'coef')]
        pval = display_table.loc[lag, (market, 'pval')]
        display_table.loc[lag, (market, 'coef')] = highlight_significant(coef, pval)

print(display_table)