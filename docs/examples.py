from manim import *
from manim_sequence_diagram import *

class ClientRaceDatabaseNetwork(MovingCameraScene):
    def construct(self):
        actor_client = SeqActor(name="client")
        actor_delivery = SeqActor(name="delivery")
        actor_server = SeqActor(name="server")
        actor_db = SeqActor(name="database")
        for anime in SeqAction.introduce_actors(actor_client, actor_server, actor_delivery, actor_db):
            self.play(anime)

        # Move the camera yourself!
        self.play(self.camera.frame.animate.move_to(DOWN * 3))

        for anime in SeqAction.subject_gives_gift_to_target(
            subject=actor_client,
            gift=SeqObject(name="async getData"),
            target=actor_delivery
        ):
            self.play(anime)

        delivery_to_db_animes = SeqAction.subject_gives_gift_to_target(
            subject=actor_delivery,
            gift=SeqObject(name="fast fetchFromDB"),
            target=actor_db
        )
        delivery_to_server_animes = SeqAction.subject_gives_gift_to_target(
            subject=actor_delivery,
            gift=SeqObject(name="slow fetchFromServer"),
            target=actor_server
        )

        # Concurrent tasks can be shown by zipping together
        # existing animations
        for (db_anime, server_anime) in zip(delivery_to_db_animes, delivery_to_server_animes):
            self.play(db_anime)
            self.play(server_anime)

        for anime in SeqAction.subject_gives_gift_to_target(
            subject=actor_db,
            gift=SeqObject(name="data.json"),
            target=actor_delivery
        ):
            self.play(anime)

        for anime in SeqAction.subject_gives_gift_to_target(
            subject=actor_delivery,
            gift=SeqObject(name="<Render data=(data.json)>"),
            target=actor_client
        ):
            self.play(anime)

        for anime in SeqAction.subject_gives_gift_to_target(
            subject=actor_server,
            gift=SeqObject(name="data.json"),
            target=actor_delivery
        ):
            self.play(anime)

        for anime in SeqAction.subject_gives_gift_to_target(
            subject=actor_delivery,
            gift=SeqObject(name="ignore server response"),
            target=actor_delivery
        ):
            self.play(anime)
