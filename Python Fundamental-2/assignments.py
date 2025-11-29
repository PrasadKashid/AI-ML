# q1
# def taxRate(salary: float,tax : float):
#     return(salary - (salary * (tax /100)))


# salary = float(input("Enter salary : "))
# if(salary < 30000):
#     print("Salary after tax is ",taxRate(salary, tax=5))
# elif(salary >= 30000 and salary <= 70000):
#     print("Salary after tax is ",taxRate(salary, tax=15))
# else:
#     print("Salary after tax is ",taxRate(salary, tax=25))
    
# q2
# def evenAndOdd(a,b):
#     for i in range(a, b+1):
#         if(i % 2== 0 ):
#             print(i)

# evenAndOdd(10, 20)

# q3
# def printNum(num):
#     while num > 0:
#         n = num % 10
#         num //= 10
#         print(n)
# printNum(1920)

#q4
# def countNums(num):
#     count = 0
#     while num > 0:
#         n = num % 10
#         num //= 10
#         count += 1
#     print(count)
        
# countNums(102910)

#q5
# def sumOfDigits(num):
#     n = 0
#     while num > 0:
#         n += num % 10
#         num //= 10 
#     print(n)
# sumOfDigits(5555)

#q6
# def printNum():
#     for i in range(1, 101):
#         if(i % 3 == 0 and i % 5 == 0):
#             print(i)

# printNum()

#q7 
# def userInput():
#     while True:
#         n = input("Enter a number or quit : ")
#         if(n == "quit"):
#             print("Quiting...")
#             break;
#         elif(float(n) > 0):
#             print("Positive Number ")
#         else:
#             print("Negative Number ")
# userInput();

#q8
# def calculator(a,b,operation ) :
#     # return (a operation b);
#     if operation == "+":
#         return a + b
#     elif operation ==  "-":
#         return a - b
#     elif operation == "/":
#         return a / b
#     else:
#         return a * b

# print(calculator(10,9,"*"))

#q9
# def is_prime(n):
#     dividedBy = 0
#     for i in range(2, n-1):
#         if(n % i == 0):
#             dividedBy += 1
        
#     if(dividedBy >= 1):
#         print("Non Prime")
#     else:
#         print("Prime")

# is_prime(51);

#q10
# def numberGuessing():
#     number_to_guess = 91
#     while True:
#         n = int(input("Enter number to guess "))
#         if(n > number_to_guess):
#             print("Too high....")
#         elif(n < number_to_guess):
#             print("Too low....")
#         else:
#             print("Correct!!")
#             break

# numberGuessing()