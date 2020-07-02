import json

student =[{
        "name" : "Lopi",
        "age" : 19,
        "hobby" : ["dancing","singing"]
    },
    {
        "name" : "Lopi",
        "age" : 19,
        "hobby" : ["dancing","singing"]
    }]
# object Dict to Json
# toJson = json.dumps(student, indent=4)
# print(toJson)
# fwrite = open("lalala.json", "w")
# fwrite.write(toJson)

# Json ke Object
fread = open("lalala.csv", "r")
toObject = json.loads(fread.read())
print(type(toObject))
# print(toObject["name"])