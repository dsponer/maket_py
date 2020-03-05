import RPi.GPIO as maket_pins
import time
import socket
import pygame
import Adafruit_PCA9685


# (18 - relay 1,
# 16 - relay 2,
# 22 - relay 3,
# 24 - relay 4,
# 26 - relay 5,
# 40 - relay 6,
# 38 - relay 7,
# 36 - relay 8)


class Maket_CTF:
    def __init__(self):
        maket_pins.setmode(maket_pins.BOARD)
        self.relay_list = (18, 16, 22, 24, 26, 40, 38, 36)
        for pin in self.relay_list:
            maket_pins.setup(pin, maket_pins.OUT)
        print('start class')
        self.host_name = '10.50.16.71'
        self.port_name = 12345
        self.list_of_building = ['military', 'electrostation', 'goverment', 'weather', 'rls', 'home']
        self.pwm = Adafruit_PCA9685.PCA9685(address=0x41)
        self.servo_min = 150
        self.servo_max = 600
        self.pwm.set_pwm_freq(50)

    def init_building(self):
        for pin in self.relay_list:
            maket_pins.output(pin, 0)

        self.pwm.set_pwm(0, 0, self.servo_min)
        self.pwm.set_pwm(1, 0, self.servo_min)
        time.sleep(1)

    def test_code(self):
        for pin in self.relay_list:
            maket_pins.output(pin, 1)
            time.sleep(1)
        for pin in self.relay_list:
            maket_pins.output(pin, 0)
            time.sleep(1)

    def military_base(self, control_pin):
        print('change red')
        print('open roof')
        print('start timer')
        print('switch music to game')
        file = 'asking-alexandria-alone-in-a-room_456510653.mp3'
        maket_pins.output(control_pin, 1)
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()

    def electrostation(self, led_pin, smoke_pin):
        print('change red')
        print('switch off smoke')
        print('switch music to dingg')
        maket_pins.output(led_pin, 1)
        maket_pins.output(smoke_pin, 1)

    def goverment(self, control_pin):
        print('change red')
        print('switch off light')
        print('play song')
        maket_pins.output(control_pin, 1)

    def weather_station(self, control_pin):
        print('change red')
        maket_pins.output(control_pin, 1)

    def rls_system(self, control_pin):
        print('change red')
        maket_pins.output(control_pin, 1)

    def home_build(self, control_pin):
        print('change red')
        maket_pins.output(control_pin, 1)

    def clean_all(self):
        maket_pins.cleanup()

    def read_socket(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.s:
            self.s.connect((self.host_name, self.port_name))
            while True:
                data = self.s.recv(1024)
                value = data.decode('utf-8')
                if value in self.list_of_building:
                    if value == self.list_of_building[0]:
                        self.military_base(self.relay_list[0])
                    if value == self.list_of_building[1]:
                        self.electrostation(self.relay_list[1], self.relay_list[7])
                    if value == self.list_of_building[2]:
                        self.goverment(self.relay_list[2])
                    if value == self.list_of_building[3]:
                        self.goverment(self.relay_list[3])
                    if value == self.list_of_building[4]:
                        self.goverment(self.relay_list[4])
                    if value == self.list_of_building[5]:
                        self.goverment(self.relay_list[5])
                else:
                    self.init_building()
                    print('wait')
                # if value % 3 == 0:
                #     self.military_base(self.relay_list[0])
                # else:
                #     print(value)


if __name__ == "__main__":
    try:
        maket = Maket_CTF()
        print('start work')
        maket.init_building()

        # proc = mp.Process(target=maket.read_socket, args=(message,))
        # proc.start()
        maket.read_socket()

        # maket.test_code()
    except KeyboardInterrupt:
        for pin in (18, 16, 22, 24, 26, 40, 38, 36):
            maket_pins.output(pin, 0)

        maket.clean_all()
