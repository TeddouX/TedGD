from TedGD import editor, gdobject
from TedGD.Properties import propertiesID, properties
from TedGD.Triggers import triggers, easings, color

def main() -> None:
    gd_editor = editor.Editor.load_level("AABB")
    gd_editor.remove_all_objects()

    red = triggers.color_trigger(editor.align_to_grid(5), editor.align_to_grid(5), color.RGB(255, 0, 0), 0.1, target_color_channel=color.CHANNEL_BG)
    green = triggers.color_trigger(editor.align_to_grid(10), editor.align_to_grid(5), color.RGB(0, 255, 0), 0.1, target_color_channel=color.CHANNEL_BG)
    blue = triggers.color_trigger(editor.align_to_grid(15), editor.align_to_grid(5), color.RGB(0, 0, 255), 0.1, target_color_channel=color.CHANNEL_BG)
    red.add_group(1)
    green.add_group(1)
    blue.add_group(1)

    gd_editor.add_objects(red, green, blue)

    triggers.create_spawn_loop(gd_editor, 1, editor.align_to_grid(0), editor.align_to_grid(5), True, False, 0, 0.25)

    gd_editor.overwrite_gd_level()

if __name__ == "__main__":
    main()
