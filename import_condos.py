import psycopg2
import pandas as pd

conn = psycopg2.connect("host=localhost dbname=speculator_db user=postgres")
cur = conn.cursor()

df_condos = pd.read_csv("static/data/condos.csv", index_col=False, dtype={'ZIP': str})
for idx, c in df_condos.iterrows():
    try:
        cur.execute(
            '''INSERT INTO condos (mlsnum, zip, beds, baths, sqft, listprice, photourl) VALUES (%s,%s,%s,%s,%s,%s, %s)''',
            (c.MLSNUM, c.ZIP, c.BEDS, c.BATHS, c.SQFT, c.LISTPRICE, c.PHOTOURL)
        )
        conn.commit()
    except:
        pass

cur.close()
conn.close()
