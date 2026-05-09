from manim import BOLD, DOWN, UP, Text
from utils.actions import actions
from utils.colors import colors


def titulo(self):
    titulo = Text(
        "Efecto Fotoeléctrico", font_size=52, color=colors["colorYellow"], weight=BOLD
    )
    subtitulo = Text(
        "Albert Einstein · Nobel de Física 1921",
        font_size=26,
        color=colors["colorGrayB"],
    )
    subtitulo.next_to(titulo, DOWN, buff=0.4)

    self.play(actions["write"](titulo), run_time=1.5)
    self.play(actions["fadeIn"](subtitulo, shift=UP * 0.3))
    self.wait(1.5)
    self.play(actions["fadeOut"](titulo), actions["fadeOut"](subtitulo))
