nums = [45,87,21,24,99]
print(nums)
# print first number 
print(nums[0])
# negative indexing
print(nums[-5])

# slicing
print(nums[2:4])

# slicing till end
print(nums[2:])

names = ["sai", "sandeep", "medisetty"]

print(names)

# mixing of names and numbers in single list
mix = ["sandeep" , 36, 6.5]

print(mix)

#mixing of two lists
mix = [nums, names]

print(mix)

print(len(mix))

# get the first list element

print(mix[0][0])
print(mix[1][2])

# combine the two lists

mix = nums + names;
print(mix)

# add element at the end
nums.append(33)

print(nums)

# number of times an element 

print(nums.count(45))

# inserts element in specific index
nums.insert(1, 55)

print(nums)

# remove an element 

nums.remove(55)

print(nums)

# remove an element at an index

nums.pop(4);

print(nums);

# removes last element

nums.pop()

print(nums);

# deletes elements from lists

del nums[2:4]

print(nums)

# add the elements into lists

nums.extend([44,56,11,99])

print(nums)

# replace particular indexed elements in lists

nums[2:4] = [54,76]

print(nums)

# reverse a list

nums.reverse()

print(nums)

# min number

print(min(nums))

# max number 

print(max(nums))

# sum of numbers

print(sum(nums))

print(min(names))

