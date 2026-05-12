from manim import BOLD, Text, DOWN, VGroup, UP, RIGHT, LEFT, MathTex
from utils.actions import actions
from utils.colors import colors
from utils.objetos import crearLed, crearFoton


def escenaComparacionLed(self):
    isNotTheSame = MathTex(r"\boldsymbol{\neq}", font_size=96)
    fotodiodoText = Text("Fotodiodo", font_size=32, color=colors["colorWhite"])
    ledText = Text("Led", font_size=32, color=colors["colorWhite"])
    led = crearLed()
    led.move_to(RIGHT * 4)
    corrienteNegativa = Text("-", font_size=24, color=colors["colorBlue"], weight=BOLD)
    corrientePositiva = Text("+", font_size=24, color=colors["colorRed"], weight=BOLD)
    corrienteNegativa.shift(RIGHT * 4.5 + DOWN * 1.90)
    corrientePositiva.shift(RIGHT * 3.5 + DOWN * 1.9)

    positionEntradaFoton = UP * 4.5 + LEFT * 4
    positionSalidaFoton = UP * 2.15 + RIGHT * 4
    positionFinalEntradaFoton = UP * 2.15 + LEFT * 4
    positionFinalSalidaFoton = UP * 4.5 + RIGHT * 4

    fotonEntradaUno = VGroup(crearFoton(positionEntradaFoton))
    fotonEntradaDos = VGroup(crearFoton(positionEntradaFoton))
    fotonEntradaTres = VGroup(crearFoton(positionEntradaFoton))

    fotonSalidaUno = VGroup(crearFoton(positionSalidaFoton))
    fotonSalidaDos = VGroup(crearFoton(positionSalidaFoton))
    fotonSalidaTres = VGroup(crearFoton(positionSalidaFoton))

    ledText.shift(UP * 3.5 + RIGHT * 3)
    fotodiodoText.shift(UP * 3.5 + LEFT * 3)

    self.play(
        self.fotodiodo.animate.move_to(LEFT * 4),
        self.corrienteNegativa.animate.move_to(LEFT * 4.5 + DOWN * 1.90),
        self.corrientePositiva.animate.move_to(LEFT * 3.5 + DOWN * 1.90),
        actions["fadeOut"](self.cathode),
        actions["fadeOut"](self.anode),
        actions["fadeOut"](self.entradaDeLuz),
    )
    self.play(
        actions["fadeIn"](led),
        actions["write"](corrientePositiva),
        actions["write"](corrienteNegativa),
    )
    self.play(
        actions["write"](isNotTheSame),
        actions["write"](fotodiodoText),
        actions["write"](ledText),
    )
    self.wait(0.5)
    self.play(actions["fadeOut"](
        fotodiodoText,ledText
    ))
    self.play(actions["fadeIn"](fotonSalidaUno))
    self.play(
        fotonEntradaUno.animate.move_to(positionFinalEntradaFoton),
        fotonSalidaUno.animate.move_to(positionFinalSalidaFoton),
    )
    self.wait(0.5)
    self.play(
        actions["fadeOut"](fotonEntradaUno),
        actions["fadeOut"](fotonSalidaUno),
        actions["fadeIn"](fotonSalidaDos),
    )
    self.play(
        fotonEntradaDos.animate.move_to(positionFinalEntradaFoton),
        fotonSalidaDos.animate.move_to(positionFinalSalidaFoton),
    )
    self.wait(0.5)
    self.play(
        actions["fadeOut"](fotonEntradaDos),
        actions["fadeOut"](fotonSalidaDos),
        actions["fadeIn"](fotonSalidaTres),
    )
    self.play(
        fotonEntradaTres.animate.move_to(positionFinalEntradaFoton),
        fotonSalidaTres.animate.move_to(positionFinalSalidaFoton),
    )
    self.wait(0.5)
    self.play(actions["fadeOut"](fotonEntradaTres), actions["fadeOut"](fotonSalidaTres))
    self.play(actions["fadeOut"](*self.mobjects))
    self.wait(1)

