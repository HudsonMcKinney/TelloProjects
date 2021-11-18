from djitellopy import Tello
from time import sleep

tello = Tello()
tello.connect()
print(tello.get_battery())

feet = 30.48

tello.takeoff()
sleep(.5)
tello.move_up(round(3*feet))
sleep(.5)
tello.move_forward(round(5*feet))
sleep(.5)
tello.rotate_counter_clockwise(90)
sleep(.5)
# first straight


tello.move_forward(round(6*feet))
sleep(.5)
tello.rotate_clockwise(90)
sleep(.5)
# 2nd straight

tello.move_down(round(3*feet))
sleep(.5)
tello.move_forward(round(3*feet))
sleep(.5)
tello.rotate_clockwise(90)
sleep(.5)
# 3rd straight

tello.move_up(round(1*feet))
sleep(.5)
tello.move_forward(round(3*feet))
sleep(.5)
tello.rotate_counter_clockwise(90)
sleep(.5)
# 4th straight

tello.move_forward(round(6*feet))
sleep(.5)
tello.land()
# 5th straight
