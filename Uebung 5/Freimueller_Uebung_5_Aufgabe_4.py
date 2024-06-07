playlist = [
    {
        "titel": "Bohemian Rhapsody",
        "interpret": "Queen",
        "genre": "Rock"
    },
    {
        "titel": "Shape of You",
        "interpret": "Ed Sheeran",
        "genre": "Pop"
    },
    {
        "titel": "Billie Jean",
        "interpret": "Michael Jackson",
        "genre": "Pop"
    },
    {
        "titel": "Hotel California",
        "interpret": "Eagles",
        "genre": "Rock"
    },
    {
        "titel": "Rolling in the Deep",
        "interpret": "Adele",
        "genre": "Soul"
    },
    {
        "titel": "Smells Like Teen Spirit",
        "interpret": "Nirvana",
        "genre": "Grunge"
    },
    {
        "titel": "Blinding Lights",
        "interpret": "The Weeknd",
        "genre": "Synthpop"
    },
    {
        "titel": "Hey Jude",
        "interpret": "The Beatles",
        "genre": "Rock"
    },
    {
        "titel": "Lose Yourself",
        "interpret": "Eminem",
        "genre": "Hip-Hop"
    },
    {
        "titel": "Imagine",
        "interpret": "John Lennon",
        "genre": "Pop"
    },
    {
        "titel": "Hallelujah",
        "interpret": "Leonard Cohen",
        "genre": "Folk"
    },
    {
        "titel": "Stairway to Heaven",
        "interpret": "Led Zeppelin",
        "genre": "Rock"
    }
]

genres = dict()

for song in playlist:
    genre = song["genre"]

    if genre in genres:
        genres[genre] = genres[genre] + 1
    else:
        genres[genre] = 1

# Es gibt zwei Möglichkeiten, die maximale Häufigkeit auszulesen.
# Weg 1 ist quasi 'brute force' und geht alle Entries durch,
# Weg 2 ist elegant und holt sich den Max-Value.

# Die offensichtliche Schwäche beider Algorithmen ist klarerweisen,
# dass, wenn zwei oder mehr Genres dieselbe maximalen Häufigkeiten
# aufweisen, mehr oder minder der Zufall entscheidet, welches Genre 
# ausgegeben wird (de facto wäre es jeweils der erste Entry, der
# die maximale Häufigkeit ausweist - in beiden Fällen).

elegant = True

if elegant:
    max_occurance = max(genres.values())
    most_common_genre = list(genres.keys())[list(genres.values()).index(max_occurance)]
else:
    most_common_genre = ""
    most_common_genre_occurances = 0

    for genre in genres:
        if genres[genre] > most_common_genre_occurances:
            most_common_genre_occurances = genres[genre]
            most_common_genre = genre

print("Die Anzahl der Lieder:", len(playlist))
print("Eindeutige Genres:", sorted(genres.keys()))
print("Beliebtester Genre:", most_common_genre)