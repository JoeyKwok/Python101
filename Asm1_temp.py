"""This script matching the parent Folders with the children Folders.
    2 functions are created to do the mapping and reading of csv.
    Expected output: {parent1: [child1, child2], parent2: [child3, child4]}

    Args:
        csv - ProjNameList.csv/ ProjParentNameList.csv = ProjParentNameList.csv indicate the correpsonding parent project of each project in ProjNameList.csv
        lists - WorkbookList/ParentProject = lists indicate the parent project of each Workbook

    Return(Expected Output):
        List out the dictionary of parent/child project.
        {'RAN': ['2G', '3G', '4G', '5G', 'CDMA', 'DAS', 'DATACOM', 'FEMTO', 'GBL', 'MISC', 'NODE', 'WIFI'], 'CORE': ['ALARM', 'ATS', 'CG', 'CSCF', 'DNS', 'eMGW', 'eMSC', 'ENS', 'ePDG', 'eSight', 'HSS', 'IMS', 'IPBB', 'NSA_UDG', 'SBC', 'SPS', 'UEIR', 'UGW', 'UIM', 'UPCC', 'USN'], 'Workbook': ['CDR', 'Flow Monitoring', 'HSSDB', 'Smart Care'], 'Data Source': ['CORE', 'EARTH', 'RAN', 'SPO', 'VAS'], 'KPI Web': ['Core'], 'CDR': ['Daily Report', 'KPI', 'Monthly Report', 'STS', 'VoWifi'], 'None': ['Data Source', 'Flow', 'KPIWeb', 'Workbook', 'Workspace', 'Default'], 'Default': ['Data Sources Verification', 'External files', 'Monitoring', 'Others'], 'EARTH': ['iCG', 'iUGW', 'iUSN', 'vCG', 'vUGW', 'vUPCC'], 'Workspace': ['NAA'], 'SPO': ['OCN_AGG', 'ORN_AGG'], 'VAS': ['OCU', 'SCU']}
        List out the dictionary of view in workbook
        {'Flow Monitoring': ['Project ID'], 'STS': ['CDR Daily - STS Report'], 'VoWifi': ['CDR Daily - VoWifi Report'], 'DNS': ['DNS Overview', 'A_Testing for KPI Web', 'DNS001 Internal resolution success rate', 'DNS002 External resolution success rate'], 'Data Sources Verification': ['Verification Template - UGW']}

"""

import csv
##############################################################################
# Create dictionary to map the parent & child project from lists
# Example: data = {parent1: [child1, child2], parent2: [child3, child4]}

##############################################################################
# Reading csv and convert into lists

##############################################################################


WorkbookList = ['Project ID', 'CDR Daily - STS Report', 'CDR Daily - VoWifi Report', 'DNS Overview', 'A_Testing for KPI Web', 'DNS001 Internal resolution success rate', 'DNS002 External resolution success rate', 'Verification Template - UGW']
ParentProject = ['Flow Monitoring', 'STS', 'VoWifi', 'DNS', 'DNS', 'DNS' ,'DNS', 'Data Sources Verification']
ViewList = ['ID', 'Overall', 'Overall', 'DNS MAIN', 'AAA', 'DNS1', 'DNS2', 'Verify']

print('List out the dictionary of parent/child project.')


print('List out the dictionary of view in workbook')
