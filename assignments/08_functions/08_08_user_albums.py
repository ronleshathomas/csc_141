def make_album(artist, title, songs=None):
    album = {"artist": artist, "title": title}
    if songs:
        album["songs"] = songs
    return album

while True:
    print("\nEnter album information (or type 'quit' at any time to stop):")

    artist = input("Artist name: ")
    if artist.lower() == 'quit':
        break

    title = input("Album title: ")
    if title.lower() == 'quit':
        break
