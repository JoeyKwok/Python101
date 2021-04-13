import lxml.etree as ET
import sqlite3
import pandas as pd
from yattag import indent

#################################################################################
# Build up connection with DB
conn = sqlite3.connect('joinrelation.db')

# Import data from DB by SQL as dataframe
df = pd.read_sql(f"SELECT * FROM DNS_column LIMIT 20", con = conn)

#################################################################################
# Loop through the DB data to build xml tree, and output as xml
# E.g.   <map key="[c1728053552(t_f05_dns_m1728053448)]" value="[t_f05_dns_m1728053448].[c1728053552]"/>

cols = ET.fromstring("<cols></cols>")
for index, row in df.iterrows():

    cols.append(ET.fromstring(
        f"<map key='[{row['tds_column_name'].rstrip()}({row['tds_table_name'].split('.')[1]})]' value='[{row['tds_table_name'].split('.')[1]}].[{row['tds_column_name'].rstrip()}]' />"))

xmlstr = ET.tostring(cols, encoding='utf8', method='xml').decode()
xmlstr = indent(xmlstr)
print(xmlstr)

with open(f"Asm7.xml", "w") as f:
    f.write(xmlstr)