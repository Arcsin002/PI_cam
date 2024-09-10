import RPi.GPIO as GPIO
from time import sleep
import sys
import os
from flask import Flask, render_template, request

app = Flask(__name__)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)


# servo setup on specified GPIO pin
class servo(object):

    # Start the servo at 0 power
    def __init__(self, pin, min_angle, mid_angle, max_angle):
        self.pin = pin
        self.angle = None
        self.min_angle = min_angle
        self.mid_angle = mid_angle
        self.max_angle = max_angle
        GPIO.setup(self.pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pin, 50)
        self.pwm.start(0)
        
    # Sets the angle of the servo
    def setangle(self, angle):
        if angle > self.max_angle:
            angle = self.max_angle
        if angle < self.min_angle:
            angle = self.min_angle
        duty = angle / 18 + 2
        GPIO.output(self.pin, True)
        self.pwm.ChangeDutyCycle(duty)
        sleep(.33)
        GPIO.output(self.pin, False)
        self.pwm.ChangeDutyCycle(0)
        self.angle = angle
        
    def getangle(self):
        return self.angle
        
    # Runs the startup sequence
    def startup(self):
        self.setangle(self.min_angle)
        sleep(1)
        self.setangle(self.max_angle)
        sleep(1)
        self.setangle(self.mid_angle)
        sleep(1)
        self.angle = self.mid_angle
        
    # Resets the servo to 0 angle and stops it
    def reset(self):
        self.setangle(self.mid_angle)
        self.angle = self.mid_angle
        
    # Stops servo for exiting
    def stop(self):
        self.reset()
        self.pwm.stop()
    
    
# Accept pan/tilt commands via web requests
@app.route("/<action>/<value>")
def action(action, value):
    if action == 'pan':
        if value == 'left':
            pan.setangle(pan.getangle() - 5)
            return "Panning left 5 degrees"
        if value == 'right':
            pan.setangle(pan.getangle() + 5)
            return "Panning right 5 degrees"
    if action == 'tilt':
        if value == 'up':
            tilt.setangle(tilt.getangle() + 5)
            return "Tilting up 5 degrees"
        if value == 'down':
            tilt.setangle(tilt.getangle() - 5)
            return "Tilting down 5 degrees"
            
            
# Reset camera to neutral position
@app.route("/reset")
def reset():
    pan.reset()
    tilt.reset()
    return "Resetting position."
    
    
def main():
    try:
        # Start both servos
        pan.startup()
        tilt.startup()
        
        # Run the flask server to accept commands
        app.run(host='0.0.0.0', port=8764, debug=False)
        
        # Reset position for exiting
        reset()
        GPIO.cleanup()
            
    except KeyboardInterrupt:
        # Catch CTRL-C if run from terminal and exit gracefully
        reset()
        GPIO.cleanup()
        sys.exit(0)


if __name__ == "__main__":
    # Initialize the servo objects with travel limits
    tilt = servo(18, 60, 90, 115)
    pan = servo(16, 45, 90, 145)    
    main()
