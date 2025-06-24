class LogHandler:
    def __init__(self):
        print("Init Log Handler")

    def sensor_values_updated(self, mq2_reading, mq3_reading, mq135_reading):
        print(f"FROM LOG HANDLER:\n"
              f"---->mq2: {mq2_reading}\n"
              f"---->mq3: {mq3_reading}\n"
              f"---->mq135: {mq135_reading}\n")
