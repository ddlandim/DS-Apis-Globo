import pandas as pd
from datetime import datetime

def read_inv(file_inv):
    #file_inv = '../Data/tvaberta_inventory_availability.csv(1).csv'
    dateparser_inv = lambda x: datetime.strptime(x, '%d/%m/%Y')
    sep_inv = ';'
    parsedates_inv = ['date']
    df_inv = pd.read_csv(file_inv,
                         sep=sep_inv,
                         parse_dates=parsedates_inv,
                         date_parser=dateparser_inv)
    df_inv['weekday'] = df_inv.date.dt.dayofweek
    df_inv['average_audience'] = -1
    df_inv['predicted_audience'] = -1
    return df_inv

def read_pro(file_pro):
    #file_pro = '../Data/tvaberta_program_audience(1).csv'
    dateparser_pro = lambda x: datetime.strptime(x, "%Y-%m-%dT%H:%M:%S.%fZ")
    sep_pro = ','
    parsedates_pro = ['program_start_time']
    indexcol_pro = 'program_start_time'
    df_pro = pd.read_csv(file_pro,
                         sep=sep_pro,
                         parse_dates=parsedates_pro,
                         date_parser=dateparser_pro)
    df_pro['exhibition_date'] = pd.to_datetime(df_pro['exhibition_date'], format='%Y-%m-%d')
    df_pro = df_pro.rename(columns={"exhibition_date": "date"})
    df_pro['weekday'] = df_pro.date.dt.dayofweek  
    df_pro['predicted_audience'] = -1
    df_pro['available_time'] = -1
    del df_pro['program_start_time']
    return df_pro

def median_window(df,target,window):
    if len(df[target])>0:
        df.sort_values(by=[target])
        fill = df[target].values[0]
        if window % 2 == 0:
            s1 = int(window / 2)
            s2 = int(window / 2) + 1
            laux1 = df[target].shift(s1,fill_value=fill)
            laux2 = df[target].shift(s2,fill_value=fill)
            return ((laux1 + laux2) / 2)
        else:
            s1 = int(window/2) + 1
            return df[target].shift(s1,fill_value=fill)

def df_predicted_audience(df):
    l_signal = df.signal.unique()
    for v_signal in l_signal:
        df_aux = df.loc[df['signal'] == v_signal]
        l_program_code = df_aux.program_code.unique()
        for v_program in l_program_code:
            df_aux = df.loc[(df['signal'] == v_signal) & (df['program_code'] == v_program)]
            l_weekdays = df_aux.weekday.unique()
            for v_day in l_weekdays:
                df_aux = df.loc[(df['weekday'] == v_day) & (df['signal'] == v_signal) & (
                            df['program_code'] == v_program)]
                df_aux.sort_values(by=['average_audience'])
                df_aux['predicted_audience'] = median_window(df_aux,'average_audience',4)
                df.predicted_audience.loc[df_aux.index] = df_aux['predicted_audience'].values
    return df