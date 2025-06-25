import os

from sensor_parser import SensorParser

class LogHandler:
    """ Handles logging sensor data to a file """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(LogHandler, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, '_initialized'):
            self._sensor_parser = SensorParser()
            self._initialized = True

    def sensor_values_updated(self, mq2_reading, mq3_reading, mq135_reading):
        """ Updates sensor readings and appends the formatted log string to file. """
        self._sensor_parser.sensor_values_updated(mq2_reading, mq3_reading, mq135_reading)
        self.save_data_to_log()

    def save_data_to_log(self):
        """ Writes the latest log string to the log file, creating folders if needed. """
        log_string = self._sensor_parser.log_string
        os.makedirs("resources/log", exist_ok=True)
        with open("resources/log/log.txt", "a") as file:
            file.write(log_string + "\n")