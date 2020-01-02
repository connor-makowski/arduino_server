from app import app
from flask import jsonify, request, abort, make_response
import pyfirmata

board = pyfirmata.Arduino('/dev/ttyACM0')

it = pyfirmata.util.Iterator(board)
it.start()

green=board.digital[4]
red=board.digital[2]
board.digital[8].mode = pyfirmata.INPUT

green_status=False
red_status=False

@app.route('/green', methods = ['GET'])
def green_toggle():
    global green_status
    btn_status=board.digital[8].read()
    if not btn_status:
        green_status=1-green_status
        green.write(green_status)
        return jsonify({'status':green_status, 'btn':btn_status})
    else:
        return jsonify({'status':green_status, 'btn':btn_status})

@app.route('/red', methods = ['GET'])
def red_toggle():
    global red_status
    btn_status=board.digital[8].read()
    if not btn_status:
        red_status=1-red_status
        red.write(red_status)
        return jsonify({'status':red_status, 'btn':btn_status})
    else:
        return jsonify({'status':red_status, 'btn':btn_status})
