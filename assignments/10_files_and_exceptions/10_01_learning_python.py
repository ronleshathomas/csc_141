"""In Python you can store data in variables and use them easily.
In Python you can use loops to repeat actions efficiently.
In Python you can define functions to organize your code.
In Python you can work with lists, dictionaries, and classes.
In Python you can read and write files to manage information."""


file_path = 'learning_python.txt'

print("=== Reading entire file ===")
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents)

print("=== Reading line by line ===")
with open(file_path) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())
