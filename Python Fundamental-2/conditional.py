# age = int(input("Enter age : "))
# if(age > 18) :
#     print("You can vote")
# else:
#     print("You can not vote")
    
# color = input("Enter color : ")

# if color == "red":
#     print("Stop")
# elif color == "green":
#     print("go")
# else:
#     print("Look")

# username = input("Enter username : ")
# password = input("ENter Password : ")

# if(username == "admin" and password == "pass"):
#     print("LOGIN successfull")
# elif(username != "admin"):
#     print("Wrong username")
# else:
#     print("Wrong password")

# n = int(input("Enter a number : "))
# if(n % 5 == 0):
#     print("Divisible by 5")
# else:
#     print("Not a multiple")

# username = input("Enter username : ")
# password = input("ENter Password : ")

# if(username == "admin" and password == "pass"):
#     print("success")
# else:
#     if(username != "admin"):
#         print("wrong pass")
#     else:
#         print("Wrong Pass")

color = input("Enter color : ")
match color:
    case "green":
        print("Go")
    case "red":
        print("Wait")
    case "yellow":
        print("look")
    case _:
        print("Wrong Color!!")
    