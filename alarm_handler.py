import pygame
import os

class AlarmHandler:

    def __init__(self):
        pygame.mixer.init()

        self._sounds = {
            "caution": "resources/sounds/caution_beep.mp3",
            "hazardous": "resources/sounds/hazardous_beep.mp3",
            "critical": "resources/sounds/critical_beep.mp3",
            "spike": "resources/sounds/spike_beep.mp3"
        }

    @staticmethod
    def caution_level_reached():
        pass

    @staticmethod
    def hazardous_level_reached():
        pass

    @staticmethod
    def critical_level_reached():
        pass

    def spike_in_value_registered(self):
        path = self._sounds["spike"]
        if os.path.exists(path):
            pygame.mixer.Sound(path).play()
        else:
            print("One of the sensors registered a value spike!")