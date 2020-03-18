def data_pull(tick):
    now = datetime.datetime.now()
    start_year = int(now.strftime('%Y'))#-10
    end_year = int(now.strftime('%Y'))
    day = int(now.strftime('%d'))
    month = int(now.strftime('%m'))
    start = datetime.datetime(start_year, month, day)
    end = datetime.datetime(end_year, month, day)
    #start = datetime.datetime(2010, 1, 1)
    #end = datetime.datetime(2019, 12, 31)

    df = web.DataReader(f'{tick}', 'yahoo', start, end)
    df['Company']= f'{tick}'
    return df

def stock_list_pull(list):
    stock_df_list = []
    for t in ticker_list:
        print(t)
        tick = f'{t}'
        stock = data_pull(f'{t}')
        stock_df_list.append(stock)
        time.sleep(1)
    return stock_df_list
