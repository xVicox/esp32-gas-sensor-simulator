from sensor_reader import SensorReader
from sensor_sim import SensorSim
from display import Display
from alarm_handler import AlarmHandler
from time import sleep

if __name__ == '__main__':
    sim = SensorSim()
    microcontroller_sim = SensorReader()
    display = Display()
    sound_alarm = AlarmHandler()

    sim.add_raw_values_listener(microcontroller_sim)
    microcontroller_sim.add_sensor_update_listener(display)
    microcontroller_sim.add_sensor_update_listener(sound_alarm)

    sim.run_simulation()