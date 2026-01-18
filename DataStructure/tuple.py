# Defining the Tuple
my_tuple = ("Apple", 10, "Orange", "Grapes", 20.0, 10)

# 1. Accessing by index (index 3 is the 4th item)
print(my_tuple[3])        # Output: Grapes

# 2. Accessing the last item using negative indexing
print(my_tuple[-1])       # Output: 10

# 3. Slicing from index 2 up to (but not including) index 4
print(my_tuple[2:4])      # Output: ('Orange', 'Grapes')

# 4. Slicing from the beginning up to index 4
print(my_tuple[:4])       # Output: ('Apple', 10, 'Orange', 'Grapes')

# 5. Slicing from index 2 to the end
print(my_tuple[2:])       # Output: ('Orange', 'Grapes', 20.0, 10)

# 6. Slicing with negative indices
print(my_tuple[-4:-1])    # Output: ('Orange', 'Grapes', 20.0)

print("Task 1: Print the items from the tuple")

sensor_readings = ("2026-01-16", 22.5, "Sunny", 1013.2, 45, "North", "Active")

# 2nd item
print(sensor_readings[1])

# Last item
print(sensor_readings[-1])

# Last 3 items
print(sensor_readings[-3:])

# First four items
print(sensor_readings[:5])

# Slice index 1 to 4
print(sensor_readings[1:5])