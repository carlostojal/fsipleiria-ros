from Formula import Controls, DataAcquisition

"""
controls = Controls.Controls()

controls.steering(-0.5, update_time=2)
controls.steering(0.5, update_time=2)
controls.throttle(0.76)
controls.brake(0.10)
controls.clutch(0.65)
"""

data_acquisition = DataAcquisition.DataAcquisition()

print(data_acquisition.getEngineRPM())