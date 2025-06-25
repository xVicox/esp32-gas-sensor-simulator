import value_interpreter
from value_interpreter import GasLevel

class SensorReader:
    """
    Acts as a middle layer between simulated or physical sensors and the rest of the system.
    Responsible for:
     - Storing current and previous sensor readings.
     - Interpreting risk levels.
     - Detecting sudden spikes.
     - Notifying display and alarm listeners based on changes in data.
     """
    def __init__(self):
        # set to base values
        self._mq2_base_value = 350
        self._mq3_base_value = 400
        self._mq135_base_value = 600

        self._mq2_value = 0
        self._mq3_value = 0
        self._mq135_value = 0

        self._sensor_values = {
            "MQ-2": self._mq2_value,
            "MQ-3": self._mq3_value,
            "MQ-135": self._mq135_value
        }

        self._sensor_risk_levels = {
            "MQ-2": value_interpreter.ValueInterpreter.interpret_values_for_mq2,
            "MQ-3": value_interpreter.ValueInterpreter.interpret_values_for_mq3,
            "MQ-135": value_interpreter.ValueInterpreter.interpret_values_for_mq135,
        }

        self._previous_risk_levels = {
            "MQ-2": GasLevel.SAFE,
            "MQ-3": GasLevel.SAFE,
            "MQ-135": GasLevel.SAFE
        }

        self._display_listeners = []
        self._alarm_data_listeners = []

    def sensor_values_updated(self, mq2_reading, mq3_reading, mq135_reading):
        """
        Called when new sensor readings come in. Updates internal values,
        checks for spikes, interprets risk levels, and notifies registered listeners
        if thresholds are crossed or levels change.

        Args:
            mq2_reading (int): The current ADC value from the MQ-2 sensor.
            mq3_reading (int): The current ADC value from the MQ-3 sensor.
            mq135_reading (int): The current ADC value from the MQ-135 sensor.
        """
        self._mq2_value = mq2_reading
        self._mq3_value = mq3_reading
        self._mq135_value = mq135_reading

        self._sensor_values["MQ-2"] = self._mq2_value
        self._sensor_values["MQ-3"] = self._mq3_value
        self._sensor_values["MQ-135"] = self._mq135_value

        # detect spikes notify alarm handler
        self.notify_alarm_data_listeners_on_spike_event()

        # update base values
        self._mq2_base_value = self._mq2_value
        self._mq3_base_value = self._mq3_value
        self._mq135_base_value = self._mq135_value

        # Interpret values for alarm handler
        for sensor_name in self._sensor_risk_levels:
            value = self._sensor_values[sensor_name]
            interpreter = self._sensor_risk_levels[sensor_name]
            risk_level = interpreter(value).name

            # notify alarm listeners on risk level changes
            if risk_level == "CAUTION" or risk_level == "HAZARDOUS" or risk_level == "CRITICAL":
                ####
                if self._previous_risk_levels[sensor_name] == GasLevel[risk_level]:
                    continue
                else:
                    self._previous_risk_levels[sensor_name] = GasLevel[risk_level]
                    self.notify_alarm_data_listeners_on_risk_level_change(sensor_name, risk_level)

        # notify displays
        self.notify_raw_data_listeners()

    def add_raw_data_listeners(self, subscriber):
        for listener in self._display_listeners:
            if listener is subscriber:
                return
        self._display_listeners.append(subscriber)

    def notify_raw_data_listeners(self):
        for display_listener in self._display_listeners:
            # Notify display
            display_listener.sensor_values_updated(self._mq2_value, self._mq3_value, self._mq135_value)

    def add_alarm_data_listeners(self, subscriber):
        for listener in self._alarm_data_listeners:
            if listener is subscriber:
                return
        self._alarm_data_listeners.append(subscriber)

    def notify_alarm_data_listeners_on_risk_level_change(self, device, risk_level):
        for listener in self._alarm_data_listeners:
            if risk_level == "CAUTION":
                listener.caution_level_reached(device)
            if risk_level == "HAZARDOUS":
                listener.hazardous_level_reached(device)
            if risk_level == "CRITICAL":
                listener.critical_level_reached(device)

    def notify_alarm_data_listeners_on_spike_event(self):
        for listener in self._alarm_data_listeners:
            # SPIKE NOTIFS
            if self._mq2_value - self._mq2_base_value >= 200:
                listener.spike_in_value_registered("MQ-2")
            if self._mq3_value - self._mq3_base_value >= 200:
                listener.spike_in_value_registered("MQ-3")
            if self._mq135_value - self._mq135_base_value >= 200:
                listener.spike_in_value_registered("MQ-135")