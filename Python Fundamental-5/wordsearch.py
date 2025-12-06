data = True
line_number = 1
word = "store"
with open("./Python Fundamental-5/sample.txt", "r") as f:
    while data:
        data = f.readline()
        if("python" in data):
            print(f"{word} found at line {line_number}")
            break
        line_number += 1
        
