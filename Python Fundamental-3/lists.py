#list is mutable

marks = [33,56,59,96,32,66, 100.99]

print(marks[:])

# from given from to to
print(marks[1:5])

#if no start passed
print(marks[:4])

# no end is passed:
print(marks[0:])

# nothing passed just ':' :
print(marks[:])

#negative slicing
print(marks[-4:-2])

#methods

marks.append(203)
print(marks)

marks.insert(2, 1292)
print(marks)

marks.sort(reverse=True)
print(marks)

marks.reverse()
print(marks)

for value in range(0, len(marks)):
    if marks[value] == 56:
        print(f"value found at {value} index")
        break;
    print(value)
