import re

with open("Datasources.csv", 'r') as f1, open("Asm2.csv", 'w') as f2:
    f1.readline()
    f2.write(f"Domain,NE,Time Granularity,Datasources Name\n")
    for line in f1:
        if line:
            x = re.search(r'^(\w+)\s(\w+\s?[A-Za-z]+?)\s([0-9]*)', line)
            y = re.sub(r'^\w+\s\w+\s?\w+?\s[0-9]*', '', line)
            f2.write(f"{x.group(1)},{x.group(2)},{x.group(3)},{line}")

