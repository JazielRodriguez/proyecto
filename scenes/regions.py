from manim import Text, LEFT, DOWN, VGroup, RIGHT, BOLD, UP, Arrow
from utils.actions import actions
from utils.colors import colors
from utils.objetos import crearRegiones, crearElectron, crearProton
from helpers.helpersregions import (
    helperUnoIzq,
    helperDosIzq,
    helperTresIzq,
    helperCuatroIzq,
    helperCincoIzq,
    helperSeisIzq,
    helperSieteIzq,
    helperOchoIzq,
    helperNueveIzq,
    helperDiezIzq,
    helperLineaUnoIzq,
    helperLineaDosIzq,
)
from helpers.helpersregions import (
    helperLineaUnoDer,
    helperLineaDosDer,
    helperLineaTresDer,
    helperLineaCuatroDer,
    helperLineaCincoDer,
    helperLineaSeisDer,
    helperLineaSieteDer,
    helperLineaOchoDer,
    helperLineaNueveDer,
    helperLineaDiezDer,
    helperUnoDer,
    helperDosDer,
)


negative = Text("-", font_size=32, color=colors["colorBlue"], weight=BOLD)
positive = Text("+", font_size=32, color=colors["colorRed"], weight=BOLD)
textAnodo = Text("Anodo", color=colors["colorBlue"], font_size=32)
textCatodo = Text("Catodo", color=colors["colorRed"], font_size=32)
negative.shift(LEFT * 0.85 + DOWN * 1.5)
positive.shift(RIGHT * 0.85 + DOWN * 1.5)
textAnodo.shift(UP * 2.35 + LEFT * 4.50)
textCatodo.shift(UP * 2.35 + RIGHT * 4.50)
regiones = VGroup(crearRegiones())
protonUno = VGroup(crearProton(UP * 2.6 + RIGHT * 0.65, 0.15))
protonDos = VGroup(crearProton(UP * 2.2 + RIGHT * 0.65, 0.15))
protonTres = VGroup(crearProton(UP * 1.8 + RIGHT * 0.65, 0.15))
protonCuatro = VGroup(crearProton(UP * 1.4 + RIGHT * 0.65, 0.15))
electronUno = VGroup(crearElectron(UP * 2.6 + LEFT * 0.65, 0.15))
electronDos = VGroup(crearElectron(UP * 2.2 + LEFT * 0.65, 0.15))
electronTres = VGroup(crearElectron(UP * 1.8 + LEFT * 0.65, 0.15))
electronCuatro = VGroup(crearElectron(UP * 1.4 + LEFT * 0.65, 0.15))
primeraFlecha = Arrow(start=UP * 2.6 + RIGHT * 0.65, end=UP * 2.6 + LEFT * 0.65)
segundaFlecha = Arrow(start=UP * 2.2 + RIGHT * 0.65, end=UP * 2.2 + LEFT * 0.65)
terceraFlecha = Arrow(start=UP * 1.8 + RIGHT * 0.65, end=UP * 1.8 + LEFT * 0.65)
cuartaFlecha = Arrow(start=UP * 1.4 + RIGHT * 0.65, end=UP * 1.4 + LEFT * 0.65)


def escenaRegiones(self):

    self.play(
        actions["fadeIn"](regiones),
        actions["write"](positive),
        actions["write"](negative),
    )
    self.wait(0.5)
    self.play(actions["write"](textAnodo), actions["write"](textCatodo))
    self.wait(1.5)
    self.play(
        actions["fadeIn"](
            protonUno,
            protonDos,
            protonTres,
            protonCuatro,
            electronUno,
            electronDos,
            electronTres,
            electronCuatro,
            helperUnoIzq,
            helperDosIzq,
            helperTresIzq,
            helperCuatroIzq,
            helperCincoIzq,
            helperSeisIzq,
            helperSieteIzq,
            helperOchoIzq,
            helperNueveIzq,
            helperDiezIzq,
            helperLineaUnoDer,
            helperLineaDosDer,
            helperLineaTresDer,
            helperLineaCuatroDer,
            helperLineaCincoDer,
            helperLineaSeisDer,
            helperLineaSieteDer,
            helperLineaOchoDer,
            helperLineaNueveDer,
            helperLineaDiezDer,
            helperLineaUnoIzq,
            helperLineaDosIzq,
            helperUnoDer,
            helperDosDer,
        )
    )
    self.wait(1)
    self.play(actions["laggedStart"](actions["growFromEdge"](primeraFlecha, RIGHT)))
    self.wait(0.25)
    self.play(actions["laggedStart"](actions["growFromEdge"](segundaFlecha, RIGHT)))
    self.wait(0.25)
    self.play(actions["laggedStart"](actions["growFromEdge"](terceraFlecha, RIGHT)))
    self.wait(0.25)
    self.play(actions["laggedStart"](actions["growFromEdge"](cuartaFlecha, RIGHT)))
    self.wait(0.25)
    self.play(
        helperLineaUnoIzq.animate.move_to(UP*2.2+LEFT*2.5),
        helperLineaDosIzq.animate.move_to(UP*2.08+LEFT*2.42),
        helperSeisIzq.animate.move_to(UP*2.4+LEFT*2.4),
        helperSieteIzq.animate.move_to(UP*2.56+LEFT*2.6),
        helperOchoIzq.animate.move_to(UP*1.7+LEFT*2.37),
        helperNueveIzq.animate.move_to(UP * 1.4 + LEFT * 2.55),
        helperDiezIzq.animate.move_to(UP * 1.32 + LEFT * 2.30),
    )
