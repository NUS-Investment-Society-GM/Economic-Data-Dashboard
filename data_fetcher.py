import pandas_datareader.data as web
from datetime import datetime
import pandas as pd
code_dict={'Continued Claims':'CCSA'}
def fetch_from_FRED(name,start_date, end_date):
    if not start_date:
        start_date = '2015-01-01'
    if not end_date:
        end_date = datetime.now().strftime('%Y-%m-%d') #today
    # name, code = 'Continued Claims', 'CCSA'
    if name not in code_dict.keys():
        return pd.DataFrame()
    else:
        code=code_dict[name]
    df = web.DataReader(code, 'fred', start_date, end_date)
    df.columns = [name]
    return df

start_date = '2015-01-01'
end_date = datetime.now().strftime('%Y-%m-%d') 
