guest = ['michelle obama','beyonce', 'marsai martin']
guest.remove('marsai martin')
print(guest)
guest.append('Viola Davis')
print(guest)
message = f"I would love  to formally invite you to dinner tonight Ms.{guest[0].title()}."
print(message)
message = f"You are my idol and I would love if you came to dinner with me and others tonight, Ms.{guest[1].title()}."
print(message)
message = f"I know it is short notice but there is a dinner at 9pm, that I would love for you to attend,{guest[2].title()}."
print(message)