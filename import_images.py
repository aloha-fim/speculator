import psycopg2
import pandas as pd

conn = psycopg2.connect("host=localhost dbname=speculator_db user=postgres")
cur = conn.cursor()

df_condos = pd.read_csv("static/data/condo_images.csv", sep='|', index_col=False)
for idx, c in df_condos.iterrows():
    cur.execute(
        '''INSERT INTO photos (mlsnum, imgnum, features) VALUES (%s,%s,%s)''',
        (c.MLSNUM, c.IMGNUM, c.FEATURES)
    )
    conn.commit()

cur.close()
conn.close()
