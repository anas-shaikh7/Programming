students = ["kaki", "kako", "kaka"] # --> index[0, 1, 2]
location = ["Cantt", "Citizen", "Qasimabad"]

# print(students[0]) # if you want a specific value from the list


# for student in students:
#     print(student)


for i in range(len(students)):
    # print(i+1,students[i])
    print(str(i+1) + "." + students[i], end=' ')
for i in range(len(students)) and range(len(location)):
    print(students[i],location[i])

    