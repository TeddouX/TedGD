from itertools import count, filterfalse
from TedGD.gdobject import GDObject
from TedGD.editor import Editor, align_to_grid
from TedGD.Properties import propertiesID
from TedGD.Triggers.color import RGB

EASE_IN_OUT = 1
EASE_IN = 2
EASE_OUT = 3
ELASTIC_IN_OUT = 4
ELASTIC_IN = 5
ELASTIC_OUT = 6
BOUNCE_IN_OUT = 7
BOUNCE_IN = 8
BOUNCE_OUT = 9
EXPONENTIAL_IN_OUT = 10
EXPONENTIAL_IN = 11
EXPONENTIAL_OUT = 12
SINE_IN_OUT = 13
SINE_IN = 14
SINE_OUT = 15
BACK_IN_OUT = 16
BACK_IN = 17
BACK_OUT = 18

STOP_TRIGGER_STOP = 0
STOP_TRIGGER_PAUSE = 1
STOP_TRIGGER_RESUME = 2

ID: dict[str, int] = {
    "move": 901,
    "color": 899,
    "toggle": 1049,
    "spawn": 1268,
    "stop": 1616
}

def get_smallest_not_in_list(l: list[int]):
    return next(filterfalse(set(l).__contains__, count(1)))

def move_trigger(pos_x: int = -15, pos_y: int = 15, 
                 move_x: int = 0, move_y: int = 0, 
                 easing: int = 0, easing_rate: float = 2.00,
                 duration: float = 0.00,
                 target_group: int = 0,
                 lock_to_player_x: bool = False, lock_to_player_y: bool = False,
                 x_mod: float = 1, y_mod: float = 1,
                 spawn_triggered: bool = False) -> GDObject:
    
    return GDObject({ propertiesID.ID: ID["move"], 
                      propertiesID.X: pos_x, propertiesID.Y: pos_y, 
                      propertiesID.MOVE_X: move_x * 3, propertiesID.MOVE_Y: move_y * 3,
                      propertiesID.EASING: easing, propertiesID.EASING_RATE: round(easing_rate, 2),
                      propertiesID.DURATION: round(duration, 2),
                      propertiesID.TARGET: target_group,
                      propertiesID.LOCK_TO_PLAYER_X: int(lock_to_player_x), propertiesID.LOCK_TO_PLAYER_Y: int(lock_to_player_y),
                      propertiesID.X_MOD: round(x_mod, 3), propertiesID.Y_MOD: round(y_mod, 3),
                      propertiesID.SPAWN_TRIGGERED: int(spawn_triggered), propertiesID.MULTI_TRIGGER: int(spawn_triggered) })

def color_trigger(pos_x: int = -15, pos_y: int = 15, 
                  color: RGB = RGB(0, 0, 0), 
                  fade_duration: float = 0.5,
                  opacity: float = 1.0,
                  target_color_channel: int = 1,
                  blending: bool = False,
                  spawn_triggered: bool = False) -> GDObject:
    
    return GDObject({ propertiesID.ID: ID["color"],
                      propertiesID.X: pos_x, propertiesID.Y: pos_y,
                      propertiesID.TRIGGER_RED: color.r, propertiesID.TRIGGER_GREEN: color.g, propertiesID.TRIGGER_BLUE: color.b,
                      propertiesID.DURATION: round(fade_duration, 2), 
                      propertiesID.OPACITY: round(opacity, 2),
                      propertiesID.TARGET_COLOR: target_color_channel,
                      propertiesID.BLENDING: int(blending),
                      propertiesID.SPAWN_TRIGGERED: int(spawn_triggered), propertiesID.MULTI_TRIGGER: int(spawn_triggered) })

def spawn_trigger(pos_x: int = -15, pos_y: int = 15,
                  target_group: int = 0,
                  spawn_duration: float = 0, spawn_duration_variance: float = 0, 
                  spawn_ordered: bool = False,
                  spawn_triggered: bool = False) -> GDObject:
    
    return GDObject({ propertiesID.ID: ID["spawn"],
                      propertiesID.X: pos_x, propertiesID.Y: pos_y,
                      propertiesID.TARGET: target_group,
                      propertiesID.SPAWN_DURATION: round(spawn_duration, 4), propertiesID.VARIANCE: round(spawn_duration_variance, 4),
                      propertiesID.SPAWN_ORDERED: int(spawn_ordered),
                      propertiesID.SPAWN_TRIGGERED: int(spawn_triggered), propertiesID.MULTI_TRIGGER: int(spawn_triggered) })

def toggle_trigger(pos_x: int = -15, pos_y: int = 15,
                   target_group: int = 0,
                   activate_group: bool = False,
                   spawn_triggered: bool = False) -> GDObject:
    
    return GDObject({ propertiesID.ID: ID["toggle"],
                      propertiesID.X: pos_x, propertiesID.Y: pos_y,
                      propertiesID.TARGET: target_group,
                      propertiesID.ACTIVATE_GROUP: int(activate_group),
                      propertiesID.SPAWN_TRIGGERED: int(spawn_triggered) })

def stop_trigger(pos_x: int = -15, pos_y: int = 15,
                 target_group: int = 0,
                 stop_trigger_type: int = 0,
                 spawn_triggered: bool = False) -> GDObject:

    return GDObject({ propertiesID.ID: ID["stop"],
                      propertiesID.X: pos_x, propertiesID.Y: pos_y,
                      propertiesID.TARGET: target_group,
                      propertiesID.STOP_TRIGGER_TYPE: stop_trigger_type,
                      propertiesID.SPAWN_TRIGGERED: bool(spawn_triggered) })

def create_spawn_loop(editor: Editor, target_group: int, 
                      pos_x: int = -15, pos_y: int = 15,
                      spawn_duration: float = 0,
                      spawn_ordered: bool = False, spawn_triggered: bool = False,
                      spawn_group: int = 0 ) -> None:
    
    used_groups = editor.get_all_groups()
    objects = editor.get_objects_with_group(target_group)
    
    if len(objects) == 0:
        raise Exception("There are no objects with group " + str(target_group))

    ref_obj = objects[-1]

    for i in objects: 
        i.set_property(propertiesID.SPAWN_TRIGGERED, 1)
        i.set_property(propertiesID.MULTI_TRIGGER, 1)

    used_groups = editor.get_all_groups()
    
    first_trigger_group = get_smallest_not_in_list(used_groups)

    first_trigger = spawn_trigger(pos_x, pos_y, target_group, True, 0, 0, spawn_ordered)
    first_trigger.add_group(first_trigger_group)
    second_trigger = spawn_trigger(ref_obj.get_property(propertiesID.X), ref_obj.get_property(propertiesID.Y) + align_to_grid(3)-15, first_trigger_group, True, spawn_duration)   
    second_trigger.add_group(target_group)   
    third_trigger = spawn_trigger(pos_x, pos_y + align_to_grid(2)-15, first_trigger_group, spawn_triggered, 0, 0, False)
    third_trigger.add_group(spawn_group)      
    
    editor.add_objects(first_trigger, second_trigger, third_trigger)       
    