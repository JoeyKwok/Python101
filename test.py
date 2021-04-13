list2 = ['CA1517', 'CM200', 'CM201', 'CM203', 'CM204', 'IT101', 'IT102', 'IT103', 'IT104', 'IT105', 'NS112', 'NS113', 'NS114', 'ON001','ON002','ON003','ON004']

# Filter values stared with CM
# str.find(): can't find -- -1
filter_cm = list(filter(lambda cm: (cm.find('CM') == -1), list2))
print('filter_CM:', filter_cm)

# values start with 'CA' = 'WNPD' & 'IT' = 'IOT Planning' & 'ON' = 'CS/IMS NW Operation'
map_ran = list(map(lambda ran: 'WNPD' if (ran.find('CA') > -1) else ( 'IOT Planning' if (ran.find('IT') > -1) else 'CS/IMS NW Operation' ), filter_cm))
print('mapping: ', map_ran)

# # using reduce to compute maximum element from list
# print("The maximum element of the list is : ", end="")
# print(functools.reduce(lambda a, b: a if a > b else b, lis))
# print(max(lis))