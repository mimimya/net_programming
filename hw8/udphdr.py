#import socket
import struct
import binascii

class Udphdr:

    def __init__(self, s_port, d_port, p_len, chek):
        self.s_port = s_port
        self.d_port = d_port
        self.p_len = p_len
        self.check = chek

    def pack_Udphdr(self):
        packed = b''
        packed += struct.pack('!4H', self.s_port, self.d_port, self.p_len, self.check)
        return packed


def unpack_Udphdr(buffer):
    unpacked = struct.unpack('!4H', buffer[:8])
    return unpacked
def getSourcePort(unpacked_udphdr):
    return unpacked_udphdr[0]
def getDestinationPort(unpacked_udphdr):
    return unpacked_udphdr[1]
def getLength(unpacked_udphdr):
    return unpacked_udphdr[2]
def getChecksum(unpacked_udphdr):
    return unpacked_udphdr[3]



ip = Udphdr(5555, 80, 1000, 0xFFFF)
packed_udphdr = ip.pack_Udphdr()
print(binascii.b2a_hex(packed_udphdr))

unpacked_udphdr = unpack_Udphdr(packed_udphdr)
print(unpacked_udphdr)
print('Source Port:{} Destination Port:{} Length:{} Checksum:{}' \
    .format(getSourcePort(unpacked_udphdr), getDestinationPort(unpacked_udphdr), getLength(unpacked_udphdr), getChecksum(unpacked_udphdr)))