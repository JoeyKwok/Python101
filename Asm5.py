import re
import sqlite3
import pandas as pd

#################################################################################
# Build up connection with DB
conn = sqlite3.connect('joinrelation.db')
# create at the same location of this scripts if this doesn't exist


# Import data from DB by SQL as dataframe
df = pd.read_sql(f"SELECT * FROM DNS_Join LIMIT 20", con = conn)

# Create new columns in DB
if not 'NE' in df:
    conn.execute("ALTER TABLE DNS_Join ADD NE VARCHAR(100)")
if not 'Time_Granularity' in df:
    conn.execute("ALTER TABLE DNS_Join ADD Time_Granularity VARCHAR(100)")

# Find out the values of NE & Time_Granularity and insert to DB
for index, row in df.iterrows():
    x = re.search(r'^t_f([0-9]*)_(\w+)_', row['tds_name'])
    df.at[index, 'NE'] = x.group(2).upper()
    df.at[index, 'Time_Granularity'] = x.group(1)

df.to_sql(name ='DNS_Join', con = conn ,if_exists='replace', index = False)
