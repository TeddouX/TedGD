from TedGD.Properties import propertiesID
from TedGD.Triggers.color import HSV
import base64

def decode_property(prop: int, val: str):
    if prop == propertiesID.TEXT:
        return decode_text(val)
    elif prop == propertiesID.HSV:
        return HSV.from_robtop(val)
    return str(val)
    
def encode_property(prop: int, val):
    if prop == propertiesID.TEXT:
        return encode_text(val)
    elif prop == propertiesID.HSV:
        return val.to_robtop()
    return str(val)

def encode_text(text: str):
    return base64.b64encode(text.encode(), altchars=b"-_").decode()
def decode_text(text: str):
    return base64.b64decode(text.encode(), altchars=b"-_").decode()
