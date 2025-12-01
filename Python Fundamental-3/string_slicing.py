#string are immutable

word = "I am Prasad Kashid."

#slicing 
# string[start index : end index]
"""         ^               ^  ^--- not included 
            def = 0       def = len(str)
"""

# from given from to to
print(word[1:11])

#if no start passed
print(word[:11])

# no end is passed:
print(word[0:])

# nothing passed just ':' :
print(word[:])

#negative slicing
print(word[-4:-2])
