name1="Sai"
age1=28
is_learning_ai1=True

name2="Gayathri"
age2=23
is_learning_ai2=False



sai ={
    "name":"Sai",
    "age":28,
    "is_learning_ai":True
}
gayathri ={
    "name":"Gayathri",
    "age":23,
    "is_learning_ai":False
}



people=[sai, gayathri]


for person in people:
    print(person["name"])
people=[sai, gayathri]

for person in people:
    print(person["name"], person["age"], person["is_learning_ai"])

for person in people:
    if person["is_learning_ai"]==True:
        print(person["name"], "is learning AI")
    else:
        print(person["name"], "is not learning AI")

def describe_person(person):
    if person["is_learning_ai"]:
        return person["name"] + " is learning AI"
    else:
        return person["name"] + " is not learning AI"

print(describe_person(sai))
print(describe_person(gayathri))
