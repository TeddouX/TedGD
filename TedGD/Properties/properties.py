from TedGD.Properties.IDs import p
import base64

def decode_property(prop: int, val: str):
    if prop == p["text"]:
        return decode_text(val)
    
def decode_text(text: str):
    return base64.b64decode(text, altchars=b"-_")
