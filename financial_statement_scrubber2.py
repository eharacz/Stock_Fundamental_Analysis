def financial_scrubber(list):
    """creates a dataframe of stock essential financal information and ratios"""
    for ticker in list:
        try:
            inc_st = pd.read_html(f'https://www.marketwatch.com/investing/stock/{ticker}/financials')
            income_state = pd.DataFrame(inc_st[1])
            income_state = income_state.transpose()
            new_header = income_state.iloc[0]
            income_state = income_state[1:]
            income_state.columns = new_header
            eps = income_state['EPS (Basic)']
            eps = eps.to_frame()
            eps_growth = income_state['EPS (Basic) Growth']
            eps_growth = eps_growth.to_frame()
            net_income =  income_state['Net Income']
            net_income = net_income.to_frame()
            interest_expense = income_state['Interest Expense']
            interest_expense = interest_expense.to_frame()
            EBITDA = income_state['EBITDA']
            EBITDA = EBITDA.to_frame()
            #
            outstanding_shares = income_state['Basic Shares Outstanding']
            outstanding_shares = outstanding_shares.to_frame()
            ebitda_growth_rate = income_state['EBITDA Growth']
            ebitda_growth_rate = ebitda_growth_rate.to_frame()
            #
            i_s=eps.join(eps_growth)
            i_s = i_s.join(net_income)
            i_s = i_s.join(interest_expense)
            i_s = i_s.join(EBITDA)
            #
            i_s = i_s.join(outstanding_shares)
            i_s = i_s.join(ebitda_growth_rate)
            #
            i_s = i_s.rename(columns={'EPS (Basic)':'eps', 'EPS (Basic) Growth':'eps_growth', 'Net Income': 'net_income', 'Interest Expense': 'interest_expense', 'EBITDA': 'ebitda', 'Basic Shares Outstanding': 'outstanding_shares', 'EBITDA Growth':'ebitda_growth_rate'})
            i_s=i_s.drop('5-year trend')


            bal_sh= pd.read_html(f'https://www.marketwatch.com/investing/stock/{ticker}/financials/balance-sheet')
            balance_sheet1 = pd.DataFrame(bal_sh[1])
            balance_sheet1 = balance_sheet1.transpose()
            balance_sheet2 = pd.DataFrame(bal_sh[2])
            balance_sheet2 = balance_sheet2.transpose()
            new_header1 = balance_sheet1.iloc[0]
            balance_sheet1 = balance_sheet1[1:]
            balance_sheet1.columns = new_header1
            new_header2 = balance_sheet2.iloc[0]
            balance_sheet2 = balance_sheet2[1:]
            balance_sheet2.columns = new_header2
            shareholder_equity = balance_sheet2["Total Shareholders' Equity"]
            shareholder_equity = shareholder_equity.to_frame()
            longterm_debt = balance_sheet2["Long-Term Debt"]
            longterm_debt = longterm_debt.to_frame()
            total_assets = balance_sheet1["Total Assets"]
            total_assets = total_assets.to_frame()
            b_s=shareholder_equity.join(longterm_debt)
            b_s = b_s.join(total_assets)
            b_s = b_s.rename(columns={"Total Shareholders' Equity":'shareholder_equity', 'Long-Term Debt':'longterm_debt', "Total Assets": 'total_assets'})
            b_s=b_s.drop('5-year trend')

            financials=i_s.merge(b_s, left_index=True, right_index=True)

            financials['net_income']= financials['net_income'].apply(lambda x: x.replace('.', ''))
            financials['net_income']= financials['net_income'].apply(lambda x: x.replace('B', '0000000'))
            financials['net_income']= financials['net_income'].apply(lambda x: x.replace('M', '000000'))
            financials['interest_expense']= financials['interest_expense'].apply(lambda x: x.replace('.', ''))
            financials['interest_expense']= financials['interest_expense'].apply(lambda x: x.replace('B', '0000000'))
            financials['interest_expense']= financials['interest_expense'].apply(lambda x: x.replace('M', '000000'))
            financials['ebitda']= financials['ebitda'].apply(lambda x: x.replace('.', ''))
            financials['ebitda']= financials['ebitda'].apply(lambda x: x.replace('B', '0000000'))
            financials['ebitda']= financials['ebitda'].apply(lambda x: x.replace('M', '000000'))
            financials['shareholder_equity']= financials['shareholder_equity'].apply(lambda x: x.replace('.', ''))
            financials['shareholder_equity']= financials['shareholder_equity'].apply(lambda x: x.replace('B', '0000000'))
            financials['shareholder_equity']= financials['shareholder_equity'].apply(lambda x: x.replace('M', '000000'))
            financials['longterm_debt']= financials['longterm_debt'].apply(lambda x: x.replace('.', ''))
            financials['longterm_debt']= financials['longterm_debt'].apply(lambda x: x.replace('B', '0000000'))
            financials['longterm_debt']= financials['longterm_debt'].apply(lambda x: x.replace('M', '000000'))
            financials['total_assets']= financials['total_assets'].apply(lambda x: x.replace('.', ''))
            financials['total_assets']= financials['total_assets'].apply(lambda x: x.replace('B', '0000000'))
            financials['total_assets']= financials['total_assets'].apply(lambda x: x.replace('M', '000000'))
            #
            financials['outstanding_shares']= financials['outstanding_shares'].apply(lambda x: x.replace('.', '')) #
            financials['outstanding_shares']= financials['outstanding_shares'].apply(lambda x: x.replace('B', '0000000')) #
            financials['outstanding_shares']= financials['outstanding_shares'].apply(lambda x: x.replace('M', '000000')) #
            financials['ebitda_growth_rate']= financials['ebitda_growth_rate'][1:].apply(lambda x:x.replace('%','')) #

            #financials = financials.apply(lambda x: x.replace('-', 0))#np.nan
            financials = financials.apply(lambda x: x.str.replace('(', '-'))
            financials = financials.apply(lambda x: x.str.strip(')'))
            financials = financials.apply(lambda x: x.replace('-', 0))

            financials['eps_growth'] = financials['eps_growth'].astype(float)
            financials['eps'] = financials['eps'].astype(float)
            financials['net_income'] = financials['net_income'].astype(int)
            financials['interest_expense'] = financials['interest_expense'].astype(int)
            financials['ebitda'] = financials['ebitda'].astype(int)
            financials['shareholder_equity'] = financials['shareholder_equity'].astype(int)
            financials['longterm_debt'] = financials['longterm_debt'].astype(int)
            financials['total_assets'] = financials['total_assets'].astype(int)
            #
            financials['outstanding_shares']=financials['outstanding_shares'].astype(int) #
            financials['ebitda_growth_rate']=financials['ebitda_growth_rate'][1:].astype(float) #

            stock_pricing = data_pull(f'{ticker}') #
            stock_price = stock_pricing['Close'] #
            stock_price = stock_price[0]  #

            financials['roa']=financials['net_income']/financials['total_assets']
            financials['roe']=financials['net_income']/financials['shareholder_equity']
            financials['interestcoverageratio']=financials['ebitda']/financials['interest_expense']

            #
            financials['pe']=stock_price/financials['eps'][4] #
            financials['pb']=stock_price/(financials['shareholder_equity'][4]/financials['outstanding_shares'][4]) #
            #financials['gbm']=financials['pe']*financials['pb'] #
            financials['peg']=financials['pe']/financials['ebitda_growth_rate'][1:].mean() #
            financials['pe'][0:4]=np.nan #
            financials['pb'][0:4]=np.nan #
            financials['peg'][0:4]=np.nan #
            #print(financials)

            financials = financials.apply(lambda x: x.replace(0, np.nan))
            financials = financials.apply(lambda x: x.replace(np.inf, np.nan))

            financials['ticker'] = f'{ticker}'
            print(ticker)
            financials_list.append(financials)
        except:
            trouble_stocks.append(ticker)
