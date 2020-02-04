num_strings = ['13', '44', '100', '23']
num_int = [13, 44, 100, 23]
num_float = [2.0, 3.4, 55.0, 12]
num_list = [[1, 2, 3], [2.3, 34.4, 100.0], ['test', 'new', '12345'], [4, 3, 2]]

# Stings
print("\nThe variable num_strings is a {0}".format(type(num_strings)))
print("It contains the elements: {0}".format(num_strings))
print("The element {0} is a {1}".format(num_strings[0], type(num_strings[0])))

# Int
print("\nThe variable num_strings is a {0}".format(type(num_int)))
print("It contains the elements: {0}".format(num_int))
print("The element {0} is a {1}".format(num_int[0], type(num_int[0])))

# Float
print("\nThe variable num_strings is a {0}".format(type(num_float)))
print("It contains the elements: {0}".format(num_float))
print("The element {0} is a {1}".format(num_float[0], type(num_float[0])))

# Lists
print("\nThe variable num_strings is a {0}".format(type(num_list)))
print("It contains the elements: {0}".format(num_list))
print("The element {0} is a {1}".format(num_list[0], type(num_list[0])))

# sort variables
num_strings.sort()
num_int.sort()
# Sorting lists
print("\nNow sorting num_strings and num_int...")
print("Sorted num_strings: {0}".format(num_strings))
print("Sorted num_int: {0}".format(num_int))
print("\nStrings are sorted alphabetically whiel intefers are sorted numerically!")
