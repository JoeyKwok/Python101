""" Please installs Db Broswer fro SQLite to simulate the DB environment in local PC.
    This scripts extracts the dat as dataframe using pandas in joinrelation.db/DNS_column &
    adding two new columns(NE, Time_Granularity) to DB.

    Args:
       From joinrelation.db/DNS_column:
       tds_table_name = indicates the table name
       tds_column_name = indicates the colume name in each table

    Return:
        xml file(Asm7.xml) with node <col><map key="[...]" value="[...].[...]"/>...</cols>
"""

import lxml.etree as ET
import sqlite3
import pandas as pd
from yattag import indent

#################################################################################
# Build up connection with DB
conn = sqlite3.connect('joinrelation.db')

# Import data from DB by SQL as dataframe


# Loop through the DB data to build xml tree, and output as xml
# E.g.   <map key="[c1728053552(t_f05_dns_m1728053448)]" value="[t_f05_dns_m1728053448].[c1728053552]"/>


# Pretty Print of xml

# Output the result to Asm7.xml
