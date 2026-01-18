with open("data.txt", "w", encoding="utf-8") as file_obj:
    file_obj.write("Hello File")

with open("data1.txt", "w", encoding="utf-8") as file_obj:
    file_obj.write("Hello File111")

with open("data.txt", "r", encoding="utf-8") as file_obj:
    content = file_obj.read()
    print(content)

with open("data.txt", "r", encoding="utf-8") as file_obj:
    content = file_obj.read()
    print(content)