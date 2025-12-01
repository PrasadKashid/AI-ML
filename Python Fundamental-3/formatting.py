"""
1. format()
2.f-strings

"""

a = 5
b = 7
sum = a + b

#normal formatting
print("sum is {}".format(sum))
#formatting by passing multiple values
print("sum of {} and {} is {}".format(a,b,sum))
#formatting using indexes
print("sum of {1} and {0} is {2}".format(a,b,sum))
#value based formatting
print("Values of {a} & {b}".format(a =20, b = 30));


#f-strings
print(f"sum of two number {sum}")