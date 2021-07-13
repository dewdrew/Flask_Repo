ranger = [x for x in range (5)]

print(ranger)

multiple_3 = [x*3 for x in range(5)]
print(multiple_3)

#list comprehension is basically creating lists in pyhton with simple functions 
print([x  for x in range(10) if x % 2 ==0])


list_person = ['Smart','Tange','Santan','Jeff','Saint','Bugzy']
normalized_list = [person.strip().lower() for person in list_person]

print(normalized_list)