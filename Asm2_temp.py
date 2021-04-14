"""This script splits the datasource names using Regular expressions in Datasources.csv by objects &
    output as Asm2.csv.

    Args:
        csv - Datasources.csv = contains datasource names i.e. Domain | NE | Time Granularity| Datasources Name
        Example:
        Datasource Name
        CORE CG 60 M167774000 CDR Receival
        CORE NSA UDG 30 M1911554230 PGW-C 2G session measurement (specified APN)

    Return(Expected Output):
        Example(Please refer to Asm2.csv)
        Domain,NE,Time Granularity,Datasources Name
        CORE,CG,60,CORE CG 60 M167774000 CDR Receival
        CORE,NSA UDG,30,CORE NSA UDG 30 M1911554230 PGW-C 2G session measurement (specified APN)

"""
import re


