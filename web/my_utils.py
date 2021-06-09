import pandas as pd
import datetime

def descom_fecha(df):
    # extraer fecha
    df['datefull'] = pd.to_datetime(df['DT'])
    # Date
    df['year']= df['datefull'].dt.year
    df['month']= df['datefull'].dt.month
    df['day']= df['datefull'].dt.day
    # Time
    df['hour']= df['datefull'].dt.hour
    return df