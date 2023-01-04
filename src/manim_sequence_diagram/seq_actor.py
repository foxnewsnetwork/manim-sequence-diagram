from manim import *
from .constants import HALF_DOWN

class SeqActor(VGroup):
    all_actors = list()

    @classmethod
    def get_deepest_actor(cls):
        latest_contenter = None
        for actor in cls.all_actors:
            if latest_contenter is None or (actor.get_time_depth() > latest_contenter.get_time_depth()):
                latest_contenter = actor
        return latest_contenter

    def __init__(
        self,
        name: str,
        font_size: float = 24,
    ):
        self.actor_name = name
        actor_label = Text(name, font_size=font_size).set_color(WHITE)
        self.actor_ctn = Rectangle(
            color='#FFFFFF',
            height=actor_label.height + 0.2,
            width=actor_label.width + 0.2
        )
        actor_label.align_to(self.actor_ctn, ORIGIN)
        self.actor_timedot = Dot(self.actor_ctn.get_edge_center(DOWN))
        self.actor_timedot_y_displace = self.actor_timedot.get_y() - self.actor_ctn.get_y()
        SeqActor.all_actors.append(self)
        self.actor_timepath = VMobject()
        timepath_updater = lambda x: x.become(Line(self.actor_ctn.get_edge_center(DOWN), self.actor_timedot.get_center()))
        self.actor_timepath.add_updater(timepath_updater)
        # actor_svg = fa.regular.bell
        super().__init__(self.actor_ctn, actor_label, self.actor_timedot)

    def get_time_depth(self) -> int:
        timedot = self.actor_timedot
        return round((timedot.get_center()[1] - self.actor_timedot_y_displace) / HALF_DOWN[1])

    def time_elapse(self, ticks_to_elapse: int = 1):
        deepest_actor = SeqActor.get_deepest_actor()
        time_ticks = deepest_actor.get_time_depth() + ticks_to_elapse
        latest_time_reached = HALF_DOWN * time_ticks
        curr_dot_pos = self.actor_timedot.get_center()
        next_dot_pos = curr_dot_pos.copy()
        next_dot_pos[1] = latest_time_reached[1]
        timeline = Line(
            start=curr_dot_pos,
            end=next_dot_pos
        )
        time_anime = MoveAlongPath(self.actor_timedot, path=timeline, run_time=0.25)
        return timeline, time_anime