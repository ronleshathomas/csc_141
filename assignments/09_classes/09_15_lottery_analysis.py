lottery_items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

my_ticket = [2, 'B', 7, 'E']

attempts = 0

while True:
    attempts += 1
    drawn_ticket = (lottery_items, 4)
    if set (drawn_ticket) == set(my_ticket):
        break

print(f"Your ticket {my_ticket} just won after {attempts} draws!")

