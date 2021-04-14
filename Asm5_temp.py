""" Please installs Db Broswer fro SQLite to simulate the DB environment in local PC.
    This scripts extracts the data(tds_name) as dataframe using pandas in joinrelation.db/DNS_Join &
    adding two new columns(NE, Time_Granularity) to DB.

    Args:
        From joinrelation.db/DNS_Join:
        tds_name(dataframe) = indicates the table name i.e. pms | t_f | Time_Granularity | NE | table number
        i.e. pms.t_f05_dns_m1728053448

    Return(Expected Output):
        Adding two new columns(NE, Time_Granularity) to DB according the info extract from tds_name,
        regular expressions can be used to simplify the extraction.
        Output is shown as Asm5_expectedoutput.PNG.

"""

import sqlite3
import pandas as pd

#################################################################################
# Build up connection with DB
conn = sqlite3.connect('joinrelation.db')

# Import data from DB by SQL as dataframe


# Create new columns in DB


# Find out the values of NE & Time_Granularity and insert to DB

# Input dataframe record to SQL DB
df.to_sql(name ='DNS_Join', con = conn ,if_exists='replace', index = False)
