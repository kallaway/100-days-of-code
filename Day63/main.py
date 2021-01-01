# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# modes - a =  append, r is read, w is write
with open("new_file.txt", mode="w") as file:
    file.write("\nNew text.")
