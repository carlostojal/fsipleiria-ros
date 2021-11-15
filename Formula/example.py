from time import time
from Formula import Controls

controls = Controls.Controls()

controls.STEP_TIME = 0.1

controls.steering(-0.5, time=2)
controls.steering(0.5, time=2)
controls.throttle(0.76)
controls.brake(0.10)
controls.clutch(0.65)