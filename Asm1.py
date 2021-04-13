# Match up the parent Folders with the children Folders
import csv
##############################################################################
# Create dictionary to map the parent & child project
# Example: data = {parent1: [child1, child2], parent2: [child3, child4]}
def mapping(ParentList, NameList):
    data = {}
    for ite1, id in enumerate(ParentList):
        if id not in data.keys():
            data[id] = []
        data[id].append(NameList[ite1])

    return data

##############################################################################

def readcsv(csv_name):
    data = []
    with open(csv_name, newline='') as f1:
        for row in csv.reader(f1):
            data.append(row[0])
    return data

ProjNameList = readcsv('ProjNameList.csv')
ProjParentNameList = readcsv('ProjParentNameList.csv')

WorkbookList = ['Project ID', 'CDR Daily - STS Report', 'CDR Daily - VoWifi Report', 'DNS Overview', 'A_Testing for KPI Web', 'DNS001 Internal resolution success rate', 'DNS002 External resolution success rate', 'Verification Template - UGW']
ViewList = ['ID', 'Overall', 'Overall', 'DNS MAIN', 'AAA', 'DNS1', 'DNS2', 'Verify']
ParentProject = ['Flow Monitoring', 'STS', 'VoWifi', 'DNS', 'DNS', 'DNS' ,'DNS', 'Data Sources Verification']


print('List out the dictionary of parent/child project.')
ans_proj = mapping(ProjParentNameList, ProjNameList)
print(ans_proj)
print('\n')

print('List out the dictionary of view in workbook')
ans_wb = mapping(ParentProject, WorkbookList)
print(ans_wb)