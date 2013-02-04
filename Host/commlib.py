import socket
import serial


# class ssock:
#     def __init__(self, sock=None):
#         if sock is None:
#             self.sock = socket.socket(
#                 socket.AF_INET, socket.SOCK_STREAM)
#         else:
#             self.sock = sock

#     def sconnect(self, host, port):
#         self.sock.connect((host, port))

#     def ssend(self, msg):
#         totalsent = 0
#         while totalsent < MSGLEN:
#             sent = self.sock.send(msg[totalsent:])
#             if sent == 0:
#                 raise RuntimeError("socket connection broken")
#             totalsent = totalsent + sent

#     def sreceive(self):
#         msg = ''
#         while len(msg) < MSGLEN:
#             chunk = self.sock.recv(MSGLEN-len(msg))
#             if chunk == '':
#                 raise RuntimeError("socket connection broken")
#             msg = msg + chunk
#         return msg

def sockwrite(msg):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 9999))
    s.send(msg)
    s.close()

def serialwrite(msg):
	s = serial.Serial('/dev/ttyACM0', 9600, timeout=5)
	s.write(msg)
	s.flushOutput()
	s.close()
