def make_album(artist, title, songs=None):
    album = {"artist": artist, "title": title}
    if songs:
        album["songs"] = songs
    return album

album1 = make_album("Drake", "Scorpion")
album2 = make_album("Adele", "30")
album3 = make_album("Kendrick Lamar", "DAMN.", songs=14)

print(album1)
print(album2)
print(album3)

