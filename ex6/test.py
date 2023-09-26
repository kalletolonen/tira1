test_dict = {1:3, 2:5, 3:5}

 
# printing original dictionary
print("The original dictionary is : " + str(test_dict))
 
# extracting value to compare
test_val = list(test_dict.values())[0]
 
# checking if all values are equal to test_val
res = all(val == test_val for val in test_dict.values())
 
# printing result
print("Are all values similar in dictionary? : " + str(res))

print("hello")