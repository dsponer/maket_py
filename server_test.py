import socket
import time

from PyQt5.QtCore import pyqtSlot, QTimer
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.uic import loadUi


class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        loadUi('dialog.ui', self)

        self.host_name = '10.50.16.71'
        self.port_name = 4321
        self.list_of_building = ['military', 'electrostation', 'goverment', 'weather', 'rls', 'home']

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host_name, self.port_name))
            s.listen()
            self.conn, self.addr = s.accept()

            # count = 0
            # while True:
            #     conn.sendall(str(count).encode())
            #     print(count)
            #     time.sleep(1)
            #     count += 1

    @pyqtSlot()
    def on_button_1_clicked(self):
        print('send', self.list_of_building[1])
        self.conn.sendall(self.list_of_building[1].encode())

    @pyqtSlot()
    def on_button_2_clicked(self):
        print('send', self.list_of_building[0])
        self.conn.sendall(self.list_of_building[0].encode())

    @pyqtSlot()
    def on_button_3_clicked(self):
        print('send', self.list_of_building[2])
        self.conn.sendall(self.list_of_building[2].encode())

    @pyqtSlot()
    def on_button_4_clicked(self):
        print('send', self.list_of_building[3])
        self.conn.sendall(self.list_of_building[3].encode())

    @pyqtSlot()
    def on_button_5_clicked(self):
        print('send', self.list_of_building[4])
        self.conn.sendall(self.list_of_building[4].encode())

    @pyqtSlot()
    def on_button_6_clicked(self):
        print('send', self.list_of_building[5])
        self.conn.sendall(self.list_of_building[5].encode())

    @pyqtSlot()
    def off_button_clicked(self):
        print('send off all')
        self.conn.sendall('send off all'.encode())


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
