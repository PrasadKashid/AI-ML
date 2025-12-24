# sets are immutable

set = {1,4,2,3,4,3,2}
set2 = {6,8,9}
print(set)

set.add(10)
print(set)

set.remove(3)
print(set)

# set.clear()
set.pop()
print(set)

set.union(set2)
print(set2)

info = [
    ("Alice","Math"),
    ("Bob","Science"),
    ("Charlie","Science"),
    ("Bob","Math"),
    ("Alice","English"),
    ("Charlie","English")
]


subs = set()
for name, course in info:
    # subs.add(name, course)
    print(name, course)
    subs.add(course)
print(subs)

data = set()
for name, course in info:
    if(course == "English"):
        data.add(name)
print(data)

dict  = {}
for name, course in info:
    if(dict.get(name) == None):
        dict.update({name : set()})
        dict[name].add(course)
    else:
        dict[name].add(course)
print(dict)
