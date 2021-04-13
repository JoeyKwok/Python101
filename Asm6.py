"""This script output the full path of workbooks, and its name & view.

    Args:
        ProjNameList(list) = Project Name list of all existing Projects
        ProjParentNameList(list) = Project Project of each Project, corresponding to ProjNameList
        WorkbookList(list) = Overall Workbooks List
        ViewList(list) = the corresponding view of each Workbook
        ParentProject(list) = Parent Project of each corresponding Workbook

    Return:
        csv file contains the full path of workbooks, and its name & view
"""
import Asm1
import sys

def kpi_print(path, parent_proj):
    """Locate the given input project first & search its children prject,
        until there is no child project
        Need to extract info of Workbook in Explore/KPI Web & Explore/Workspace/$TeamProject/KPI Web
    """
    if parent_proj in data.keys():
        for child_proj in data[parent_proj]:
            if path == "top-level project":
                full_path = f"{parent_proj},{child_proj}"
            else:
                full_path = (
                    f"{path},{child_proj}"
                )

            if child_proj in data.keys():
                kpi_print(
                    full_path, child_proj
                )
            else:

                for ite, proj in enumerate(ParentProject):
                    if proj == child_proj:
                        workbook_info = f"{WorkbookList[ite]},{ViewList[ite]}"
                        print(f"{full_path},{workbook_info}")

# Holding the original output object. i.e. console out
orig_stdout = sys.stdout

with open("Asm6.csv", "w") as f:
    # Changing standard out to file out.
    sys.stdout = f

    # ---------------------------------------------------------------------------------------------
    # Create dictionary to map the parent & child project
    # Example: data = {parent1: [child1, child2], parent2: [child3, child4]}

    data = Asm1.ans_proj
    ProjNameList = Asm1.ProjNameList
    ProjParentNameList = Asm1.ProjParentNameList

    # ---------------------------------------------------------------------------------------------
    # Create dictionary to map the project & workbooks
    # Example: data = {project1: [wb1, wb2], project2: [wb1, wb2]}

    WorkbookList = Asm1.WorkbookList
    ViewList = Asm1.ViewList
    ParentProject = Asm1.ParentProject

    # ---------------------------------------------------------------------------------------------
    # Locate the top-level project & triggered recursion
    for project in data.keys():
        if project == 'None':  # top-level project
            for parent_project in data[project]:
                full_path = "top-level project"
                kpi_print(full_path, parent_project)

    # ---------------------------------------------------------------------------------------------
# replacing the original output format to stdout.
sys.stdout = orig_stdout