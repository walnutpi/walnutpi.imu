from walnutpi_imu import direction
import time

while True:
    time.sleep(0.5)
    print(direction.get_lcd())