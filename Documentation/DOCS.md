
# Documentation

 - [Editor](#Editor)
 - [GDObject](#GDObject)
 - [PropertiesID](#PropertiesID)
 - [Triggers](#Triggers)
   - [Move](#Move)
   - [Color](#Color)
   - [Spawn](#Spawn)
   - [Toggle](#Toggle)
   - [Stop](#Stop)
   - [Scale](#Scale)
   - [Rotate](#Rotate)
   - [Random](#Random)
   - [Advanced Random](#advanced-random)
   - [Create Spawn Loop](#create-spawn-loop)


## Editor
Can be imported from `TedGD.editor`
### Creation
The Editor needs to be created from a method:
```python
Editor.load_empty() # Load an empty level
Editor.load_level() # Load an already axisting level
Editor.load_backup() # Load a level from a backup
```
Each of these methods takes an argument `level_name: str` and will return a `TedGD.editor.Editor`

### Methods
- `overwrite_gd_level()` Used to overwrite the Geometry Dash level with the name that was passed in the constructor  
- `backup()` Used to backup all the objects into a backup file  
- `add_object(object: GDObject)` Add an [object](#GDObject) to the editor  
- `add_objects(*objects: GDObject)` Add multiple [objects](#GDObject) to the editor  
- `remove_all_objects()` Remove all objects from the editor  
- `get_all_groups() -> list[int]` Returns a list of all used groups  
- `get_objects_with_group(group: int) -> list[GDObject]` Returns a list of all [GDObjects](#GDObject) with the group

### Variables
- `level_name: str` Your level's name  
- `objects: list[GDObject]` A list of all the editor's objects

### Example
```python
# Create the editor
gd_editor = TedGD.editor.Editor.load_level("My Level")

# Delete all objects
gd_editor.remove_all_objects()

# Add an object
gd_editor.add_object(my_object)

# Overwrite "My Level"
gd_editor.overwrite_gd_level()
```

### Functions
- `align_to_grid(grid_pos: int) -> int` Aligns an object on the Geometry Dash's editor grid

## GDObject
Can be imported from `TedGD.gdobject`

### Creation
Can be created with the default constructor `GDObject(properties_: dict[int,])` where `properties_` is a dict of [properties](#PropertiesID) associated with their value.

#### Usage
```python
# Create a GDObject
my_object = GDObject({ propertiesID.X: 15, propertiesID.Y: 15 })
```
The `propertiesID.ID` is by default 1. For more information about the propertiesID can be found here: [propertiesID](#PropertiesID)

### Methods 
- `from_robtop() -> GDObject` Creates a - `GDObject` from a RobTop properties string  
- `set_property(prop: int, val: Any)` Sets a [property](#PropertiesID) from the object   
- `get_property(prop: int) -> Any` Returns a [property](#PropertiesID) from the object
- `add_groups(groups: list[int])` Adds all groups from the list to the object's groups
- `add_group(group: int)` Adds the group to the object's add_groups
- `get_groups() -> list[int]` Returns all the object's groups
- `to_robtop() -> str` Returns the RobTop properties string of the object 

### Variables
There are no variables associated with this class.

### Usage
```python
# Create an editor
gd_editor = TedGD.editor.Editor("My Level")

# Creates GDObjects 
my_object = TedGD.gdobject.GDObject({ propertiesID.X: 15, propertiesID.Y: 15 })
my_second_object = TedGD.gdobject.GDObject({ propertiesID.X: 200, propertiesID.Y: -200 })

# Add the GDObjects to the editor
gd_editor.add_objects(my_object, my_second_object)

# Overwrite "My Level"
gd_editor.overwrite_gd_level()
```


## PropertiesID
Can be imported from `TedGD.properties`.  
Contains a list of all the properties' IDs. Used for the creation of [GDObjects](#GDObject). A list of all these properties can be found here: [propertiesID.py](../TedGD/propertiesID.py) 

#### Usage
```python
propertiesID.ID # The id of an object
propertiesID.X # The x position of an object
propertiesID.Y # The y position of an object
```

## Triggers
### Move
Can be imported from `TedGD.triggers`. 

#### Arguments
- `pos_x: int` The x position of the trigger.  
- `pos_y: int` The y position of the trigger.  
- `move_x: int` The x movement of the object.   
- `move_y: int` The y movement of the object.  
- `easing: int` The easing of the object (can be imported from `TedGD.triggers`). 
- `easing_rate: float` (*rounded to 0.01*) The easing rate.  
- `duration: float` (*rounded to 0.01*) The duration of the movement.  
- `target_group: int` The group that will be affected by the movement.  
- `lock_to_player_x: bool` If the movement is locked to the player x position.  
- `lock_to_player_y: bool` If the movement is locked to the player y position.  
- `x_mod: float` (*rounded to 0.001*) The multiplier of the lock_to_player_x.  
- `y_mod: float` (*rounded to 0.001*) The multiplier of the lock_to_player_y.  
- `spawn_triggered: bool` If the trigger is triggered by a spawn trigger.

#### Usage
```python
mv = move_trigger( pos_x=15, pos_y=15, 
                   move_x=100, move_y=50, 
                   easing=TedGD.triggers.Easings.EASE_IN_OUT, easing_rate=1.5, 
                   duration=5.5, 
                   target_group=15, 
                   lock_to_player_x=False, lock_to_player_y= False, 
                   x_mod=0, y_mod=0, 
                   spawn_triggered=False )
```

### Color
Can be imported from `TedGD.triggers`. 

#### Arguments
- `pos_x: int` The x position of the trigger.  
- `pos_y: int` The y position of the trigger.   
- `color: TedGD.Triggers.Color.RGB` The color that will be changed (can be imported from `TedGD.Triggers.color`).  
- `fade_duration: float` (*rounded to 0.01*) The time that the color will take to fade in.  
- `opacity: float` (*rounded to 0.01*) The opacity of the color.  
- `target_color_channel: int` The color channel that will be affected, can be a number or a default channel (can be imported from `TedGD.color`).  
- `blending: bool` If the color is blending or not.  
- `spawn_triggered: bool` If the trigger is triggered by a spawn trigger.

#### Usage
```python
col = color_trigger( pos_x=15, pos_y=15, 
                     color=TedGD.Triggers.color.RGB(255, 255, 127),
                     fade_duration=1.5,
                     opacity=1,
                     target_color_channel=TedGD.Triggers.color.CHANNEL_BG,
                     blending=False,
                     spawn_triggered=False )
```

### Spawn
Can be imported from `TedGD.triggers`. 

#### Arguments
- `pos_x: int` The x position of the trigger.  
- `pos_y: int` The y position of the trigger.   
- `target_group: int` The group that is spawned by the trigger.  
- `spawn_duration: float` (*rounded to 0.0001*) the time that the trigger will take to spawn the group.  
- `spawn_duration_variation: float` (*rounded to 0.0001*) Randomizer (spawn_duration +/- spawn_duration_variation).  
- `spawn_ordered: bool` If the spawn trigger executes the group in order (left to right).  
- `spawn_triggered: bool` If the trigger is triggered by a spawn trigger.

#### Usage
```python
col = color_trigger( pos_x=15, pos_y=15, 
                  target_group=12,
                  spawn_duration=1.19, spawn_duration_variation=0.0,
                  spawn_ordered=True,
                  spawn_triggered=False )
```

### Toggle
Can be imported from `TedGD.triggers`. 

#### Arguments
- `pos_x: int` The x position of the trigger.  
- `pos_y: int` The y position of the trigger.   
- `target_group: int` The group that is spawned by the trigger.  
- `activate_group: bool` If the group is activated or not.   
- `spawn_triggered: bool` If the trigger is triggered by a spawn trigger.

#### Usage
```python
tog = toggle_trigger( pos_x=15, pos_y=15, 
                      target_group=13,
                      activate_group=False
                      spawn_triggered=False )
```

### Stop
Can be imported from `TedGD.triggers`. 

#### Arguments
- `pos_x: int` The x position of the trigger.  
- `pos_y: int` The y position of the trigger.   
- `target_group: int` The group that is spawned by the trigger.  
- `stop_trigger_type: bool` The type of the stop trigger (stop, pause, resume), imported from `TedGD.triggers`.  
- `spawn_triggered: bool` If the trigger is triggered by a spawn trigger.

#### Usage
```python
stop = stop_trigger( pos_x=15, pos_y=15, 
                     target_group=13,
                     stop_trigger_type=TedGD.triggers.STOP_TRIGGER_PAUSE
                     spawn_triggered=False )
```

### Scale
Can be imported from `TedGD.triggers`. 

#### Arguments
- `pos_x: int` The x position of the trigger.  
- `pos_y: int` The y position of the trigger.   
- `target_group: int` The group that is scaled by the trigger.  
- `target_group: int` The center the objects should scale from.  
- `duration: float` (*rounded to 0.01*) The duration of the scale.  
- `easing: int` The easing of the object (can be imported from `TedGD.triggers`). 
- `easing_rate: float` (*rounded to 0.01*) The easing rate.  
- `scale_by_x: float` (*rounedd to 0.001*) The amount of scaling on the x axis.  
- `scale_by_y: float` (*rounedd to 0.001*) The amount of scaling on the y axis.
- `div_by_x: bool` Divides the current x scale by this number and uses this as the target value.  
- `div_by_y: bool` Divides the current y scale by this number and uses this as the target value.  
-  `only_move: bool` The objects will only move to the place they would be when you scale them. They will not change their size.
- `relative_rotation: bool` When blocks are rotated, they will rotate their X-axis and Y-axis as well.
- `relative_scale: bool` This option makes the scale value adjust based on a reference object.
- `spawn_triggered: bool` If the trigger is triggered by a spawn trigger.

#### Usage
```python
sc = TedGD.triggers.scale_trigger( pos_x=TedGD.editor.align_to_grid(1), 
                                  pos_y=TedGD.editor.align_to_grid(3),
                                  target_group=1, center_group=2,
                                  duration=1.25,
                                  easing=TedGD.triggers.Easings.EASE_OUT, easing_rate=2.0,
                                  scale_x_by=2.75, scale_y_by=2.25,
                                  div_by_x=False, div_by_y=False,
                                  only_move=False,
                                  relative_scale=False, relative_rotation=False,
                                  spawn_triggered=False )
```

### Rotate
Can be imported from `TedGD.triggers`. 

#### Arguments
- `pos_x: int` The x position of the trigger.  
- `pos_y: int` The y position of the trigger.  
- `target_group: int` The group that will be affected by the movement.  
- `center_group: int` The group that will be used as a center for the rotation.  
- `rotate_degrees: float` (*rounded to 0.01*) The number of degrees the object will be rotated by.   
- `times_360: int` The number of times that the object will make a full rotation.  
- `duration: float` (*rounded to 0.01*) The duration of the movement.  
- `easing: int` The easing of the object (can be imported from `TedGD.triggers`). 
- `easing_rate: float` (*rounded to 0.01*) The easing rate.  
- `spawn_triggered: bool` If the trigger is triggered by a spawn trigger.

#### Usage
```python
rot = TedGD.triggers.rotate_trigger( pos_x=TedGD.editor.align_to_grid(2), 
                                    pos_y=TedGD.editor.align_to_grid(3),
                                    target_group=1, center_group=2,
                                    rotate_degrees=280, times_360=4,
                                    duration=5.5,
                                    easing=TedGD.triggers.Easings.EASE_IN_OUT, easing_rate=2.0,
                                    spawn_triggered=False )
```

### Random
Can be imported from `TedGD.triggers`. 

#### Arguments
- `pos_x: int` The x position of the trigger.  
- `pos_y: int` The y position of the trigger. 
- `target_group_1: int` The first group that will be triggered.
- `target_group_2: int` The second group that will be triggered.
- `chances: int` The chance that "target_group_1" is triggered. For example, if this is set to 80, "Group ID 1" has an 80% chance of being triggered, while "target_group_2" has a chance of 100% - 80% = 20%.
- `spawn_triggered: bool` If the trigger is triggered by a spawn trigger.

#### Usage
```python
rand = TedGD.triggers.random_trigger( pos_x=TedGD.editor.align_to_grid(1), 
                                     pos_y=TedGD.editor.align_to_grid(3),
                                     target_group_1=18, target_group_2=19,
                                     chances=75,
                                     spawn_triggered=False )
```

### Advanced Random
Can be imported from `TedGD.triggers`. 

#### Arguments
- `pos_x: int` The x position of the trigger.  
- `pos_y: int` The y position of the trigger. 
- `group_probabilities: list[tuple[int, int]]` List of tuples each with a group and a probability: [(*group_1*, *probability_1*), (*group_n*, *probability_n*)]
- `spawn_triggered: bool` If the trigger is triggered by a spawn trigger.

#### Usage
```python
acv_rand = TedGD.triggers.adv_random_trigger( pos_x=TedGD.editor.align_to_grid(1), 
                                             pos_y=TedGD.editor.align_to_grid(3),
                                             group_probabilities=[(1, 50), (2, 75), (3, 25)],
                                             spawn_triggered=False )
```

### Create Spawn Loop 
Can be imported from `TedGD.triggers`. 
Used to create a spawn loop (a infinite loop that spawns continuously triggers).

#### Arguments
- `editor: TedGD.editor.Editor` (**REQUIRED**) The editor that you want your spawn loop to be put in.  
- `target_group: int` (**REQUIRED**) The group that will be triggered by the loop.  
- `pos_x: int` The x position of the trigger that will start the loop.  
- `pos_y: int` The y position of the trigger that will start the loop.  
- `spawn_duration: float` (*rounded to 0.0001*) The time the loop take to restart an iteration.  
- `spawn_ordered: bool` If the spawn trigger executes the group in order (left to right).   
- `spawn_group: int` The gr1oup that is used to start the loop.  
- `spawn_triggered: bool` If the loop is triggered by a spawn trigger.

#### Usage
```python
loop = create_spawn_loop( editor=gd_editor, 
                          target_group=18, 
                          pos_x=TedGD.editor.align_to_grid(13), 
                          pos_y=TedGD.editor.align_to_grid(5),
                          spawn_ordered=True, 
                          spawn_triggered=False,
                          spawn_group=0,
                          spawn_duration=1.75 )
```