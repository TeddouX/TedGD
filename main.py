from TedGD import editor, gdobject
from TedGD.IDs import p

def main() -> None:
    gd_editor = editor.Editor.load_level("AABB")
    print(gd_editor.objects)
    gd_editor.remove_all_objects()
    gd_editor.overwrite_gd_level()

if __name__ == "__main__":
    main()
