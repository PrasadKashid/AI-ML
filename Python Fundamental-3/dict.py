"""
dictionary - Stores key value pairs
"""

info = {
    "name" : "Prasad",
    "subj" : "AI, ML",
    "age" : 23
}
print(info["name"])

dict_key = info.keys() #return all keys
print(dict_key)

dict_values = info.values() # return all values
print(dict_values)

dict_items = info.items() #return all key value pairs
print(dict_items)

print(info.get("cgpa")) 
"""when we use this if the dict does not have the key we are looking for,
we can also use info["cgpa"] --> gives keyError and stops executing the remaining code"""

info.update({
    "city" : "mumbai"
})

print(info.values())