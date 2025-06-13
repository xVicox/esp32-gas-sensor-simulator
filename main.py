from sensor_sim import SensorSim
from sensor_display import SensorDisplay
from alarm_handler import AlarmHandler
from time import sleep

if __name__ == '__main__':
    sim = SensorSim()
    display = SensorDisplay()
    alarm = AlarmHandler()

    sim.add_sensor_update_listener(display)
    sim.add_alarm_listener(alarm)

    while True:
        sim.notify_sensor_update_listeners(sim.simulate_mq2(), sim.simulate_mq3(), sim.simulate_mq135())
        sleep(1.5)