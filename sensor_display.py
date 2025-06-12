from datetime import datetime

class SensorDisplay:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SensorDisplay, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, '_initialized'):

            # set to base values
            self.mq2_prev_value = 800
            self.mq3_prev_value = 400
            self.mq135_prev_value = 600

            self._initialized = True

    # Will update the display based on new values coming from the sensor simulator (sensor_sim.py)
    def sensor_values_updated(self, mq2_reading, mq3_reading, mq135_reading):
        print(datetime.now().strftime("%Y-%B-%d %H:%M:%S"))
        print("*********************")
        print(f"MQ-2: {mq2_reading} ({mq2_reading - self.mq2_prev_value})")
        print(f"MQ-3: {mq3_reading} ({mq3_reading - self.mq3_prev_value})")
        print(f"MQ-135: {mq135_reading} ({mq135_reading - self.mq135_prev_value})")
        print("-----------------------------------")
         # updating previous values
        self.mq2_prev_value = mq2_reading
        self.mq3_prev_value = mq3_reading
        self.mq135_prev_value = mq135_reading