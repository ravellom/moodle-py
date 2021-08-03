import pandas as pd
import datetime


def load_data(uploaded_file):
    #df = pd.read_csv(uploaded_file[0])
    csv_to_read = [pd.read_csv(f) for f in uploaded_file]
    df = pd.concat(csv_to_read)
    
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
    #df = df.set_index('DT')
    return df


def descom_fecha(df):
    # extraer fecha
    df['datefull'] = pd.to_datetime(df['DT'], format="%d/%m/%Y %H:%M", dayfirst=True)
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
