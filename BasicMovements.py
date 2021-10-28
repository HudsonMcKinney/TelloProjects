from djitellopy import Tello
from time import sleep

tello = Tello()

tello.connect()

tello.move_up(90)

sleep(0.25)

tello.move_forward(100)

sleep(0.25)

tello.move_right(100)

sleep(0.25)

tello.move_back(100)

sleep(0.25)

tello.move_left(100)

sleep(0.25)

tello.flip_forward()

sleep(0.25)

tello.land()
tello.end()
