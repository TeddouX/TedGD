import zlib
import base64
import os
import xml.etree.ElementTree as ET
from xml.dom import minidom


SAVE_FILE = "CCLocalLevels.dat"
SAVE_PATH = os.getenv("localappdata") + "\\GeometryDash\\" + SAVE_FILE

BACKUP_DIR = "\\Level Backups\\"
BACKUP_PATH = os.getcwd() + BACKUP_DIR

def load_save() -> bytes:
    with open(SAVE_PATH, "rb") as r:
        data = r.read()
        return data
    
def xor(data: bytes, key: int) -> str:
    final = []
    for byte in data:
        final.append(byte ^ key)

    return bytearray(final).decode()

def decrypt_save(data: bytes):
    xored = xor(data, 11)
    decrypted = base64.b64decode(xored, altchars=b"-_")
    final = zlib.decompress(decrypted[10:], -zlib.MAX_WBITS)

    return final

def read_save_xml(gamesave: bytes) -> ET.ElementTree:
    tree = ET.ElementTree(ET.fromstring(gamesave))

    return tree.getroot()


def get_levels_strings(root: ET.ElementTree) -> dict[str, bytes]:
    levels_node = root[0][1]
    levels = {}
    for child in levels_node:
        if child.tag == "d":
            for j, child_ in enumerate(child):
                if child_.text == 'k2':
                    level_name = child[j+1].text
                elif child_.text == 'k4':
                    level_string = child[j+1].text
                    decoded = base64.urlsafe_b64decode(level_string)
                    decompressed = zlib.decompress(decoded, 15 | 32).decode()
            
            levels[level_name] = {
                "head": decompressed.split(";")[0],
                "objects": decompressed.split(";")[1:]
            }

    return levels


def overwrite_level(level_name: str, level_string: str) -> None:
    current_save_str = load_save()
    decrypted = decrypt_save(current_save_str)
    current_save_xml = read_save_xml(decrypted)

    levels_node = current_save_xml[0][1]
    for child in levels_node:
        if child.tag == "d":
            for i, _child in enumerate(child):
                if _child.text == "k2":
                    _level_name = child[i+1].text
                    if _level_name == level_name:
                        # Change the level string in the XML
                        level_string_idx = [i for i in child.itertext()].index("k4") + 1
                        print(child[level_string_idx].text)
                        child[level_string_idx].text = level_string
                        break

    

def save_backup(level_name: str, data: str):
    os.makedirs(BACKUP_PATH, exist_ok=True)

    try:
        with open(BACKUP_PATH + level_name, "x") as f:
            f.write(data)
    except FileExistsError:
        with open(BACKUP_PATH + level_name, "w") as f:
            f.write(data)

def load_backup(level_name: str) -> str:
    try:
        with open(BACKUP_PATH + level_name) as f:
            contents = f.read()
            return contents
    except FileNotFoundError:
        raise Exception(f"No backup with name {level_name}")    
    