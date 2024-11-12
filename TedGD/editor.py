from TedGD import loadsave
from TedGD.gdobject import GDObject

DEFAULT_LEVEL_HEAD = "kS38,1_40_2_125_3_255_11_255_12_255_13_255_4_-1_6_1000_7_1_15_1_18_0_8_1|1_0_2_102_3_255_11_255_12_255_13_255_4_-1_6_1001_7_1_15_1_18_0_8_1|1_0_2_102_3_255_11_255_12_255_13_255_4_-1_6_1009_7_1_15_1_18_0_8_1|1_255_2_255_3_255_11_255_12_255_13_255_4_-1_6_1002_5_1_7_1_15_1_18_0_8_1|1_40_2_125_3_255_11_255_12_255_13_255_4_-1_6_1013_7_1_15_1_18_0_8_1|1_40_2_125_3_255_11_255_12_255_13_255_4_-1_6_1014_7_1_15_1_18_0_8_1|1_125_2_255_3_0_11_255_12_255_13_255_4_-1_6_1005_5_1_7_1_15_1_18_0_8_1|1_0_2_255_3_255_11_255_12_255_13_255_4_-1_6_1006_5_1_7_1_15_1_18_0_8_1|,kA13,0,kA15,0,kA16,0,kA14,,kA6,0,kA7,0,kA25,0,kA17,0,kA18,0,kS39,0,kA2,0,kA3,0,kA8,0,kA4,0,kA9,0,kA10,0,kA22,0,kA23,0,kA24,0,kA27,1,kA40,1,kA41,1,kA42,1,kA28,0,kA29,0,kA31,1,kA32,1,kA36,0,kA43,0,kA44,0,kA45,1,kA33,1,kA34,1,kA35,0,kA37,1,kA38,1,kA39,1,kA19,0,kA26,0,kA20,0,kA21,0,kA11,0"

class Editor:
    def __init__(self, level_name: str, level_head: str, objects: list[str]) -> None:
        self.level_name = level_name
        self.level_head = level_head
        self.objects: list[GDObject] = objects

    @classmethod
    def load_empty(self, level_name: str):
        return Editor(level_name, DEFAULT_LEVEL_HEAD, [])

    @classmethod
    def load_level(self, level_name: str):
        save = loadsave.load_save()
        decrypted = loadsave.decrypt_save(save)
        save_xml = loadsave.read_save_xml(decrypted)
        all_level_strings = loadsave.get_levels_strings(save_xml)

        level_head = None
        object_strings = None
        for key, item in all_level_strings.items():
            if key == level_name:
                level_head = item["head"]
                object_strings = item["objects"] 

        if level_head == None:
            raise Exception("The level can't be found. Check the level's name spelling.")
        
        objects = [GDObject.from_robtop(i) for i in object_strings]

        return Editor(level_name, level_head, objects)

    @classmethod
    def load_backup(self, level_name: str):
        contents = loadsave.load_backup(level_name)
        saved = contents.split("$")
        objects_strings = saved[1].split(";")

        objects = [GDObject.from_robtop(i) for i in objects_strings]

        return Editor(level_name, saved[0], objects)
    
    def to_backup(self) -> str:
        robtop_objects = [i.to_robtop() for i in self.objects]
        robtop_str = self.level_head + "$" + ';'.join(robtop_objects)

        return robtop_str
    
    def to_robtop(self) -> str:
        return self.to_backup().replace("$", ";")
    
    def overwrite_gd_level(self) -> None:
        robtop_str = self.to_robtop()
        loadsave.overwrite_level(self.level_name, robtop_str)

    def backup(self) -> None:
        loadsave.save_backup(self.level_name, self.to_backup())

    def add_object(self, object: GDObject) -> None:
        if type(object) != GDObject: raise Exception("Cannot add an object that isn't of type \"GDObject\"")

        self.objects.append(object)

    def remove_all_objects(self) -> None:
        self.objects = []
