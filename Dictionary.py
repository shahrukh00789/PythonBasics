data = {"name":"Shahrukh khan","Address":"Kharghar",
        "Occupation":"Data Scientist",
        "Skills":{"frontend":"Html","Backend":"Python"}}
print(data)

print(data["Skills"])

data["Location"]="Worli"
print(data)

del data["Location"]

print(data)

data_copy = data

print(data_copy["Skills"])

# del data_copy["name"]
print("After Deletion")
print(data["Skills"])

data.update({"name":"Asif"})
print(data)

print(data.items())