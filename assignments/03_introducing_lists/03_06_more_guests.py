guest = ['michelle obama','beyonce', 'marsai martin']
message = f"I have found a bigger table and will be inviting more people {guest}."
print(message)
guest.insert(0, 'viola davis')
guest.insert(2, 'Rihanna')
guest.append('H.E.R')
print(guest)
message = f"I would love  to formally invite you to dinner tonight Ms.{guest[0].title()}."
print(message)
message = f"You are my idol and I would love if you came to dinner with me and others tonight, Ms.{guest[1].title()}."
print(message)
message = f"I would love for you to attend dinner with me Ms.{guest[2].title()}."
print(message)
message = f"I know it is short notice but there is a dinner at 9pm, that I would love for you to attend, Ms.{guest[3].title()}."
print(message)
message = f"There is a dinner tonight,I believe you would enjoy.{guest[4].title()}."
print(message)
message = f"I would love for you to attend and perform at dinner tonight Ms.{guest[5].title()}."
print(message)      