from manim import BOLD, DOWN, UP, Text
from utils.actions import actions
from utils.colors import colors


def titulo(self):
    titulo = Text(
        "Efecto Fotoeléctrico", font_size=52, color=colors["colorYellow"], weight=BOLD
    )
    subtitulo = Text(
        "Brayan Monroy Hernandez \nAbraham Amado Moreno Magos \nOsmar Greco Franco Lopez \nJaziel Aldair Rodriguez Mendoza ",
        font_size=26,
        color=colors["colorWhite"],
    )
    subtitulo.next_to(titulo, DOWN, buff=0.4)

    self.play(actions["write"](titulo), run_time=1.5)
    self.play(actions["write"](subtitulo), shift=UP * 0.3, run_time=5)
    self.wait(1.5)
    self.play(actions["fadeOut"](titulo), actions["fadeOut"](subtitulo))
