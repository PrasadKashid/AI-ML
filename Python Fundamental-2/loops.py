# a = int(input("Enter a num : "))
# count = 1
# while count <= a:
#     print(f"hello {count}")
#     count += 1
    
# i  = 5
# while (i <= 1):
#     print(i)
#     i += 1
    
# i = 1
# num= int(input("ENter a number to generate the table : "))
# while i <= 10:
#     print(f"{num} x {i} =", num * i)
#     i += 1

# i = 1
# while i <= 10:
#     if(i % 6 == 0):
#         break;
#     print(i)
#     i+= 1
# print("Outside loop")
# i = 1
# while i < 10:
#     i += 1
#     if(i % 2 == 0):
#         continue;
#     print(i)
# print("Outside loop")

# for i in range(1, 11):
#     print(i)
    
# a = "hello"
# for i in "hello":
#     print(i)

# a = [1,3,4,4,5]
# for i in range(0, len(a)):
#     print(a[i])

# a = "hello"
# if 'o' in a:
#     print("yes")

# word = "artificial intelligence"
# count = 0
# for i in word:
#     if (i == 'i'):
#         count += 1
# print(count)
        
# word = "artificial intelligence"
# count = 0
# for ch in word:
#     print(ch)
#     match ch:
#         case 'a':
#             count += 1
#         case 'e':
#             count += 1
#         case 'o':
#             count += 1
#         case 'i' :
#             count += 1
#         case 'u':
#             count += 1
#         case _:
#             continue;
# print("count" , count)

# word = "artificial intelligence"
# count = 0
# for ch in word:
#     if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' ):
#         count += 1
# print(count)
# sum =0
# for i in range(1, 6):
#     sum += i
# print(sum)

# sum = lambda a,b,c: a+b+c
# print(sum(4,5,6))

def fact(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
print(fact(5))

a = 10
print('yes' if a < 6 else "no")