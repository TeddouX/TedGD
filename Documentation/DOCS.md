
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
- `overwrite_gd_level()` used to overwrite the Geometry Dash level with the name that was passed in the constructor  
- `backup()` used to backup all the objects into a backup file  
- `add_object(object: GDObject)` add an [object](#GDObject) to the editor  
- `add_objects(*objects: GDObject)` add multiple [objects](#GDObject) to the editor  
- `remove_all_objects()` remove all objects from the editor  
- `get_all_groups() -> list[int]` returns a list of all used groups  
- `get_objects_with_group(group: int) -> list[GDObject]` returns a list of all [GDObjects](#GDObject) with the group

### Variables
- `level_name: str` your level's name  
- `objects: list[GDObject]` a list of all the editor's objects

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
- `align_to_grid(grid_pos: int) -> int` aligns an object on the Geometry Dash's editor grid

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
- `from_robtop() -> GDObject` creates a - `GDObject` from a RobTop properties string  
- `set_property(prop: int, val: Any)` sets a [property](#PropertiesID) from the object   
- `get_property(prop: int) -> Any` returns a [property](#PropertiesID) from the object
- `add_groups(groups: list[int])` adds all groups from the list to the object's groups
- `add_group(group: int)` adds the group to the object's add_groups
- `get_groups() -> list[int]` returns all the object's groups
- `to_robtop() -> str` returns the RobTop properties string of the object 

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
Contains a list of all the properties' IDs. Used for the creation of [GDObjects](#GDObject). A list of all these properties can be found here: [propertiesID.py](../TedGD/Properties/propertiesID.py) 

#### Usage
```python
propertiesID.ID # The id of an object
propertiesID.X # The x position of an object
propertiesID.Y # The y position of an object
```

## Triggers
### Move
Can be imported from `TedGD.Triggers.triggers`. 

#### Arguments
- `pos_x: int` the x position of the trigger.  
- `pos_y: int` the y position of the trigger.  
- `move_x: int` the x movement of the object.   
- `move_y: int` the y movement of the object.  
- `easing: int` the easing of the object (can be imported from `TedGD.Triggers.triggers`).
- `easing_rate: float` (*rounded to 0.01*) the easing rate.  
- `duration: float` (*rounded to 0.01*) the duration of the movement.  
- `target_group: int` the group that will be affected by the movement.  
- `lock_to_player_x: bool` if the movement is locked to the player x position.  
- `lock_to_player_y: bool` if the movement is locked to the player y position.  
- `x_mod: float` (*rounded to 0.001*) the multiplier of the lock_to_player_x.  
- `y_mod: float` (*rounded to 0.001*) the multiplier of the lock_to_player_y.  
- `spawn_triggered: bool` if the movement is triggered by a spawn trigger.

#### Usage
```python
mv = move_trigger( pos_x=15, pos_y=15, 
                  move_x=100, move_y=50, 
                  easing=TedGD.Triggers.easings.EASE_IN_OUT, easing_rate=1.5, 
                  duration=5.5, 
                  target_group=15, 
                  lock_to_player_x=False, lock_to_player_y= False, 
                  x_mod=0, y_mod=0, 
                  spawn_triggered=False )
```

### Color
Can be imported from `TedGD.Triggers.triggers`. 

#### Arguments
- `pos_x: int` the x position of the trigger.  
- `pos_y: int` the y position of the trigger.   
- `color: TedGD.Triggers.Color.RGB` the color that will be changed (can be imported from `TedGD.Triggers.color`).  
- `fade_duration: float` (*rounded to 0.01*) the time that the color will take to fade in.  
- `opacity: float` (*rounded to 0.01*) the opacity of the color.  
- `target_color_channel: int` the color channel that will be affected, can be a number or a default channel (can be imported from `TedGD.Triggers.color`).  
- `blending: bool` if the color is blending or not.  
- `spawn_triggered: bool` if the movement is triggered by a spawn trigger.

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
Can be imported from `TedGD.Triggers.triggers`. 

#### Arguments
- `pos_x: int` the x position of the trigger.  
- `pos_y: int` the y position of the trigger.   
- `target_group: int` the group that is spawned by the trigger.  
- `spawn_duration: float` (*rounded to 0.0001*) the time that the trigger will take to spawn the group.  
- `spawn_duration_variation: float` (*rounded to 0.0001*) randomizer (spawn_duration +/- spawn_duration_variation).  
- `spawn_ordered: bool` if the spawn trigger executes the group in order (left to right).  
- `spawn_triggered: bool` if the movement is triggered by a spawn trigger.

#### Usage
```python
col = color_trigger( pos_x=15, pos_y=15, 
                  target_group=12,
                  spawn_duration=1.19, spawn_duration_variation=0.0,
                  spawn_ordered=True,
                  spawn_triggered=False )
```

### Toggle
Can be imported from `TedGD.Triggers.triggers`. 

#### Arguments
- `pos_x: int` the x position of the trigger.  
- `pos_y: int` the y position of the trigger.   
- `target_group: int` the group that is spawned by the trigger.  
- `activate_group: bool` if the group is activated or not.   
- `spawn_triggered: bool` if the movement is triggered by a spawn trigger.

#### Usage
```python
tog = toggle_trigger( pos_x=15, pos_y=15, 
                      target_group=13,
                      activate_group=False
                      spawn_triggered=False )
```

### Stop
Can be imported from `TedGD.Triggers.triggers`. 

#### Arguments
- `pos_x: int` the x position of the trigger.  
- `pos_y: int` the y position of the trigger.   
- `target_group: int` the group that is spawned by the trigger.  
- `stop_trigger_type: bool` the type of the stop trigger (stop, pause, resume), imported from `TedGD.Triggers.triggers`.  
- `spawn_triggered: bool` if the movement is triggered by a spawn trigger.

#### Usage
```python
tog = toggle_trigger( pos_x=15, pos_y=15, 
                      target_group=13,
                      stop_trigger_type=TedGD.triggers.STOP_TRIGGER_PAUSE
                      spawn_triggered=False )
```

### Create Spawn Loop 
Can be imported from `TedGD.Triggers.triggers`. 
Used to create a spawn loop (a infinite loop that spawns continuously triggers).

#### Arguments
- `editor: TedGD.editor.Editor` (**REQUIRED**) the editor that you want your spawn loop to be put in.  
- `target_group: int` (**REQUIRED**) the group that will be triggered by the loop.  
- `pos_x: int` the x position of the trigger that will start the loop.  
- `pos_y: int` the y position of the trigger that will start the loop.  
- `spawn_duration: float` (*rounded to 0.0001*) the time the loop take to restart an iteration.  
- `spawn_ordered: bool` if the spawn trigger executes the group in order (left to right).   
- `spawn_group: int` the group that is used to start the loop.  


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