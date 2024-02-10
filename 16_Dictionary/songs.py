violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

songs_quantity = int(input('How much songs ? '))
minutes = 0

for _ in range(songs_quantity):
    song_name = input('Enter song name: ')
    # minutes += violator_songs.get(song_name, 0)
    minutes += violator_songs[song_name]

print('Total minutes:', round(minutes, 2))