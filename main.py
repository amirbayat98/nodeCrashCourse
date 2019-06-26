import serial
import time

flag_serial = False

# from flask import Flask, jsonify, render_template, request, send_from_directory
from random import *
import threading
import time

# app = Flask(__name__, static_folder="templates/digital/build/static", template_folder='templates/digital/build')
# app = Flask(__name__, template_folder="templates1")


nodFlag = False
direction = ""

ser1 = serial.Serial(port='/dev/ttyS0')
ser1.baudrate = 115200

try:
    ser = serial.Serial('/dev/ttyUSB0')
except serial.serialutil.SerialException:
    flag_serial = False

if flag_serial:
    ser.baudrate = 38400
    print(ser.name)
data = [0] * 9
max_speed = 150
output_speedR = 0
output_speedL = 0
speed_step = 3 * 3
speed_stepR = 15 * 3
speed_stepB = 1 * 3


# @app.route('/')
# def direction():
#    # return direction
#    global direction
#    direction = request.args.get('direction')
#    print(direction)
#    #dir()
#    if flag_serial:
#        for i in range(9):
#            data[i] = float(ser.readline().decode().strip())
#        print(data[8])
#    return render_template('ugv.html')


# @app.route('/', methods=['POST'])
# def direction1():
#     print('goh')
#     direction = request
#     print(direction)
#     return ("an")

def dir():
    global output_speedR, output_speedL
    if direction == "w":
        if (output_speedR < max_speed):
            if output_speedR < 0:
                output_speedR += speed_stepR
            else:
                output_speedR += speed_step
        if (output_speedL < max_speed):
            if output_speedL < 0:
                output_speedL += speed_stepR
            else:
                output_speedL += speed_step
        if flag_serial:
            ser.write(("S" + str(output_speedR) + " " + str(output_speedL) + '\n').encode())

    elif direction == "h":
        output_speedL, output_speedR = 0, 0
        if flag_serial:
            ser.write(("S" + str(output_speedR) + " " + str(output_speedL) + '\n').encode())

    elif direction == "s":
        if (-output_speedR < max_speed):
            if output_speedR > 0:
                output_speedR -= speed_stepR
            else:
                output_speedR -= speed_step
        if (-output_speedL < max_speed):
            if output_speedL > 0:
                output_speedL -= speed_stepR
            else:
                output_speedL -= speed_step
        if flag_serial:
            ser.write(("S" + str(output_speedR) + " " + str(output_speedL) + '\n').encode())

    elif direction == "a":
        if (output_speedR < max_speed):
            output_speedR += speed_step
        if (-output_speedL < max_speed):
            output_speedL -= speed_step
        if flag_serial:
            ser.write(("S" + str(output_speedR) + " " + str(output_speedL) + '\n').encode())

    elif direction == "d":
        if (-output_speedR < max_speed):
            output_speedR -= speed_step
        if (output_speedL < max_speed):
            output_speedL += speed_step
        if flag_serial:
            ser.write(("S" + str(output_speedR) + " " + str(output_speedL) + '\n').encode())

    elif direction=="q":
        if(output_speedR < max_speed):
            output_speedR += speed_step
        if(output_speedL < max_speed):
            output_speedL += speed_stepB
        if flag_serial:
            ser.write(("S" + str(output_speedR) + " " + str(output_speedL) + '\n').encode())

    elif direction=="e":
        if(output_speedR < max_speed):
            output_speedR += speed_stepB
        if(output_speedL < max_speed):
            output_speedL += speed_step
        if flag_serial:
            ser.write(("S" + str(output_speedR) + " " + str(output_speedL) + '\n').encode())

    else:
        if flag_serial:
            ser.write(("S0 0\n").encode())

    print(output_speedR, output_speedL)

    time.sleep(0.1)


while (True):
    global direction
    direc = ser1.readline()
    print(direc)
    if(direc == b'w\n'):
        direction = 'w'
    elif(direc == b'q\n'):
        direction = 'q'
    elif(direc == b'e\n'):
        direction = 'e'
    elif(direc == b'a\n'):
        direction = 'a'
    elif(direc == b's\n'):
        direction = 's'
    elif(direc == b'd\n'):
        direction = 'd'
    elif(direc == b'h\n'):
        direction = 'h'
    dir()
    dataToSend = ""
    for i in range(9):
        data[i] = float(ser.readline().decode().strip())
        dataToSend += str(data[i])
        if i < 8:
            dataToSend += "*"
        dataToSend += "R"
    ser1.write(dataToSend)
    print("sent")

# if __name__ == '__main__':
#    if flag_serial:
#        ser.write("R0 0\n".encode())
#    app.debug = True
#    app.run(use_reloader=True, host='0.0.0.0', port=5000)
