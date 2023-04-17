import pygame

def init():
    pygame.init()
    pygame.mixer.init()

def load(filename):
    pygame.mixer.music.load(filename)

def play(start = 0.0):
    pygame.mixer.music.play(start=start)

def play_at_frame(video_frameid = 0, fps = 30):
    start = video_frameid / fps
    play(start=start)

def get_busy():
    return pygame.mixer.music.get_busy()

def unload():
    pygame.mixer.music.unload()
