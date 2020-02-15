from socket import *
import selectors
from datetime import datetime
# import cv2

addr = ('10.50.16.5', 8000)
selector = selectors.DefaultSelector()
connections = []
jpeg_quality = 60


# class VideoGrabber:
#     def __init__(self):
#         self.encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), jpeg_quality]
#         self.cap = cv2.VideoCapture(0)
#         self.cap.set(cv2.CAP_PROP_FPS, 60)
#         self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
#         self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
#         self.buffer = None
#
#     def get_bimage(self):
#         success, img = self.cap.read()
#         result, buffer = cv2.imencode('.jpg', img, self.encode_param)
#         return buffer


# grab = VideoGrabber()


def server():
    server_socket = socket(AF_INET, SOCK_DGRAM)
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server_socket.bind(addr)

    selector.register(server_socket, selectors.EVENT_READ, data)


def data(client_socket):
    request, addr = client_socket.recvfrom(4096)
    request = bytes.decode(request)

    if request:
        # if request == 'get':
        #     # buffer = grab.get_bimage()
        #     if buffer is None:
        #         return
        #     if len(buffer) > 65507:
        #         print(
        #             "The message is too large to be sent within a single UDP datagram. We do not handle splitting the message in multiple datagrams")
        #         client_socket.sendto("FAIL", addr)
        #         return
        #     # We sent back the buffer to the client
        #     client_socket.sendto(buffer.tobytes(), addr)
        # else:
        #     print(request.split(','))
        print(request)
    else:
        selector.unregister(client_socket)
        client_socket.close()


def event_loop():
    while True:
        events = selector.select()  # (key,events)

        for key, _ in events:
            callback = key.data
            callback(key.fileobj)


if __name__ == '__main__':
    server()
    event_loop()
