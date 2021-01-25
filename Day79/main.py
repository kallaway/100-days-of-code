# file not found
try:
    file = open("a._file.txt")
except FileNotFoundError as error_message:
    open("a_file.txt", "w")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("file was closed")