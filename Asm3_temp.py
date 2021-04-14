"""This script parsing an xml-based file(SET and parameter3.0.tds) and output the specific info as shown in Return.

    Args:
        xml - SET and parameter3.0.tds
        Reading info in <datasource-dependencies datasource='Parameters'>....</datasource-dependencies>
        attributes ['caption'], ['name'], ['datatype'], ['param-domain-type'], ['value'] are being used.

    Return(Expected Output):
        Caption:  Include Today
        Name:  Include Today
        Datatype:  string
        Parameter Domain Type:  list
        Value:  No
        Member include:
             1 - No
             2 - Yes


        Caption:  Day option
        Name:  Parameter 2
        Datatype:  string
        Parameter Domain Type:  list
        Value:  last 3 day
        Member include:
             1 - last 2 day
             2 - last 3 day


        Caption:  Year Parameter
        Name:  Year Parameter
        Datatype:  integer
        Parameter Domain Type:  range
        Value:  2017
        Member include:
            Parameter 'Year Parameter' contains NO member value.

"""
import xml.etree.ElementTree as ET

# Parsing xml
input_xml_file = ET.parse("SET and parameter3.0.tds")
# Locate the node of useful xml

# For loop reading the parameters in the node
# Output the member value if existed