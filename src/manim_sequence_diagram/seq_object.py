from manim import *

class SeqObject(VGroup):
    def __init__(
        self,
        name: str,
        font_size: float = 18
    ):
        self.obj_name = name
        obj_label = self.create_obj_label(font_size)
        obj_ctn = Rectangle(
            color='#00FF00',
            height=obj_label.height + 0.5,
            width=obj_label.width + 0.4
        )
        # TODO: figure out a way to show json data
        # or alternatively code snippets
        obj_label.align_to(obj_ctn, ORIGIN)
        super().__init__(obj_ctn, obj_label)

    def create_obj_label(self, font_size: float = 18):
        return Text(self.obj_name, font_size=font_size).set_color(WHITE)
