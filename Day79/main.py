# # file not found
# try:
#     file = open("a._file.txt")
# except FileNotFoundError as error_message:
#     open("a_file.txt", "w")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise KeyError

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)