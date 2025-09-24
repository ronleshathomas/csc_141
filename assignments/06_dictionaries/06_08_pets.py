pet1 = {
    'animal': 'dog',
    'owner': 'mir'
}
pet2 = {
    'animal': 'cat',
    'owner': 'miya'
}
pet3 = {
    'animal': 'parrot',
    'owner': 'sier'
}
pet4 = {
    'animal': 'hamster',
    'owner': 'yanna'
}
pets = [pet1, pet2, pet3, pet4]
for pet in pets:
    print(f"Animal: {pet['animal'].title()}")
    print(f"Owner: {pet['owner'].title()}")
    print() 

