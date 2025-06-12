from sensor_sim import SensorSim
from sensor_display import SensorDisplay
from time import sleep

if __name__ == '__main__':
    sim = SensorSim()
    display = SensorDisplay()

    sim.add_listener(display)

    while True:
        sim.notify_listeners(sim.simulate_mq2(), sim.simulate_mq3(), sim.simulate_mq135())
        sleep(1.5)