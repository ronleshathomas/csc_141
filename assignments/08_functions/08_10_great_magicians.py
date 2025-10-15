def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    while messages:
        message = messages.pop(0)  
        print(message)
        sent_messages.append(message)

text_messages = [
    "Hello, how are you?",
    "Don't forget the meeting tomorrow.",
    "Happy Birthday!",
    "See you soon."
]

sent_messages = []

send_messages(text_messages, sent_messages)

print("\nOriginal list (should be empty):", text_messages)
print("Sent messages list:", sent_messages)

