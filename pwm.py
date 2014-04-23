import Adafruit_BBIO.PWM as PWM
 
servo_pin = "P9_14"
duty_min = 2.5
duty_max = 13.1
duty_span = duty_max - duty_min
 
PWM.start(servo_pin, duty_span * 0.5, 60.0)
 
while True:
    angle = raw_input("Angle (0 to 180 x to exit):")
    if angle == 'x':
        PWM.stop(servo_pin)
        PWM.cleanup()
        break
    duty = float(angle)
    print "Setting duty to %.2f%%" % duty
    PWM.set_duty_cycle(servo_pin, duty)
