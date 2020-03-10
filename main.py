import RPi.GPIO as maket_pins
import time
import socket
import pygame
import Adafruit_PCA9685

from multiprocessing import Process


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
        self.relay_list = (22, 18, 16, 40, 26, 24, 38, 36)
        for pin in self.relay_list:
            maket_pins.setup(pin, maket_pins.OUT)
        print('start class')
        self.host_name = '10.193.53.204'
        # self.host_name = '10.193.48.189'
        self.port_name = 4321
        self.list_of_building = ['military', 'electrostation', 'goverment', 'weather', 'rls', 'bank']
        self.pwm = Adafruit_PCA9685.PCA9685(address=0x41)
        self.servo_min_0 = 50
        self.servo_min_1 = 75
        self.servo_max_0 = 70
        self.servo_max_1 = 50
        self.pwm.set_pwm_freq(60)
        pygame.init()
        pygame.mixer.init()

    def init_building(self):
        for pin in self.relay_list:
            maket_pins.output(pin, 0)

        self.pwm.set_pwm(0, 0, self.calculate_angle(self.servo_min_0))
        self.pwm.set_pwm(1, 0, self.calculate_angle(self.servo_min_1))

    def calculate_angle(self, value):
        return int(float(value) * 500.0 / 180.0) + 110

    def play_music(self, file):
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()

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
        maket_pins.output(38, 1)
        self.pwm.set_pwm(0, 0, self.calculate_angle(self.servo_max_0))  # min 50 max 70
        self.pwm.set_pwm(1, 0, self.calculate_angle(self.servo_max_1))  # min 80 max 50
        file = 'rls.mp3'
        maket_pins.output(control_pin, 1)
        self.play_music(file)
        time.sleep(12)
        self.pwm.set_pwm(0, 0, self.calculate_angle(self.servo_min_0))  # min 50 max 70
        self.pwm.set_pwm(1, 0, self.calculate_angle(self.servo_min_1))  # min 80 max 50
        maket_pins.output(control_pin, 0)
        pygame.mixer.music.stop()

    def electrostation(self, led_pin, smoke_pin):
        print('change red')
        print('switch off smoke')
        print('switch music to dingg')
        file = 'electrostation.mp3'
        self.play_music(file)
        maket_pins.output(led_pin, 1)
        maket_pins.output(smoke_pin, 1)
        time.sleep(10)
        maket_pins.output(led_pin, 0)
        maket_pins.output(smoke_pin, 0)

    def goverment(self, control_pin):
        print('change red')
        print('switch off light')
        print('play song')
        file = 'goverment.mp3'
        self.play_music(file)
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        maket_pins.output(control_pin, 1)
        time.sleep(10)
        maket_pins.output(control_pin, 0)

    def weather_station(self, control_pin):
        print('change red')
        file = 'weather.mp3'
        self.play_music(file)
        maket_pins.output(control_pin, 1)
        time.sleep(10)
        maket_pins.output(control_pin, 0)

    def rls_system(self, control_pin):
        print('change red')
        file = 'rls.mp3'
        self.play_music(file)
        maket_pins.output(control_pin, 1)
        time.sleep(10)
        maket_pins.output(control_pin, 0)

    def home_build(self, control_pin):
        print('change red')
        file = 'bank.mp3'
        self.play_music(file)
        maket_pins.output(control_pin, 1)
        time.sleep(10)
        maket_pins.output(control_pin, 0)

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
                        p1 = Process(target=self.military_base, args=(self.relay_list[0],))
                        p1.start()
                        # self.military_base(self.relay_list[0])
                    if value == self.list_of_building[1]:
                        p2 = Process(target=self.electrostation, args=(self.relay_list[1], self.relay_list[7],))
                        p2.start()
                        # self.electrostation(self.relay_list[1], self.relay_list[7])
                    if value == self.list_of_building[2]:
                        p3 = Process(target=self.goverment, args=(self.relay_list[2],))
                        p3.start()
                        # self.goverment(self.relay_list[2])
                    if value == self.list_of_building[3]:
                        p4 = Process(target=self.weather_station, args=(self.relay_list[3],))
                        p4.start()
                        # self.goverment(self.relay_list[3])
                    if value == self.list_of_building[4]:
                        p5 = Process(target=self.rls_system, args=(self.relay_list[4],))
                        p5.start()
                        # self.goverment(self.relay_list[4])
                    if value == self.list_of_building[5]:
                        p6 = Process(target=self.home_build, args=(self.relay_list[5],))
                        p6.start()
                        # self.goverment(self.relay_list[5])
                else:
                    p7 = Process(target=self.off_all(), args=())
                    p7.start()
                    # self.off_all()
                    print('wait')
                # if value % 3 == 0:
                #     self.military_base(self.relay_list[0])
                # else:
                #     print(value)

    def off_all(self):
        for pin in self.relay_list:
            maket_pins.output(pin, 0)


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
