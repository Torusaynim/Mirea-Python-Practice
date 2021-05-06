import struct
import pprint

D_SIZE = 4 + 4 + 1
E_SIZE = 8 + 4 + 2 + 2 + 1
C_SIZE = 1 + 8 + 2 + 4 + 2 + 2
B_SIZE = 4 + 4 + E_SIZE + 2 + 8 + 4 + 8 + 8 + 4 + 4
A_SIZE = B_SIZE + 2


def parse_d(offset, byte_string):
    d_bytes = byte_string[offset:offset + D_SIZE]
    d_parsed = struct.unpack('>iIb', d_bytes)
    return {'D1': d_parsed[0], 'D2': d_parsed[1], 'D3': d_parsed[2]}


def parse_e(offset, byte_string):
    e_bytes = byte_string[offset:offset + E_SIZE]
    e_parsed = struct.unpack('>QIHHB', e_bytes)
    e3_bytes = byte_string[e_parsed[3]:e_parsed[3] + e_parsed[2]]
    e3_parsed = struct.unpack('>' + 'B' * e_parsed[2], e3_bytes)
    return {'E1': e_parsed[0],
            'E2': e_parsed[1],
            'E3': list(e3_parsed),
            'E4': e_parsed[4]}


def parse_c(offset, byte_string):
    c_bytes = byte_string[offset:offset + C_SIZE]
    c_parsed = struct.unpack('>bQHIHH', c_bytes)
    c5_bytes = byte_string[c_parsed[5]:c_parsed[5] + c_parsed[4] * 2]
    c5_parsed = struct.unpack('>' + 'H' * c_parsed[4], c5_bytes)
    return {'C1': c_parsed[0],
            'C2': c_parsed[1],
            'C3': c_parsed[2],
            'C4': parse_d(c_parsed[3], byte_string),
            'C5': list(c5_parsed)}


def parse_b(offset, byte_string):
    b1_bytes = byte_string[offset:offset + 8]
    b1_parsed = struct.unpack('>II', b1_bytes)
    b1_list = [parse_c(b1_parsed[1] + i * C_SIZE, byte_string) for i in range(b1_parsed[0])]
    b345678_bytes = byte_string[offset + 8 + E_SIZE:offset + 8 + E_SIZE + 2 + 8 + 4 + 8 + 8 + 4 + 4]
    b345678_parsed = struct.unpack('>hqidQII', b345678_bytes)
    b8_bytes = byte_string[b345678_parsed[6]:b345678_parsed[6] + b345678_parsed[5] * 8]
    b8_parsed = struct.unpack('>' + 'q' * b345678_parsed[5], b8_bytes)
    return {'B1': b1_list,
            'B2': parse_e(offset + 8, byte_string),
            'B3': b345678_parsed[0],
            'B4': b345678_parsed[1],
            'B5': b345678_parsed[2],
            'B6': b345678_parsed[3],
            'B7': b345678_parsed[4],
            'B8': list(b8_parsed)}


def parse_a(offset, byte_string):
    a2_bytes = byte_string[offset + B_SIZE:offset + B_SIZE + 2]
    a2_parsed = struct.unpack('>h', a2_bytes)
    return {'A1': parse_b(offset, byte_string),
            'A2': a2_parsed[0]}


def f31(byte_string):
    return parse_a(4, byte_string)


'''
pprint.pprint(f31((b'\x0cKGR\x00\x00\x00\x02\x00\x00\x00e\xa5vf\x87 0\x8as\x06HKO\x00\x03\x00\x8b'
b"\xa0'q\xf9\x93\xce+\x02\x1b\xc7\xf3q\xbc\xd1\xeb?\xb0D-^\xb4\xc3 b"
b'q\xef\xc0\x10\xf3\x9d+\x00\x00\x00\x03\x00\x00\x00\x8e\xdeN\xd1\xfe\xb2'
b'P\x9a2s\xbc[\x13\xc64\xe9\x94\xfd7\x80k\xc8\x9b\xf1`\x8d\xb9z\x02\xeb'
b'J\x93\x9a=\xd0\x80;fgC\xc8zH*8\x01\x00\x00\x00E\x00\x04\x00NB\xecW\xbb'
b'u\xf9\x95\xff\xa0=\xf5\x00\x00\x00V\x00\x03\x00_+:\x93>Ah,\xaf\xabq[\x0bn'
b'\xb3\xe1\xf3\x88\xcfD0\x01u\xd7S\xe8\x85(')))

pprint.pprint(f31((b'\x0cKGR\x00\x00\x00\x02\x00\x00\x00g\xe8\xfd\xddpDk\x96\xda~4q\x8a'
b'\x00\x05\x00\x8d7cA\xf3\xb2E\xd8M\xc8zv0k\x1b#?\xe6m\xbe/{\x8f\xee\xcb'
b'\x15\xc5\xb7l\x03t<\x00\x00\x00\x03\x00\x00\x00\x92|\x11\xd3u\xcd'
b'\xdf\xaf\xe0-\xac4W)\xc6\xbb\xd9\x1d\xb6\xf1\x9d\x01\xd2K\x83E'
b'\xe8\xf5\xa4\xf3B\xabMD7\xe2\xd4\xfe\xd9\x8e;~\xbc\xe1\x96\x80'
b'\x8f\xb9\x00\x00\x00E\x00\x06\x00Nl\xa8 \xfd\xcc\xbc\xf8\x06x\x90'
b'a\x00\x00\x00Z\x00\x02\x00cx\xed\xbc\xbe\xa4H\xf9\x1bB\xfb\x824\xe2\xaa\xe3'
b':\x06\n\xd6\x17\xb1z{\xfb^\xdd\rvh')))
'''


class C32:
    def __init__(self):
        self.condition = 'A'

    def amass(self):
        if self.condition == 'B':
            self.condition = 'B'
            return 3
        elif self.condition == 'C':
            self.condition = 'D'
            return 4
        elif self.condition == 'D':
            self.condition = 'E'
            return 5
        else:
            return None

    def check(self):
        if self.condition == 'A':
            self.condition = 'B'
            return 0
        elif self.condition == 'B':
            self.condition = 'C'
            return 1
        elif self.condition == 'F':
            self.condition = 'G'
            return 7
        elif self.condition == 'G':
            self.condition = 'G'
            return 9
        else:
            return None

    def daub(self):
        if self.condition == 'B':
            self.condition = 'F'
            return 2
        elif self.condition == 'E':
            self.condition = 'F'
            return 6
        elif self.condition == 'G':
            self.condition = 'C'
            return 8
        else:
            return None


'''
o = C32()
print(o.check())
print(o.amass())
print(o.check())
print(o.amass())
print(o.amass())
print(o.amass())
print(o.daub())
print(o.check())
print(o.daub())
print(o.amass())
print(o.daub())
print(o.amass())
print(o.daub())
print(o.check())
print(o.amass())
print(o.check())
'''