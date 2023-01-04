from manim import *
from .seq_actor import SeqActor
from .seq_object import SeqObject

class SeqAction(AnimationGroup):
    @classmethod
    def introduce_actors(
        cls,
        *actors: SeqActor
    ) -> None:
        group = Group(*actors).move_to(ORIGIN).arrange(buff=0.25)
        animation = FadeIn(group, shift=DOWN, run_time=0.5)
        yield animation

    @classmethod
    def subject_gives_gift_to_target(
        cls,
        subject: SeqActor,
        gift: SeqObject,
        target: SeqActor
    ):
        sub_arr, sub_ani = subject.time_elapse()
        obj_arr, obj_ani = target.time_elapse()
        yield Succession(
            AnimationGroup(Create(sub_arr), Create(obj_arr)),
            AnimationGroup(sub_ani, obj_ani)
        )

        act_start = Dot(sub_arr.get_end())
        is_move_left = (obj_arr.get_end() - sub_arr.get_end())[0] > 0.0
        gift.move_to(act_start.get_center(), aligned_edge=(RIGHT if is_move_left else LEFT))
        act_end = Dot(obj_arr.get_end())
        iobj_planned_path = Arrow(
            start=act_start.get_center(),
            end=act_end.get_center(),
            buff=0,
            stroke_width=1,
            max_tip_length_to_length_ratio=0.2
        )
        iobj_moved_path = TracedPath(gift.get_center)
        mid_point = utils.space_ops.midpoint(act_start.get_center(), act_end.get_center())
        post_move_gift_label = gift.create_obj_label(font_size=16).move_to(mid_point, aligned_edge=UP)

        yield Succession(
            FadeIn(gift),
            Transform(gift, act_start, run_time=0.4),
            Create(iobj_moved_path, run_time=0.1),
            MoveAlongPath(gift, iobj_planned_path),
            AnimationGroup(
                FadeIn(iobj_planned_path, run_time=0.2),
                FadeIn(post_move_gift_label)
            )
        )