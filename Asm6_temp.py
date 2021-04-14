""" This script output the full path of workbooks, and its name & view.
    Results & lists from Asm1 are being used in here & print out the full path of Workbooks.

    Args:
        Import from Asm1:
        ProjNameList(list) = Project Name list of all existing Projects
        ProjParentNameList(list) = Project Project of each Project, corresponding to ProjNameList
        WorkbookList(list) = Overall Workbooks List
        ViewList(list) = the corresponding view of each Workbook
        ParentProject(list) = Parent Project of each corresponding Workbook

    Return:
        csv file(Asm6.csv) contains the full path of workbooks, and its name & view
"""
import Asm1
import sys

def recursion_print(path, parent_proj):
    """Locate the given input project first & search its children prject,
        until there is no child project
        Print out the workbook name & its view name which belongs to that project
    """


# Holding the original output object. i.e. console out
orig_stdout = sys.stdout

with open("Asm6.csv", "w") as f:
    # Changing standard out to file out.
    sys.stdout = f

    # From Asm1
    # Create dictionary to map the parent & child project
    # Example: data = {parent1: [child1, child2], parent2: [child3, child4]}
    data =

    # From Asm1
    # Create dictionary to map the project & workbooks
    # Example: data = {project1: [wb1, wb2], project2: [wb1, wb2]}


    # Locate the top-level project & triggered recursion
    for project in data.keys():


    # ---------------------------------------------------------------------------------------------
# replacing the original output format to stdout.
sys.stdout = orig_stdout