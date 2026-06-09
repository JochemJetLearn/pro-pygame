import time

class Gif:
    def __init__(self, images=[], time_between_frames=1, sound=None):
        self.images = images
        self.time = time_between_frames
        self.frame = 1
        self.start_time = None
        self.running = False
        self.sound = sound
        self.repeat = True

    def start(self):
        if not self.sound == None:
            self.sound.play()
        self.running = True
        self.start_time = time.time()
        return self
    
    def draw(self, surface):
        if not self.running:
            return None
        frame = (time.time() - self.start_time) // self.time % len(self.images)
        surface.blit(self.images[frame.__floor__()], (0, 0))
        return frame

