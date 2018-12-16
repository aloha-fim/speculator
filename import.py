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


df_images = pd.read_csv("static/data/condo_images.csv", sep='|', index_col=False)
for idx, c in df_images.iterrows():
    cur.execute(
        '''INSERT INTO photos (mlsnum, imgnum, features) VALUES (%s,%s,%s)''',
        (c.MLSNUM, c.IMGNUM, c.FEATURES)
    )
    conn.commit()


cur.execute(
    '''DELETE FROM condos WHERE mlsnum NOT IN (SELECT mlsnum FROM photos)'''
)
conn.commit()

cur.close()
conn.close()
