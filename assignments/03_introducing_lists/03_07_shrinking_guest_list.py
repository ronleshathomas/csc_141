guest = ['michelle obama','beyonce', 'marsai martin']
message = f"I have found a bigger table and will be inviting more people {guest}."
print(message)
guest.insert(0, 'viola davis')
guest.insert(2, 'Rihanna')
guest.append('H.E.R')
print(guest)
message = f"So I found out my new table will not arrive in time and I can only have two more people attend {guest}"
print(message)
removed_guest = guest.pop()
print(f"Sorry {removed_guest.title()}, I can no longer invite you to dinner.")
removed_guest = guest.pop()
print(f"Sorry {removed_guest.title()}, I can no longer invite you to dinner.")
removed_guest = guest.pop()
print(f"Sorry {removed_guest.title()}, I can no longer invite you to dinner.")
removed_guest = guest.pop()
print(f"Sorry {removed_guest.title()}, I can no longer invite you to dinner.")
message = f"I would still love  to formally invite you to dinner tonight Ms.{guest[0].title()}."
print(message)
message = f" I would love if you still came to dinner with me and others tonight, Ms.{guest[1].title()}."
print(message)
del guest[1]
del guest[0]
print(guest)
