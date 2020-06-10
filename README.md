# Stock Fundamental Analysis (Value Investing)
## Purpose
The purpose of this project is to create a streamlined method of analyzing a stock. The main objectives are to determine if a stock is a 'value' stock and then to estimate if it is currently over or under-priced. There are multiple functions that are streamlined into one master or pagination function allowing the input of a list of stocks and a return of all the information. The indicators are primarily based off of Sean Seah's book "Gone Fishing with Buffett".
## Process
### Data Pull & Clean
Stock Price information pulled from Yahoo! using Pandas Datareader. <br />
Financial Statement information scraped from MarketWatch. <br />
The information is then compiled, cleaned and critical financial ratios are computed and stored in a dataframe.
### Metrics (Warning Filter Function)
Used to determine if stock would be categorized as a "Value" stock or not. <br />
Metrics used are:
- EPS (Earnings per Share)
- ROE (Return on Equity)
- ROA (Return on Assets)
- Long Term Debt vs. Net Income
- Interest Coverage Ratio
- PEG Ratio
### Estimated Price
A future price is estimated and compared to the current price. A 'Buy' or 'Sell' response is returned based upon the results.
## Moving Forward
Industry information would be included to get a better understanding of the company because a lot of these ratios can vary and have different norms based upon what the company does. <br />
Financial Statement scraper function could use some improvement. I tested it on all S&P500 stocks and it was able to work on ~85% of them. The other ~15% it did not work on because their statements were formatted differently. A more flexible scraper would be a great improvement.

