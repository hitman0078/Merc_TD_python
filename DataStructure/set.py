unique = {1, 2, 3}
unique.add(4)
unique.add(4)
print(unique)

# Force-assign the new values
my_set_1 = {"Apple", 10, "Orange", "Grapes", 20.0}
my_set_2 = {30.0, 10, "Orange", "Apple", 40}

# Print the results
print("Union:", my_set_1 | my_set_2)
print("Intersection:", my_set_1 & my_set_2)
print("Difference:", my_set_1 - my_set_2)
print("Symmetric Difference:", my_set_1 ^ my_set_2)

print("Task 1: Perform Union, Intersection, Difference")

employees_mon = {"Alice", "Bob", "Charlie"}
employees_tue = {"Bob", "Charlie", "David"}

print("Union:", employees_mon | employees_tue)
print("Intersection:", employees_mon & employees_tue)
print("Difference:", employees_mon - employees_tue)
print("Symmetric Difference:", employees_mon ^ employees_tue)