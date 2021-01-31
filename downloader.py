# sudo apt-get install ffmpeg

import os
import pafy
import shutil
from pydub import AudioSegment as convert

SONGS_FILE = "canciones.txt"
MUSIC_FOLDER = "musica"
MUSIC_TEMP_FOLDER = "musica/temp"

if not os.path.exists(SONGS_FILE):
    print("Creando fichero para las canciones (" + SONGS_FILE + ")....")
    document = open(SONGS_FILE, 'w')
    print("Pega todas las URL de youtube en este fichero.")
    document.close()

if os.path.exists(MUSIC_FOLDER):
    if os.path.exists(MUSIC_TEMP_FOLDER):
        pass
    else:
        os.mkdir(MUSIC_TEMP_FOLDER)
else:
    os.mkdir(MUSIC_FOLDER)
    os.mkdir(MUSIC_TEMP_FOLDER)

document = open(SONGS_FILE, 'r')
music_list = document.readlines()
document.close()
error_list = []

print("Descargando canciones...")
for music in music_list:
    try:
        url = music
        video = pafy.new(url)
        bestaudio = video.getbestaudio()
        bestaudio.download(filepath=MUSIC_TEMP_FOLDER)
    except:
        error_list.append("Error descargando: " + music)

print("Converting to mp3.....")
for filename in os.listdir(MUSIC_TEMP_FOLDER):
    name = os.path.splitext(filename)
    try:
        audio = convert.from_file(MUSIC_TEMP_FOLDER + filename)
        audio.export(MUSIC_FOLDER + '/' + name[0] + '.mp3', format="mp3", bitrate="160k")
    except:
        error_list.append("Error convirtiendo: " + name[0])
shutil.rmtree(MUSIC_TEMP_FOLDER)

for error in error_list:
    print(error)

print("¡Terminado con éxito! ¡A disfrutar!")
