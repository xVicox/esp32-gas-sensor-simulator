from sensor_sim import SensorSim
from sensor_display import SensorDisplay
from time import sleep

if __name__ == '__main__':
    sim = SensorSim()
    display = SensorDisplay()

    while True:
        mq2_reading = sim.simulate_mq2()
        mq3_reading = sim.simulate_mq3()
        mq135_reading = sim.simulate_mq135()

        display.display(mq2_reading, mq3_reading, mq135_reading)

        sleep(1.5)