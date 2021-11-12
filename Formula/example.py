from Controls import Controls

controls = Controls()

# 10400 -> 20

for i in range(0, 1):
    controls.throttle(0.76)
    controls.brake(0.10)
    controls.clutch(0.65)