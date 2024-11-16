from TedGD import propertiesID
from TedGD.color import HSV
import base64
import itertools

def decode_property(prop: int, val: str):
    if prop == propertiesID.TEXT:
        return decode_text(val)
    elif prop == propertiesID.HSV:
        return HSV.from_robtop(val)
    elif prop == propertiesID.GROUP_PROBABILITIES:
        splitted = val.split(".")
        it = iter(splitted)
        return zip(it, it)
            
    return val
    
def encode_property(prop: int, val):
    if prop == propertiesID.TEXT:
        return encode_text(val)
    elif prop == propertiesID.HSV:
        return val.to_robtop()
    elif prop == propertiesID.GROUP_PROBABILITIES:
        without_tuples = itertools.chain(*val)
        without_tuples = [str(i) for i in without_tuples]
        return ".".join(without_tuples)
    
    return str(val)

def encode_text(text: str):
    return base64.b64encode(text.encode(), altchars=b"-_").decode()
def decode_text(text: str):
    return base64.b64decode(text.encode(), altchars=b"-_").decode()
