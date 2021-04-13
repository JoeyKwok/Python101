import xml.etree.ElementTree as ET

input_xml_file = ET.parse("SET and parameter3.0.tds")
parameter = input_xml_file.find('datasource-dependencies')

for item in parameter.findall('column'):
    caption = item.attrib['caption']
    name = item.attrib['name']
    name = name.replace('[', '').replace(']', '')
    datatype = item.attrib['datatype']
    paramdomaintype = item.attrib['param-domain-type']
    value = item.attrib['value']
    value = value.replace('"', '')

    print('Caption: ', caption)
    print('Name: ', name)
    print('Datatype: ', datatype)
    print('Parameter Domain Type: ', paramdomaintype)
    print('Value: ', value)

    print('Member include:')
    if item.findall('members/member'):
        for ite, members in enumerate(item.findall('members/member')):
            ite = ite+1
            member = members.attrib['value']
            member = member.replace('"', '')
            print('\t', ite, '-', member)
    else:
        print('\tParameter \'{}\' contains NO member value.'.format(caption))

    print('\n')