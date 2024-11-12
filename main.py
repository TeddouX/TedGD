from TedGD import editor, gdobject
from TedGD.IDs import p

def main() -> None:
    gd_editor = editor.Editor.load_level("AABB")
    test_object = gdobject.GDObject({1: 1, 2: 15, 3: 15, 155: 1})
    gd_editor.add_object(test_object)

    gd_editor.overwrite_gd_level()

if __name__ == "__main__":
    main()
