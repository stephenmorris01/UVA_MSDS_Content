import json
import pandas as pd

def extract_the_data():
    jsonfile = r"D:\Git\UVA_MSDS_Content\STAT_6021_Linear_Models\BlueNileDiamonds.json"

    with open(jsonfile, "r") as f:
        jsonfile = json.load(f)

    jsonfile = jsonfile['results']

    df = pd.DataFrame(jsonfile)

    df['cut1'] = df['cut'].str.extract(r"'label': '(.*?)',")
    df['meas'] = df['measurements'].astype(str).str.extract(r"'label': '(.*?)',")
    df[['measure1', 'measure2', 'measure3']] = df['meas'].str.split(' x ',expand=True) 
    df['measure3'] = df['measure3'].str.replace(' mm', '')
    df = df.drop(columns=['cut', 'measurements', 'meas'])

    #df = df.apply(lambda x: x[0] if isinstance(x, list) else x.replace('[', '').replace(']', ''))

    print(df.head())

    df.to_csv(r"D:\Git\UVA_MSDS_Content\STAT_6021_Linear_Models\diamond_df1.csv")

