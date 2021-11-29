from djitellopy import Tello
from time import sleep

# drone start sequence 
tello = Tello()
tello.connect()
print(tello.get_battery())

# converts centimeters into feet
feet = 30.48

# drone moves up, moves forward, then turns
tello.takeoff()
sleep(.5)
tello.move_up(round(3.333*feet))
sleep(.5)
tello.move_forward(round(5*feet))
sleep(.5)
tello.rotate_counter_clockwise(90)
sleep(.5)
# first straight

# drone moves forward and turns
tello.move_forward(round(6*feet))
sleep(.5)
tello.rotate_clockwise(90)
sleep(.5)
# 2nd straight

# drone moves down, then forward, then turns
tello.move_down(round(3*feet))
sleep(.5)
tello.move_forward(round(3*feet))
sleep(.5)
tello.rotate_clockwise(90)
sleep(.5)
# 3rd straight

# Drone moves up, then moves forward, then turns
tello.move_up(round(1*feet))
sleep(.5)
tello.move_forward(round(3*feet))
sleep(.5)
tello.rotate_counter_clockwise(90)
sleep(.5)
# 4th straight

# drone moves forward and lands
tello.move_forward(round(6*feet))
sleep(.5)
tello.land()
# 5th straight
