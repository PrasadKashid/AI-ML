# q1
userInput = input("Enter a string : ")
reverseString  = ""
for ch in userInput:
    reverseString = ch + reverseString

print(reverseString)
if(userInput == reverseString):
    print("Palindrome")
else:
    print("Not a palindrome")
    
# q2
nums = [1,2,3,4,5]
sum = 0
for i in nums:
    sum += i
print("Avg = " , sum // len(nums))

# q3
l1 = [1,2,3]
l2 = [1,2,7]

l3 = l1 + l2
l3.sort()
print(l3)

# q4
even = []
odd = []
tup = (1,2,3,4,5,6)
for i in tup:
    if(i % 2 == 0):
        even.append(i)
    else:
        odd.append(i)
evenTup = tuple(even)
oddTup = tuple(odd)
print(evenTup)
print(oddTup) 

# q5
dict = {}

while True:
    option = input("Enter Options : \n A. Add a student \n B. Update Marks \n C. Search for student \n D. Display all students and marks \n")
    match option:
        case 'A':
            student_name = input("Enter student name : ")
            if(dict.get(student_name) == None):
                dict.update({student_name : []})
                print(f"Student added successfully with name {student_name}")
            else:
                print("Student name already exists :(")
        case 'B':
            student_name = input("Enter student name to add marks : ")
            if(dict.get(student_name) == None):
                print("Student name does not exists ")
            else:
                marks = int(input("Enter marks : "))
                dict[student_name].append(marks)
                print("Marks added successfully")
        case 'C':
            student_name = input("Enter student name to find : ")
            if(dict.get(student_name) == None):
                print("Student not found ")
            else:
                print(f"{student_name}'s Marks : ",dict[student_name])
        case "D":
            print("All students information : ",dict)
        case _:
            print("Invalid Input!!");
            break;
        
# q6
words = ["apple", "banana","kiwi", "cherry","mango"]
dict = {}
for fruit in words:
    dict.update({fruit : len(fruit)})
print(dict)

# q7
userInput = str(input("Enter a set of strings to get number of spaces : "))
count = 0
for i in userInput:
    if(i == " "):
        count += 1
print("Spaces in string", count)

# q8
l1 = [1,2,3,4]
l2 = [1,2]

s1 = (l1,l2)

if(len(s1) < len(l1) + len(l2)):
    print("same values")
else:
    print("No same values")

# q9
l1 = [1,2,3,4]
l2 = [1,2]

s1 = set(l1)
s2 = set(l2)

print(s1.intersection(s2))

# q10
userInput = input("Enter a string : ")
dict = {}
for i in userInput:
    if(dict.get(i) == None):
        dict.update({i : 1})
    else:
        dict[i] = dict[i] + 1
print(dict)
uniqueChars = []
unique_chars_with_count = []
for ch in dict:
    if(dict[ch] == 1):
        uniqueChars.append(ch)
        unique_chars_with_count.append({ch : dict[ch]})
print("Unique chars : ", uniqueChars)
print("Unique chars with count : ", unique_chars_with_count)