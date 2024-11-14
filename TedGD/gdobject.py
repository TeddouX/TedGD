from collections import UserDict
from TedGD.Properties import properties, propertiesID

DEFAULT_BLOCK = 1
COLORABLE_BLOCK = 211
OUTLINE_BLOCK = 467
TEXT = 914
SMALL_CIRCLE = 3802

class GDObject(UserDict):
    def __init__(self, properties_: dict[int,] = {}) -> None:
        # Default object
        super().__init__({1: DEFAULT_BLOCK, 2: "0", 3: "0", 155: "1"})
        
        # Create the dict
        for k, v in properties_.items():
            self.__setitem__(k, v)

    @classmethod
    def from_robtop(self, data: str):
        obj = {}
        properties_ = data.split(',')
        encoded_pairs = [(int(properties_[i]), properties_[i+1]) for i in range(0, len(properties_), 2)]

        for k, v in encoded_pairs:
            obj[k] = properties.decode_property(k, v)

        return GDObject(obj)  

    def set_property(self, prop: int, val) -> None:
        self[prop] = val

    def get_property(self, prop: int):
        return self[prop]
    
    def add_groups(self, groups: list[int]) -> None:
        groups = [str(i) for i in groups]

        try:
            self[propertiesID.GROUPS] += "." + ".".join(groups)
        except KeyError:
            self[propertiesID.GROUPS] = ".".join(groups)

    def add_group(self, group_num: int) -> None:
        try:
            self[propertiesID.GROUPS] += "." + str(group_num) 
        except KeyError:
            self[propertiesID.GROUPS] = str(group_num)

    def get_groups(self) -> list[int]:
        return [int(i) for i in self[propertiesID.GROUPS].split(".")]

    def to_robtop(self) -> str:
        rob_str = ""
        all_keys_list = list(self.keys())
        for k, v in self.items():
            if all_keys_list.index(k) == len(all_keys_list) - 1: 
                rob_str += str(k) + "," + properties.encode_property(k, v)
            else:
                rob_str += str(k) + "," + properties.encode_property(k, v) + ","
        
        return rob_str
    