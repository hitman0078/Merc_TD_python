numbers = [1, 2, 3, 4]
numbers.append(5)
print(numbers)

my_list = [10, "apple", 12, 13, 14]
print("--------")
print(my_list)
print(my_list[1:2])
print(my_list[1:3])
print(my_list[:2])
print(my_list[2:])


items = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
if "apple" in items:
    print("Yes, 'apple' is in the fruits list")
elif "banana" in items:
    print("Yes, 'banana' is in the fruits list")
else:
    print("fruit not found")

print("\n Task 1: Use a for loop to traverse and print prices ", end="")
print("for each fruit using if-else statements")
prices = {
    "apple": 100,
    "banana": 40,
    "cherry": 80,
    "orange": 60,
    "kiwi": 200,
    "melon": 70,
    "mango": 85
}

for fruit in items:
    if fruit == "apple":
        print(f"The price of {fruit} is INR {prices['apple']:.2f} per kg")
    elif fruit == "banana":
        print(f"The price of {fruit} is INR {prices['banana']:.2f} per kg")
    elif fruit == "cherry":
        print(f"The price of {fruit} is INR {prices['cherry']:.2f} per kg")
    elif fruit == "orange":
        print(f"The price of {fruit} is INR {prices['orange']:.2f} per kg")
    elif fruit == "kiwi":
        print(f"The price of {fruit} is INR {prices['kiwi']:.2f} per kg")
    elif fruit == "melon":
        print(f"The price of {fruit} is INR {prices['melon']:.2f} per kg")
    elif fruit == "mango":
        print(f"The price of {fruit} is INR {prices['mango']:.2f} per kg")
    else:
        print(f"Price for {fruit} not found.")