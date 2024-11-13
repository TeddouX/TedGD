from TedGD import editor, gdobject
from TedGD.Properties import properties
from TedGD.Properties.IDs import p

def main() -> None:
    gd_editor = editor.Editor.load_level("AABB")
    gd_editor.remove_all_objects()
    gd_editor.overwrite_gd_level()

if __name__ == "__main__":
    main()
