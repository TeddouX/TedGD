from typing import NamedTuple
from TedGD import propertiesID
from TedGD.gdobject import GDObject
from TedGD.editor import Editor, align_to_grid
from TedGD.color import RGB

class Easings(NamedTuple):
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

class StopTriggerTypes(NamedTuple):
    STOP = 0
    PAUSE = 1
    RESUME = 2

class TriggersID(NamedTuple):
    MOVE = 901
    COLOR = 899
    TOGGLE = 1049
    SPAWN = 1268
    ROTATE = 1346
    STOP = 1616
    RANDOM = 1912
    SCALE = 2067
    ADV_RANDOM = 2068

def move_trigger(pos_x: int = -15, pos_y: int = 15, 
                 move_x: int = 0, move_y: int = 0, 
                 easing: int = 0, easing_rate: float = 2.00,
                 duration: float = 0.00,
                 target_group: int = 0,
                 lock_to_player_x: bool = False, lock_to_player_y: bool = False,
                 x_mod: float = 1, y_mod: float = 1,
                 spawn_triggered: bool = False) -> GDObject:
    
    return GDObject({ propertiesID.ID: TriggersID.MOVE, 
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
    
    return GDObject({ propertiesID.ID: TriggersID.COLOR,
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
    
    return GDObject({ propertiesID.ID: TriggersID.SPAWN,
                      propertiesID.X: pos_x, propertiesID.Y: pos_y,
                      propertiesID.TARGET: target_group,
                      propertiesID.SPAWN_DURATION: round(spawn_duration, 4), propertiesID.VARIANCE: round(spawn_duration_variance, 4),
                      propertiesID.SPAWN_ORDERED: int(spawn_ordered),
                      propertiesID.SPAWN_TRIGGERED: int(spawn_triggered), propertiesID.MULTI_TRIGGER: int(spawn_triggered) })

def toggle_trigger(pos_x: int = -15, pos_y: int = 15,
                   target_group: int = 0,
                   activate_group: bool = False,
                   spawn_triggered: bool = False) -> GDObject:
    
    return GDObject({ propertiesID.ID: TriggersID.TOGGLE,
                      propertiesID.X: pos_x, propertiesID.Y: pos_y,
                      propertiesID.TARGET: target_group,
                      propertiesID.ACTIVATE_GROUP: int(activate_group),
                      propertiesID.SPAWN_TRIGGERED: int(spawn_triggered), propertiesID.MULTI_TRIGGER: int(spawn_triggered) })

def stop_trigger(pos_x: int = -15, pos_y: int = 15,
                 target_group: int = 0,
                 stop_trigger_type: int = 0,
                 spawn_triggered: bool = False) -> GDObject:

    return GDObject({ propertiesID.ID: TriggersID.STOP,
                      propertiesID.X: pos_x, propertiesID.Y: pos_y,
                      propertiesID.TARGET: target_group,
                      propertiesID.STOP_TRIGGER_TYPE: stop_trigger_type,
                      propertiesID.SPAWN_TRIGGERED: bool(spawn_triggered), propertiesID.MULTI_TRIGGER: int(spawn_triggered) })

def scale_trigger(pos_x: int = -15, pos_y: int = 15,
                  target_group: int = 0, center_group: int = 0,
                  duration: float = 1,
                  easing: int = 0, easing_rate: float = 2,
                  scale_x_by: float = 0, scale_y_by: float = 0,
                  div_by_x: bool = False, div_by_y: bool = False, 
                  only_move: bool = False, 
                  relative_scale: bool = False, relative_rotation: bool = False,
                  spawn_triggered: bool = False) -> GDObject:
    
    ## CENTER_GROUP: 71
    return GDObject({ propertiesID.ID: TriggersID.SCALE,
                      propertiesID.X: pos_x, propertiesID.Y: pos_y,
                      propertiesID.TARGET: target_group, propertiesID.TARGET_POS: center_group,
                      propertiesID.DURATION: round(duration, 2),
                      propertiesID.EASING: easing, propertiesID.EASING_RATE: round(easing_rate, 2),
                      propertiesID.SCALE_X_BY: round(scale_x_by, 3), propertiesID.SCALE_Y_BY: round(scale_y_by, 3),
                      propertiesID.DIV_BY_X: int(div_by_x), propertiesID.DIV_BY_Y: int(div_by_y),
                      propertiesID.ONLY_MOVE: int(only_move),
                      propertiesID.RELATIVE_SCALE: int(relative_scale), propertiesID.RELATIVE_ROTATION: int(relative_rotation),
                      propertiesID.SPAWN_TRIGGERED: int(spawn_triggered), propertiesID.MULTI_TRIGGER: int(spawn_triggered) })

def rotate_trigger(pos_x: int = -15, pos_y: int = 15,
                   target_group: int = 0, center_group: int = 0,
                   rotate_degrees: float = 0, times_360: int = 0,
                   duration: float = 1, 
                   easing: int = 0, easing_rate: float = 2,
                   spawn_triggered: bool = False) -> GDObject:
    
    return GDObject({ propertiesID.ID: TriggersID.ROTATE,
                      propertiesID.X: pos_x, propertiesID.Y: pos_y,
                      propertiesID.TARGET: target_group, propertiesID.TARGET_POS: center_group,
                      propertiesID.ROTATE_DEGREES: round(rotate_degrees, 2), propertiesID.TIMES_360: times_360,
                      propertiesID.DURATION: round(duration, 2),
                      propertiesID.EASING: easing, propertiesID.EASING_RATE: round(easing_rate, 2),
                      propertiesID.SPAWN_TRIGGERED: int(spawn_triggered), propertiesID.MULTI_TRIGGER: int(spawn_triggered) })

def random_trigger(pos_x: int = -15, pos_y: int = 15,
                   target_group_1: int = 0, target_group_2: int = 0,
                   chances: int = 50,
                   spawn_triggered: bool = False) -> GDObject:
    
    return GDObject({ propertiesID.ID: TriggersID.RANDOM,
                      propertiesID.X: pos_x, propertiesID.Y: pos_y,
                      propertiesID.TARGET: target_group_1, propertiesID.TARGET_POS: target_group_2,
                      propertiesID.DURATION: chances,
                      propertiesID.SPAWN_TRIGGERED: int(spawn_triggered), propertiesID.MULTI_TRIGGER: int(spawn_triggered) })

def adv_random_trigger(pos_x: int = -15, pos_y: int = 15,
                       group_probabilities: list[tuple[int, int]] = [],
                       spawn_triggered: bool = False):
    
    return GDObject({ propertiesID.ID: TriggersID.ADV_RANDOM,
                      propertiesID.X: pos_x, propertiesID.Y: pos_y,
                      propertiesID.GROUP_PROBABILITIES: group_probabilities,
                      propertiesID.SPAWN_TRIGGERED: int(spawn_triggered), propertiesID.MULTI_TRIGGER: int(spawn_triggered) })


def create_spawn_loop(editor: Editor, target_group: int, 
                      pos_x: int = -15, pos_y: int = 15,
                      spawn_duration: float = 0,
                      spawn_ordered: bool = False, spawn_triggered: bool = False,
                      spawn_group: int = 0 ) -> None:
    
    objects = editor.get_objects_with_group(target_group)
    
    if len(objects) == 0:
        raise Exception("There are no objects with group " + str(target_group))

    ref_obj = objects[-1]

    for i in objects: 
        i.set_property(propertiesID.SPAWN_TRIGGERED, 1)
        i.set_property(propertiesID.MULTI_TRIGGER, 1)

    first_trigger_group = editor.get_smallest_unused_group()

    first_trigger = spawn_trigger(pos_x, pos_y, target_group, True, 0, 0, spawn_ordered)
    first_trigger.add_group(first_trigger_group)
    second_trigger = spawn_trigger(ref_obj.get_property(propertiesID.X), ref_obj.get_property(propertiesID.Y) + align_to_grid(3)-15, first_trigger_group, True, spawn_duration)   
    second_trigger.add_group(target_group)   
    third_trigger = spawn_trigger(pos_x, pos_y + align_to_grid(2)-15, first_trigger_group, spawn_triggered, 0, 0, False)
    third_trigger.add_group(spawn_group)      
    
    editor.add_objects(first_trigger, second_trigger, third_trigger)       
    