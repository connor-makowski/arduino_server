import pyfirmata
import time

board = pyfirmata.Arduino('/dev/ttyACM0')

it = pyfirmata.util.Iterator(board)
it.start()

green=board.digital[4]
red=board.digital[2]
board.digital[8].mode = pyfirmata.INPUT
btn=board.digital[8]

status=False
btn_status=False

def show_output(bool=True, wait=1):
    if bool:
        green.write(1)
        time.sleep(wait)
        green.write(0)
    else:
        red.write(1)
        time.sleep(wait)
        red.write(0)

while True:
    btn_current=btn.read()
    if btn_current:
        btn_status=btn_current
        status=1-status
        show_output(status)
    time.sleep(0.1)
