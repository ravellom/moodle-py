import pandas as pd
import datetime


def load_data(uploaded_file):
    df = pd.read_csv(uploaded_file)
    df = df.rename(columns={
                    'Hora': 'DT',
                    'Nombre completo del usuario': 'Name',
                    'Usuario afectado': 'User_afec',
                    'Contexto del evento': 'Context',
                    'Componente': 'Component',
                    'Nombre evento': 'Event',
                    'Descripción': 'Description',
                    'Origen': 'Origen',
                    'Dirección IP': 'IP',
                })
    df = df.loc[df["Name"] != "-"]
    df = descom_fecha(df)
    return df


def descom_fecha(df):
    # extraer fecha
    df['datefull'] = pd.to_datetime(df['DT'])
    # Date
    df['date']= df['datefull'].dt.date
    df['year']= df['datefull'].dt.year
    df['month']= df['datefull'].dt.month
    df['day']= df['datefull'].dt.day
    # Time
    df['hour']= df['datefull'].dt.hour
    # Weekday
    df['wd'] = df['date'].map(lambda x: x.weekday())
    return df