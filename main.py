from sensor_reader import SensorReader
from sensor_sim import SensorSim
from display import Display
from alarm_handler import AlarmHandler

if __name__ == '__main__':
    sim = SensorSim()
    microcontroller_sim = SensorReader()
    display = Display()
    sound_alarm = AlarmHandler()

    sim.add_raw_values_listener(microcontroller_sim)
    microcontroller_sim.add_raw_data_listeners(display)
    microcontroller_sim.add_alarm_data_listeners(sound_alarm)

    sim.run_simulation()