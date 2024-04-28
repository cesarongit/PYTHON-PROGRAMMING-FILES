import moviepy.editor as me

video = me.VideoFileClip('abc.mp4')

audio = video.audio

audio.write_audiofile('abc.mp3')