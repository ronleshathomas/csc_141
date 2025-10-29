cats.txt = """Whiskers, Mittens, Shadow"""
with open('cats.txt', 'a') as file_object:
 
dogs.txt = """Buddy, Charlie, Bella"""
with open('dogs.txt', 'a') as file_object: 

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    print(f"\nReading file: {filename}")

    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print(f"Sorry, the file '{filename}' was not found.")
    else:
        print(contents.strip())
