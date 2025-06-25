from sensor_parser import SensorParser

class Display:
    """ Handles displaying sensor data to the console """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Display, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, '_initialized'):
            self._sensor_parser = SensorParser()
            self._initialized = True

    def sensor_values_updated(self, mq2_reading, mq3_reading, mq135_reading):
        """ Updates sensor readings and prints the formatted display string. """
        self._sensor_parser.sensor_values_updated(mq2_reading,mq3_reading,mq135_reading)
        self.emit_to_display()

    def emit_to_display(self):
        """ Prints the current formatted sensor data to the console. """
        print(self._sensor_parser.display_string)