from collections import UserDict
from TedGD.Properties.IDs import p

class GDObject(UserDict):
    def __init__(self, properties: dict[int, int|str] = {}) -> None:
        # Default object
        super().__init__({1:"1", 2:"0", 3:"0", 155:"1"})
        
        # Create the dict
        for k, v in properties.items():
            self.__setitem__(k, str(v))

    @classmethod
    def from_robtop(self, data: str):
        obj = {}
        properties = data.split(',')
        encoded_pairs = [(int(properties[i]), properties[i+1]) for i in range(0, len(properties), 2)]


        for k, v in encoded_pairs:
            obj[k] = v

        return GDObject(obj)  

    def set_property(self, prop: int, val: str|int) -> None:
        self[prop] = val
    
    def add_groups(self, groups: list[int]) -> None:
        groups = [str(i) for i in groups]

        try:
            self[p["groups"]] += "." + ".".join(groups)
        except KeyError:
            self[p["groups"]] = ".".join(groups)

    def add_group(self, group_num: int) -> None:
        try:
            self[p["groups"]] += "." + str(group_num) 
        except KeyError:
            self[p["groups"]] = str(group_num)

    def to_robtop(self) -> str:
        rob_str = ""
        all_keys_list = list(self.keys())
        for k, v in self.items():
            if all_keys_list.index(k) == len(all_keys_list) - 1: 
                rob_str += str(k) + "," + v
            else:
                rob_str += str(k) + "," + v + ","
        
        return rob_str
    