# importing existing json module
import json


# reading json file from current directory
with open("data.json", "r") as data_file:
    data = json.load(data_file)


# Get class value from json object
print(data["class"])

# Get school value from json object
print(data["school"])

# Get location value from json object     
print(data["location"])


# Get instructors value from json object     
print(data["instructors"])


# Get 1 instructors value from json object     
print(data["instructors"][0]["instructor1"]["name"])
INSTRUCTOR1_NAME = data["instructors"][0]["instructor1"]["name"]
INSTRUCTOR1_LASTNAME = data["instructors"][0]["instructor1"]["lastname"]


# for i in data["instructors"]:
#     print(i)


# # Write instructor 1 information to a file
with open("instructor1_data", "a") as target_file:
    target_file.write(INSTRUCTOR1_NAME + " " + INSTRUCTOR1_LASTNAME)

target_file.close()    
