from datetime import datetime

from value_interpreter import ValueInterpreter

class SensorParser:
    """Parses sensor readings and formats them for display and logging."""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SensorParser, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, '_initialized'):

            # set to base values
            self.mq2_base_value = 350
            self.mq3_base_value = 400
            self.mq135_base_value = 600

            self._initialized = True

            self._value_interpreter = ValueInterpreter()

            self._log_string = {}
            self._display_string = ""

    def sensor_values_updated(self, mq2_reading, mq3_reading, mq135_reading):
        """
        Updates sensor values and computes risk, change, and formatted output.

        Args:
            mq2_reading (int): Current MQ-2 sensor value.
            mq3_reading (int): Current MQ-3 sensor value.
            mq135_reading (int): Current MQ-135 sensor value.
        """
        timestamp = datetime.now()
        mq2_change = mq2_reading - self.mq2_base_value
        mq3_change = mq3_reading - self.mq3_base_value
        mq135_change = mq135_reading - self.mq135_base_value

        mq2_risk_level = self._value_interpreter.interpret_values_for_mq2(mq2_reading).name
        mq3_risk_level = self._value_interpreter.interpret_values_for_mq3(mq3_reading).name
        mq135_risk_level = self._value_interpreter.interpret_values_for_mq135(mq135_reading).name

        data_dict = {
            "timestamp": timestamp,
            "readings": {
                "MQ2": {"value":mq2_reading, "change":mq2_change, "risk":mq2_risk_level},
                "MQ3": {"value":mq3_reading, "change":mq3_change, "risk":mq3_risk_level},
                "MQ135": {"value":mq135_reading, "change":mq135_change, "risk":mq135_risk_level}
            }
        }

        self._log_string = SensorParser.get_log_string(data_dict)
        self._display_string = SensorParser.get_display_string(data_dict)

        # updating previous base values
        self.mq2_base_value = mq2_reading
        self.mq3_base_value = mq3_reading
        self.mq135_base_value = mq135_reading

    @property
    def display_string(self):
        return self._display_string

    @property
    def log_string(self):
        return self._log_string

    @staticmethod
    def get_log_string(data):
        """ Formats a data dictionary into a compact log-friendly string. """
        timestamp = data['timestamp'].strftime("%Y%m%d_%H%M%S")
        log_string = (
            f"{timestamp}"
            f"|MQ2_{data['readings']['MQ2']['value']}_{data['readings']['MQ2']['change']}_{data['readings']['MQ2']['risk']}"
            f"|MQ3_{data['readings']['MQ3']['value']}_{data['readings']['MQ3']['change']}_{data['readings']['MQ3']['risk']}"
            f"|MQ135_{data['readings']['MQ135']['value']}_{data['readings']['MQ135']['change']}_{data['readings']['MQ135']['risk']}"
        )
        return log_string

    @staticmethod
    def get_display_string(data):
        """ Formats a data dictionary into a human-readable display string. """

        timestamp = data['timestamp'].strftime("%d-%B-%Y %H:%M:%S")
        display_string = (
            f"{timestamp}\n"
            f"************************\n"
            f"{'Sensor':<8} {'Value':>8} {'Change':>8} {'Risk Level':>15}\n"
            + "-" * 35 + "\n"
            + f"{'MQ-2':<8} {data['readings']['MQ2']['value']:>8} {data['readings']['MQ2']['change']:>+8} {data['readings']['MQ2']['risk']:>15}\n"
            + f"{'MQ-3':<8} {data['readings']['MQ3']['value']:>8} {data['readings']['MQ3']['change']:>+8} {data['readings']['MQ3']['risk']:>15}\n"
            + f"{'MQ-135':<8} {data['readings']['MQ135']['value']:>8} {data['readings']['MQ135']['change']:>+8} {data['readings']['MQ135']['risk']:>15}\n"
            + "-" * 35 + "\n"
        )
        return display_string