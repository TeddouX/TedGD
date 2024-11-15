from TedGD import editor, gdobject
from TedGD.Properties import propertiesID, properties
from TedGD.Triggers import triggers, easings, color

def main() -> None:
    gd_editor = editor.Editor.load_level("AABB")
    print(gd_editor.objects)

if __name__ == "__main__":
    main()
