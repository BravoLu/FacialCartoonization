from moviepy.editor import *

video = VideoFileClip('teacher_ma.mp4')
audio = video.audio
audio.write_audiofile('teacher_ma.mp3')
