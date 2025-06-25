import pygame
import os

class AlarmHandler:
    """
    Handles sound alerts for sensor events such as spikes or changes in detected gas levels
    Uses pygame to play pre-defined sound files corresponding to each type of alert.
    """
    def __init__(self):
        pygame.mixer.init()

        self._sounds = {
            "caution": "resources/sounds/caution_beep.mp3",
            "hazardous": "resources/sounds/hazardous_beep.mp3",
            "critical": "resources/sounds/critical_beep.mp3",
            "spike": "resources/sounds/spike_beep.mp3"
        }

    def spike_in_value_registered(self, device):
        AlarmHandler.play_alarm_sound(self, "spike")

    def caution_level_reached(self, device):
        AlarmHandler.play_alarm_sound(self,"caution")

    def hazardous_level_reached(self, device):
        AlarmHandler.play_alarm_sound(self,"hazardous")

    def critical_level_reached(self, device):
        AlarmHandler.play_alarm_sound(self,"critical")

    def play_alarm_sound(self, alarm_type):
        """
        Plays the sound corresponding to the given alarm type.
        Args:
            alarm_type (str): One of 'caution', 'hazardous', 'critical', or 'spike'.
        """
        path = self._sounds[alarm_type]
        if os.path.exists(path):
            pygame.mixer.Sound(path).play()
        else:
            print(f"Missing sound file for alarm type: {alarm_type}!")