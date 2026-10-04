data = {"name": "Alice", "age": 30, "city": "New York"}

del data["age"]
print(data)

#pop
data = {"name": "Alice", "age": 30, "city": "New York"}

deleted_data = data.pop("city")
print(data)
print("Deleted data:", deleted_data)


# popitem
data = {"name": "Alice", "age": 30, "city": "New York"}

deleted_item = data.popitem() #last value deleted
print(data)

data.clear()
print(data)

#nested dictionary
data = {
  "name": "Alice", 
  "age": 30,
  "city": {
    "perm": "pokhara",
    "temp": "kathmandu"
  },
  "experience": 5,
  "profession": "Engineer"
}

print(data["city"]["perm"]) #accessing nested dictionary


user_info = {
    "name":"Ramesh",
    "age":12,
    "phone":[
        {
            "type":"JIO",
            "number":9844
        },
         {
            "type":"NCell",
            "number":98097
        },

    ]
}

print("---------------------------------")
print(user_info["phone"][0]["type"])
print(user_info["phone"][1]["number"])


print(f'{user_info["name"]} {user_info["phone"][1]["type"]} number is {user_info["phone"][1]["number"]}')
print(f'{user_info["name"]} {user_info["phone"][0]["type"]} number is {user_info["phone"][0]["number"]}')


fname = "Namuna"
lname = "Timsina"
age = 26

print("my first name is", fname, "my last name is", lname, "and my age is", age)
f'my name is {fname} my last name is {lname} and my age is {age}'