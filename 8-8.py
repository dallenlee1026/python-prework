def make_album(artist, title, year, genre, tracks=''):
    """Create a dictionary for an album with metadata."""
    album = {'artist': artist, 'title': title,
             'year': year, 'genre': genre}
    return album


while True:
    print("\nPlease enter an album")
    print("or enter 'quit' when finished")

    artist_name = input("Artist: ")
    if artist_name == 'quit':
        break

    album_title = input("Title: ")
    album_year = input("Year release: ")
    album_genre = input("Genre: ")
    album_tracks = input("Number of Tracks on the Album: ")

    album_info = make_album(artist_name, album_title,
                            album_year, album_genre)
    if album_tracks:
        album_info['tracks'] = album_tracks

    print(album_info)
