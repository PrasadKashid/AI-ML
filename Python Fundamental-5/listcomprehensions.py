nums = [i**2 for i in range(1,6) if i % 2 != 0]
print(nums)

nums = [i for i in range(1, 10) if i % 2 == 0]
print(nums)

nums = [-2,-4,-5,0,1,4,2,-1]
nums = [0 if val < 0 else val for val in nums]
print(nums)

words = ["hello", "prasad", "here"]
words = [word.upper() for word in words]
print(words)