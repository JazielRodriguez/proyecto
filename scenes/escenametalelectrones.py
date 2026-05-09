from manim import LEFT, DOWN, ORIGIN, RIGHT, VGroup, Text, UP
from utils.colors import colors
from utils.actions import actions
from utils.objetos import superficie, crearElectron


def metalElectrones(self):
    metal = superficie()

    # Electrones atrapados en la superficie
    posiciones_e = [
        LEFT * 3 + DOWN * 2.2,
        LEFT * 1.5 + DOWN * 2.4,
        ORIGIN + DOWN * 2.1,
        RIGHT * 1.5 + DOWN * 2.3,
        RIGHT * 3 + DOWN * 2.2,
    ]
    electrones = VGroup(*[crearElectron(p) for p in posiciones_e])

    titulo = Text(
        "Electrones ligados al metal", font_size=28, color=colors["colorWhite"]
    )
    titulo.to_edge(UP, buff=0.4)

    self.play(actions["fadeIn"](metal), actions["write"](titulo))
    self.play(
        actions["laggedStart"](
            *[actions["growFromCenter"](e) for e in electrones], lag_ratio=0.2
        )
    )
    self.wait(1.2)

    # Guardar para siguiente escena
    self.metal = metal
    self.electrones_base = electrones
    self.titulo_base = titulo
