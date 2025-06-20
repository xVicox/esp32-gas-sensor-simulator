from datetime import datetime
from value_interpreter import ValueInterpreter


class Display:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Display, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, '_initialized'):

            # set to base values
            self.mq2_base_value = 350
            self.mq3_base_value = 400
            self.mq135_base_value = 600

            self._initialized = True

            self._value_interpreter = ValueInterpreter()

    # Will update the display based on new values coming from the sensor simulator (sensor_sim.py)
    def sensor_values_updated(self, mq2_reading, mq3_reading, mq135_reading):
        timestamp = datetime.now().strftime("%Y-%B-%d %H:%M:%S")
        mq2_change = mq2_reading - self.mq2_base_value
        mq3_change = mq3_reading - self.mq3_base_value
        mq135_change = mq135_reading - self.mq135_base_value

        mq2_risk_level = self._value_interpreter.interpret_values_for_mq2(mq2_reading).name
        mq3_risk_level = self._value_interpreter.interpret_values_for_mq3(mq3_reading).name
        mq135_risk_level = self._value_interpreter.interpret_values_for_mq135(mq135_reading).name

        reset_color = "\033[0m"

        print(timestamp)
        print("************************")
        print(f"{'Sensor':<8} {'Value':>8} {'Change':>8} {'Risk Level':>5}")
        print("-" * 35)
        print(f"{'MQ-2':<8} {mq2_reading:>8} {mq2_change:>+8} {self.get_colored_text(mq2_risk_level):>15}{reset_color}")
        print(f"{'MQ-3':<8} {mq3_reading:>8} {mq3_change:>+8} {self.get_colored_text(mq3_risk_level):>15}{reset_color}")
        print(f"{'MQ-135':<8} {mq135_reading:>8} {mq135_change:>+8} {self.get_colored_text(mq135_risk_level):>15}{reset_color}")
        print("-" * 35 + "\n")

        # updating previous base values
        self.mq2_base_value = mq2_reading
        self.mq3_base_value = mq3_reading
        self.mq135_base_value = mq135_reading

    @staticmethod
    def get_colored_text(risk_level):
        colors = {
            "SAFE": "\033[92m",
            "CAUTION": "\033[93m",
            "HAZARDOUS": "\033[95m",
            "CRITICAL": "\033[91m"
        }
        reset = "\033[0m"
        return f"{colors.get(risk_level, '')}{risk_level}{reset}"