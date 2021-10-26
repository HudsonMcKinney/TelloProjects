from djitellopy import Tello

tello = Tello()

tello.move_up(90)
tello.move_forward(100)
tello.move_right(100)
tello.move_back(100)
tello.move_left(100)

tello.flip_forward()

tello.land()
tello.end()
