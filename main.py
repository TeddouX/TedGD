from TedGD import editor, gdobject
from TedGD.Properties import properties
from TedGD.Properties.IDs import p

def main() -> None:
    gd_editor = editor.Editor.load_level("AABB")

    obj = gdobject.GDObject()
    obj.add_groups([1, 2, 3])
    obj.add_groups([4, 5, 6])

    gd_editor.add_object(obj)

    print(gd_editor.objects)

    gd_editor.overwrite_gd_level()

if __name__ == "__main__":
    main()
