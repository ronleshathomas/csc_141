print("Reading the entire file:\n")
with open('learning_python.txt') as file_object:
    print(file_object.read())


print("\nReading the file line by line:\n")
with open('learning_python.txt') as file_object:
    for line in file_object.readlines():
        print(line.strip())


with open('learning_python.txt') as file_object:
    for line in file_object.readlines():
        print(line.replace('Python', 'C').strip())


with open('learning_python.txt') as file_object:
    contents = file_object.read()

for line in contents.splitlines():
    print(line.replace('Python', 'C'))

