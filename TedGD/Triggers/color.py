from typing import NamedTuple

CHANNEL_BG = 1000
CHANNEL_G1 = 1001
CHANNEL_G2 = 1009
CHANNEL_LINE = 1001
CHANNEL_OBJ = 1004
CHANNEL_3DL = 1003
CHANNEL_MG = 1013
CHANNEL_MG2 = 1014

class RGB(NamedTuple):
    r: int
    g: int
    b: int

class HSV():
    def __init__(self, h: int, s: float, v: float):
        self.h = h
        self.s = s
        self.v = v

    @classmethod
    def from_robtop(self, robtop_string: str):
        values = robtop_string.split("a")
        
        h = int(values[0])
        s = float(values[1])
        v = float(values[2])

        return HSV(h, s, v)

    def to_robtop(self) -> str:
        robtop_string = str(self.h) + "a" + str(self.s) + "a" + str(self.v) + "a0a0a"
        return robtop_string
