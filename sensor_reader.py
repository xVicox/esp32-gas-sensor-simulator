class SensorReader:

    def __init__(self):
        # base values
        self._mq2_value = 350
        self._mq3_value = 400
        self._mq135_value = 600

        self._listeners = []

    def sensor_values_updated(self, mq2_change, mq3_change, mq135_change):
        self._mq2_value = mq2_change
        self._mq3_value = mq3_change
        self._mq135_value = mq135_change

        self.notify_display_listeners()

    def add_sensor_update_listener(self, subscriber):
        for listener in self._listeners:
            if listener is subscriber:
                return
        self._listeners.append(subscriber)

    def notify_display_listeners(self):
        for display_listener in self._listeners:
            display_listener.sensor_values_updated(self._mq2_value, self._mq3_value, self._mq135_value)