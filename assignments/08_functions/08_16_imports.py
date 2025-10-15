def display_message():
    print("I’m learning about functions in this chapter!")


import message
message.display_message()

from message import display_message
display_message()

from message import display_message as dm
dm()

import message as msg
msg.display_message()
