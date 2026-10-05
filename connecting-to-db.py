import sqlite3
import pandas as pd

conn = sqlite3.connect("data.sqlite")

cur = conn.cursor()

cur.execute("""SELECT name FROM sqlite_master WHERE type = 'table';""")

table_names = cur.fetchall()

table_names  # returns list of table columns

cur.execute("""SELECT * FROM offices;""")

cur.fetchall()

cur.description  # contains information about the offices table

# generate dataframe with the right column names, using pandas

pd.DataFrame(
    data=cur.execute("""SELECT * FROM offices;""").fetchall(),
    columns=[x[0] for x in cur.description],
)

# close connection
conn.close()

# using pandas intead of cursor

df = pd.read_sql("""SELECT name FROM sqlite_master WHERE type = 'table';""", conn)
df
