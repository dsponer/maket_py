import Adafruit_PCA9685
import time


def calculate_angle(value):
    return int(float(value) * 500.0 / 180.0) + 110


pwm = Adafruit_PCA9685.PCA9685(address=0x41)
servo_min = 150
servo_max = 600
pwm.set_pwm_freq(60)

while True:
    pwm.set_pwm(0, 0, calculate_angle(50))  # min 50 max 70
    pwm.set_pwm(1, 0, calculate_angle(75))  # min 80 max 50
    time.sleep(5)
    pwm.set_pwm(0, 0, calculate_angle(70))  # min 50 max 70
    pwm.set_pwm(1, 0, calculate_angle(50))  # min 80 max 50
    time.sleep(5)
