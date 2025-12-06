"""
r - reading [default]
w - writing, truncate file first - overwrite
x - creates new and open for writing
a - writing, appends at end
b - binary mode
t - text mode [default]
+ - open disk file for update(r & w)
rt wt - write text and read text
rb wb - write binary and read binary
r+ - if we write using r+ added at start 
a+ - if we write using a+ added at end 
"""

# read
f = open("./Python Fundamental-5/sample.txt") # even if we don't pass "r" it's by default in reading mode
print(f.read())
f.close()

# write
f = open("./Python Fundamental-5/sample.txt", "w")
f.write("Hey it's Prasad!!")
f.close()

# x - creating new file
f = open("./Python Fundamental-5/sample2.txt", "x")
f.write("New file created using x")
f.close()

# a - appends at end of file
f = open("./Python Fundamental-5/sample.txt", "a")
f.write("new line added using a")
f.close()

# + 
f = open("./Python Fundamental-5/sample.txt", "w+")
f.write("abc")
print(f.read())
f.close()

# using with -  no need to write close
with open("./Python Fundamental-5/sample.txt", "r") as f:
    print(f.read())

# os module to delete a file
import os 
os.remove("./Python Fundamental-5/sample2.txt")