from djitellopy import Tello
from time import sleep

tello = Tello()
tello.connect()
print(tello.get_battery())

feet = 31

tello.takeoff()
sleep(.5)
tello.move_up(3*feet)
sleep(.5)
tello.move_forward(5*feet)
sleep(.5)
tello.rotate_counter_clockwise(90)
sleep(.5)
# first straight


tello.move_forward(6*feet)
sleep(.5)
tello.rotate_clockwise(90)
sleep(.5)
# 2nd straight

tello.move_down(3*feet)
sleep(.5)
tello.move_forward(3*feet)
sleep(.5)
tello.rotate_clockwise(90)
sleep(.5)
# 3rd straight

tello.move_up(1*feet)
sleep(.5)
tello.move_forward(3*feet)
sleep(.5)
tello.rotate_counter_clockwise(90)
sleep(.5)
# 4th straight

tello.move_forward(6*feet)
sleep(.5)
tello.land()
# 5th straight
