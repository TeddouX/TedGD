from collections import UserDict

class GDObject(UserDict):
    def __init__(self, properties: dict[int, int] = {}) -> None:
        super().__init__({1:1, 2:0, 3:0, 155:1})
        
        for k, v in properties.items():
            self.__setitem__(k, v)

    @classmethod
    def from_robtop(self, data: str):
        obj = {}
        properties = data.split(',')
        encoded_pairs = [(int(properties[i]), int(properties[i+1])) for i in range(0, len(properties), 2)]

        for k, v in encoded_pairs:
            obj[k] = v

        return GDObject(obj)  
    
    def to_robtop(self) -> str:
        rob_str = ""
        all_keys_list = list(self.keys())
        for k, v in self.items():
            if all_keys_list.index(k) == len(all_keys_list) - 1: 
                rob_str += str(k) + "," + str(v)
            else:
                rob_str += str(k) + "," + str(v) + ","
        
        return rob_str
    