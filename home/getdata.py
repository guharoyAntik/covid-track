import requests
import pandas as pd
from io import StringIO

CSV_URL = "https://api.covid19india.org/csv/latest/state_wise.csv"

with requests.Session() as s:
    download = s.get(CSV_URL)
    
    decoded_content = download.content.decode('utf-8')
    data = StringIO(decoded_content)
    
    df = pd.read_csv(data)


def states_report():
    return df
