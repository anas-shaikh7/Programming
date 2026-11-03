# student = {"Rzaiya": "Khairpur public school", "Jamshed": "Mirus", "Anas": "Hyderabad"}
students = {
    "Raziya": "Khairpur public school", 
    "Jamshed": "Mirus", # key: value
    "Anas": "Hyderabad"
}
# making this better

# print(students["Raziya"]) --- this will print just the specfic key's location 
# print(students["Jamshed"])
# print(students["Anas"])


for student in students:
    print(students[student]) # we can make this variable student index the value it represents 

kids = [
    {"name": "Hermione", "house": "Gryddindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
     {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
     {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for kid in kids:
    print(kid["name"], kid["house"], kid["patronus"], sep=', ')