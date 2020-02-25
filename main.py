import RPi.GPIO as maket_pins
import time
import multiprocessing as mp
import socket
import struct


def military_base(conrtol_pin):
    print('change red')
    print('open roof')
    print('start timer')
    print('switch music to game')
    maket_pins.output(conrtol_pin, 1)
    time.sleep(1)
    maket_pins.output(conrtol_pin, 0)
    time.sleep(1)



class Maket_CTF:
    def __init__(self):
        maket_pins.setmode(maket_pins.BOARD)
        self.relay_list = (18, 16, 22, 24, 26, 40, 38, 36)
        for pin in self.relay_list:
            maket_pins.setup(pin, maket_pins.OUT)
        print('start class')
        self.host_name = '10.50.16.5'
        self.port_name = 8080

    def init_building(self):
        for pin in self.relay_list:
            maket_pins.output(pin, 0)

    def test_code(self):
        for pin in self.relay_list:
            maket_pins.output(pin, 1)
            time.sleep(1)
        for pin in self.relay_list:
            maket_pins.output(pin, 0)
            time.sleep(1)

    def electrostation(self, control_pin):
        print('change red')
        print('switch off smoke')
        print('switch music to dingg')

    def goverment(self, conrtol_pin):
        print('change red')
        print('switch off light')
        print('play song')

    def weather_station(self, control_pin):
        print('change red')

    def rls_system(self, control_pin):
        print('change red')

    def home_build(self, control_pin):
        print('change red')

    def clean_all(self):
        maket_pins.cleanup()

    def read_socket(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.s:
            self.s.connect((self.host_name, self.port_name))
            while True:
                data = self.s.recv(1024)
                value = data.decode('utf-8')
                value = int(value)
                if value % 3 == 0:
                    military_base(self.relay_list[0])

                else:
                    print(value)


if __name__ == "__main__":
    maket = Maket_CTF()
    print('start work')
    maket.init_building()

    # proc = mp.Process(target=maket.read_socket, args=(message,))
    # proc.start()
    maket.read_socket()

    # maket.test_code()
    maket.clean_all()

# maket_pin.output(16, 1)
# maket_pin.output(18, 1)
# time.sleep(10)
# maket_pin.output(16, 0)
# maket_pin.output(18, 0)
# time.sleep(1)
