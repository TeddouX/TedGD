import TedGD
import TedGD.triggers
import TedGD.editor

def main() -> None:
    gd_editor = TedGD.editor.Editor.load_level("AABB")
    gd_editor.remove_all_objects()
    
    """
    adv_rand = TedGD.triggers.adv_random_trigger( pos_x=TedGD.editor.align_to_grid(1), pos_y=TedGD.editor.align_to_grid(3),
                                                  group_probabilities=[(1, 25), (2, 40), (3, 75)],
                                                  spawn_triggered=False )

    
    rand = TedGD.triggers.random_trigger( pos_x=TedGD.editor.align_to_grid(1), pos_y=TedGD.editor.align_to_grid(3),
                                          target_group_1=18, target_group_2=19,
                                          chances=75,
                                          spawn_triggered=False )

    sc = TedGD.triggers.scale_trigger( pos_x=TedGD.editor.align_to_grid(1), pos_y=TedGD.editor.align_to_grid(3),
                                       target_group=1, center_group=2,
                                       duration=1.25,
                                       easing=TedGD.triggers.Easings.EASE_OUT, easing_rate=2.0,
                                       scale_x_by=2.75, scale_y_by=2.25,
                                       div_by_x=False, div_by_y=False,
                                       only_move=False,
                                       relative_scale=False, relative_rotation=False,
                                       spawn_triggered=False )
    
    rot = TedGD.triggers.rotate_trigger( pos_x=TedGD.editor.align_to_grid(2), pos_y=TedGD.editor.align_to_grid(3),
                                         target_group=1, center_group=2,
                                         rotate_degrees=280, times_360=4,
                                         duration=5.5,
                                         easing=TedGD.triggers.Easings.EASE_IN_OUT, easing_rate=2.0,
                                         spawn_triggered=False )

    gd_editor.add_objects(adv_rand)
    gd_editor.overwrite_gd_level()
    """


if __name__ == "__main__":
    main()
