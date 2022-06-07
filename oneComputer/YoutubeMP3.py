from youtube_dl import YoutubeDL
from pydub import AudioSegment
from os import remove as r

audio_downloder = YoutubeDL({'format':'bestaudio'})

link_to_youtube_video = 'https://www.youtube.com/watch?v=gVhC9R6qeGs'

data = audio_downloder.extract_info(link_to_youtube_video)

filename = data["title"]+"-"+data["id"]

webm_audio = AudioSegment.from_file(filename+".wav", format="wav")

webm_audio.export(filename+".mp3", format="mp3")

r(filename+".wav")