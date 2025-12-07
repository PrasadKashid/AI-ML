#q1
def question1():
    count = 0
    with open('./Python Fundamental-5/names.txt', 'a') as f:
        while True:
            username = input("Enter user name : ")
            f.writelines(username + '\n')
            count += 1
            if(count == 5):
                break
    with open('./Python Fundamental-5/names.txt', 'r') as f:
        for line in f:
            print(line.strip())
    
#q2
def question2():
    with open('./Python Fundamental-5/log.txt', 'a') as f:
        try:
            divide = int(input("Enter a number to divide : "))
            for i in range(0, 11):
                print(round((i / divide), 2))
        except ZeroDivisionError:
            f.writelines('Cannot be divided by zero \n')
        except ValueError:
            f.writelines("A value error occured \n" )
        else:
            f.writelines("Program run successfully \n" )
    
    with open('./Python Fundamental-5/log.txt', 'r') as f:
        print("-----------Logs from file--------------")
        for line in f:
            print(line.strip())

#q3
def question3():
    nums = [5,10,15,20,25,30]
    newNums = [i for i in nums if i >= 15]
    print(newNums)

#q4
import json
def question4():
    citiesdata = {
        'Mumbai' : 1000000,
        'Pune' : 500000,
        'Delhi' : 982000
    }        
    with open('./Python Fundamental-5/cities.json', 'w') as f:
        json.dump(citiesdata, f,indent=2)
        
    with open('./Python Fundamental-5/cities.json', 'r') as f:
        data  = json.load(f)
        for city in data:
            print(f"{city} : ",data[city])
            
    city = input("Enter a city : ")
    population = int(input(f"Enter population for {city} : "))
    with open('./Python Fundamental-5/cities.json', 'w') as f:
        citiesdata.update({city : population})
        json.dump(citiesdata, f,indent=2)

def question5():
    try:
        with open("./Python Fundamental-5/abc.txt", 'r') as f:
            data = f.read();
    except FileNotFoundError:
        print("File not found!")
    else:
        print(data)
        
question5()