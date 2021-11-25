from Formula import Controls, DataAcquisition

controls = Controls.Controls()
data_acquisition = DataAcquisition.DataAcquisition()

controls.steering(-0.5)
controls.steering(0.5)
controls.throttle(0.76)
controls.brake(0.10)

def engine_speed_callback(speed):

    print(speed)

# this gets the most recent enfine speed value
print(data_acquisition.getEngineRPM())

# this will be called on each engine speed update
data_acquisition.listenEngineRPM(engine_speed_callback)