from controller import Robot

TIME_STEP = 64
MAX_SPEED=6.28
robot = Robot()
ds = []
dsNames = ['ds_right', 'ds_left']
for i in range(2):
    ds.append(robot.getDevice(dsNames[i]))
    ds[i].enable(TIME_STEP)
wheels = []
wheelsNames = ['wheel1', 'wheel2', 'wheel3', 'wheel4']
for i in range(4):
    wheels.append(robot.getDevice(wheelsNames[i]))
    wheels[i].setPosition(float('inf'))
    wheels[i].setVelocity(0.0)
avoidObstacleCounter = 0
while robot.step(TIME_STEP) != -1:
    leftSpeed = MAX_SPEED
    rightSpeed = MAX_SPEED
    if avoidObstacleCounter > 0:
        avoidObstacleCounter -= 1
        leftSpeed = MAX_SPEED
        rightSpeed = -MAX_SPEED
    else:
        for i in range(2):
            if ds[i].getValue() < 950.0:
                avoidObstacleCounter = 100
    wheels[0].setVelocity(leftSpeed)
    wheels[1].setVelocity(rightSpeed)
    wheels[2].setVelocity(leftSpeed)
    wheels[3].setVelocity(rightSpeed)