from pygame import mixer
import time


def play_to_mic():
	mixer.init(devicename='Микрофон (Realtek(R) Audio)')
	mixer.music.load('o-privet.mp3')
	mixer.music.set_volume(0.4)
	mixer.music.play()
	while mixer.music.get_busy():
		time.sleep(0.1)


if __name__ == '__main__':
	play_to_mic()
