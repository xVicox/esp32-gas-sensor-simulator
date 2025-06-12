import random

class SensorSim:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SensorSim, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "_initialized"):
            # base values
            self.mq2_value = 800
            self.mq3_value = 400
            self.mq135_value = 600
            self._initialized = True

            self._listeners = []

    def add_listener(self, subscriber):
        for listener in self._listeners:
            if listener is subscriber:
                return
        self._listeners.append(subscriber)

    def notify_listeners(self, mq2_change, mq3_change, mq135_change):
        for sub in self._listeners:
            sub.sensor_values_updated(mq2_change, mq3_change, mq135_change)

    def simulate_mq2(self, min_value=200, max_value=3500):
        """
        MQ-2 sensor → Detects: general gas leaks (LPG, methane, propane, smoke)
        Typical ADC Range: 200–3500, natural drift ±5-15, spike range +1000 to +2000
        Base value set to 800

        Simulates an analog sensor reading for the MQ-2 gas sensor.
        This method generates a pseudo-random value that mimics real sensor behavior,
        including natural drift and occasional sudden spikes.

        Behavior:
        - 5% chance of a sudden spike to simulate gas leak events.
        - Otherwise, simulates a natural drift in the range of ±5 to ±15 units.
        - The resulting value is clamped to stay within the specified ADC range.

        Parameters:
            min_value (int): Minimum ADC value for the sensor reading (default is 200).
            max_value (int): Maximum ADC value for the sensor reading (default is 3500).

        Returns:
            int: Simulated sensor reading clamped within the given range.
        """
        # random spike
        if random.random() < 0.05:
            self.mq2_value += random.randint(1000,2000)
            return self.mq2_value

        drift = random.randint(5,15)
        plus_minus = random.choice([1, -1])

        # increase value
        if plus_minus == 1:
            self.mq2_value += drift
        # decrease value
        else:
            self.mq2_value -= drift

        if min_value <= self.mq2_value <= max_value:
            return self.mq2_value
        else:
            # Clamp the value -> return min/max values if the value of self.mq2_value exceeds min or max
            self.mq2_value = max(min_value, min(max_value, self.mq2_value))
            return self.mq2_value

    def simulate_mq3(self, min_value=100, max_value=3000):
        """
        MQ-3 sensor → Detects: alcohols, benzene, ethanol, VOCs (Volatile Organic Compounds)
        Typical ADC Range: 100-3000, natural drift ±5-20, spike range +800 to +1200
        Base value set to 400

        The MQ-3 sensor detects alcohols, benzene, ethanol, and various VOCs.
        This method generates a pseudo-random value that mimics real sensor behavior,
        including natural drift and occasional sudden spikes.

        Behavior:
        - Approximately 4% chance of a sudden spike (+800 to +1200 units) to simulate transient alcohol or VOC exposure.
        - Otherwise, simulates a natural drift in the range of ±5 to ±20 units.
        - The resulting value is clamped to stay within the specified ADC range.

        Parameters:
            min_value (int): Minimum ADC value for the sensor reading (default is 100).
            max_value (int): Maximum ADC value for the sensor reading (default is 3000).

        Returns:
            int: Simulated sensor reading clamped within the given range.
        """
        # random spike
        if random.random() < 0.04:
            self.mq3_value += random.randint(800, 1200)
            return self.mq3_value

        drift = random.randint(5, 20)
        plus_minus = random.choice([1, -1])

        # increase value
        if plus_minus == 1:
            self.mq3_value += drift
        # decrease value
        else:
            self.mq3_value -= drift

        if min_value <= self.mq3_value <= max_value:
            return self.mq3_value
        else:
            # Clamp the value -> return min/max values if the value of self.mq3_value exceeds min or max
            self.mq3_value = max(min_value, min(self.mq3_value, max_value))
            return self.mq3_value

    def simulate_mq135(self, min_value=150, max_value=3200):
        """
        MQ-135 sensor → Detects: alcohols, benzene, ethanol, VOCs (Volatile Organic Compounds)
        Typical ADC Range: 100-3000, natural drift ±5-20, spike range +800 to +1200
        Base value set to 400

        MQ-135 sensor detects various gases related to air pollution and indoor air quality,
        including benzene, ammonia, CO₂, alcohol, smoke, and general VOCs.
        This method mimics realistic behavior through natural value drift and occasional
        spikes representing sudden changes in air composition.

        Behavior:
        - ~5% chance of a sudden spike (+700 to +1300 units) to simulate a burst of polluted air.
        - Otherwise, applies a natural drift in the range of ±5 to ±25 units.
        - The final value is clamped to remain within the defined ADC range.

        Parameters:
            min_value (int): Minimum ADC value for the sensor reading (default is 150).
            max_value (int): Maximum ADC value for the sensor reading (default is 3200).

        Returns:
            int: Simulated sensor reading clamped within the given range.
        """
        # random spike
        if random.random() < 0.05:
            self.mq135_value += random.randint(700, 1300)
            return self.mq135_value

        drift = random.randint(5, 25)
        plus_minus = random.choice([1, -1])

        # increase value
        if plus_minus == 1:
            self.mq135_value += drift
        # decrease value
        else:
            self.mq135_value -= drift

        if min_value <= self.mq135_value <= max_value:
            return self.mq135_value
        else:
            # Clamp the value -> return min/max values if the value of self.mq135_value exceeds min or max
            self.mq135_value = max(min_value, min(self.mq135_value, max_value))
            return self.mq135_value