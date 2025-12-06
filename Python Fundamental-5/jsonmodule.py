import json;

py_obj = {
    'name' : 'Nisha',
    'isStudent' :True
} 

json_str = json.dumps(py_obj)
print(json_str)

json_str = '{"name" : "Nisha", "isStudent" : true}'
py_obj = json.loads(json_str)
print(py_obj['name'])

py_obj = {
 "profile": {
    "age": 28,
    "country": "India",
    "skills": [
      { "name": "Python", "level": "Intermediate" },
      { "name": "React", "level": "Beginner" }
    ]
  }
 }

with open("./Python Fundamental-5/data.json", "w") as f:
    json.dump(py_obj , f, indent=2, sort_keys=True)
    
    
with open("./Python Fundamental-5/data.json", "r") as f:
    py_obj = json.load(f)
    print(py_obj)