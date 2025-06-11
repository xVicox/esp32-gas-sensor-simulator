from datetime import datetime

class SensorDisplay:

    def __init__(self):
        # set to base values
        self.mq2_prev_value = 800
        self.mq3_prev_value = 400
        self.mq135_prev_value = 600

    def display(self, mq2_reading, mq3_reading, mq135_reading):
        print(datetime.now().strftime("%Y-%B-%d %H:%M:%S"))
        print(f"MQ-2: {mq2_reading} ({mq2_reading - self.mq2_prev_value})")
        print(f"MQ-3: {mq3_reading} ({mq3_reading - self.mq3_prev_value})")
        print(f"MQ-135: {mq135_reading} ({mq135_reading - self.mq135_prev_value})")
        print("-----------------------------------")