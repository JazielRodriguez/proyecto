from utils.objetos import crearRegiones, crearProton, crearElectron, crearHazDeLuz
from utils.actions import actions
from manim import UP, RIGHT, VGroup, LEFT, Arrow, Brace, Text, DOWN, Line
from utils.colors import colors
from utils.objetos import helperParaRegions
from helpers.helpersregions import (
    corrienteUno,
    corrienteDos,
    corrienteTres,
    corrienteCuatro,
    corrienteCinco,
    corrienteSeis,
    corrienteSiete,
    corrienteOcho,
    corrienteNueve,
    corrienteDiez,
)

protonUno = VGroup(crearProton(UP * 2.6 + RIGHT * 0.65, 0.15))
protonDos = VGroup(crearProton(UP * 2.2 + RIGHT * 0.65, 0.15))
protonTres = VGroup(crearProton(UP * 1.4 + RIGHT * 0.65, 0.15))
electronUno = VGroup(crearElectron(UP * 2.6 + LEFT * 0.65, 0.15))
electronDos = VGroup(crearElectron(UP * 2.2 + LEFT * 0.65, 0.15))
electronTres = VGroup(crearElectron(UP * 1.4 + LEFT * 0.65, 0.15))
primeraFlecha = Arrow(start=UP * 2.6 + RIGHT * 0.65, end=UP * 2.6 + LEFT * 0.65)
segundaFlecha = Arrow(start=UP * 2.2 + RIGHT * 0.65, end=UP * 2.2 + LEFT * 0.65)
terceraFlecha = Arrow(start=UP * 1.4 + RIGHT * 0.65, end=UP * 1.4 + LEFT * 0.65)
regiones = crearRegiones()
centralRegion = regiones[0]
nRegion = regiones[1]
pRegion = regiones[2]
centralRegion.stretch_to_fit_width(3)
nRegion.stretch_to_fit_width(1.5).move_to(RIGHT * 2.25 + UP * 2)
pRegion.stretch_to_fit_width(1.5).move_to(LEFT * 2.25 + UP * 2)
protonUno.move_to(UP * 2.75 + RIGHT * 1.2)
protonDos.move_to(UP * 2.0 + RIGHT * 1.2)
protonTres.move_to(UP * 1.25 + RIGHT * 1.2)
electronUno.move_to(UP * 2.75 + LEFT * 1.2)
electronDos.move_to(UP * 2.0 + LEFT * 1.2)
electronTres.move_to(UP * 1.25 + LEFT * 1.2)
primeraFlecha.put_start_and_end_on(UP * 2.75 + RIGHT * 0.9, UP * 2.75 + LEFT * 0.9)
segundaFlecha.put_start_and_end_on(UP * 2.0 + RIGHT * 0.9, UP * 2.0 + LEFT * 0.9)
terceraFlecha.put_start_and_end_on(UP * 1.25 + RIGHT * 0.9, UP * 1.25 + LEFT * 0.9)
textRegion = Text("Region de agotamiento", font_size=32)
llave = Brace(centralRegion, direction=DOWN)
electronUnoInteraccion = helperParaRegions(UP * 2.375 + LEFT * 0.1, 0.1)
lineaUnoInteraccion = Line(
    color=colors["colorPurple"],
    start=RIGHT * 0.1 + UP * 2.375,
    end=RIGHT * 0.35 + UP * 2.375,
)
electronDosInteraccion = helperParaRegions(UP * 1.625 + LEFT * 0.1, 0.1)
lineaDosInteraccion = Line(
    color=colors["colorPurple"],
    start=RIGHT * 0.1 + UP * 1.625,
    end=RIGHT * 0.35 + UP * 1.625,
)
hazDeLuzIzq = crearHazDeLuz(
    x_top=0,  # posición horizontal
    y_top=4,  # donde empieza (arriba)
    ancho_top=0.75,  # ancho de arriba (pequeño)
    ancho_bot=1.5,  # ancho de abajo (grande)
    altura=1,
).move_to(LEFT * 2.25 + UP * 3.5)
hazDeLuzDer = crearHazDeLuz(
    x_top=0,  # posición horizontal
    y_top=4,  # donde empieza (arriba)
    ancho_top=0.75,  # ancho de arriba (pequeño)
    ancho_bot=1.5,  # ancho de abajo (grande)
    altura=1,
).move_to(RIGHT * 2.25 + UP * 3.5)


def escenaFotoCorrienteDos(self):
    self.play(actions["fadeIn"](corrienteUno, shift=LEFT * 0.5))
    self.play(actions["fadeIn"](corrienteDos, shift=DOWN * 0.5))
    self.play(actions["fadeIn"](corrienteTres, shift=DOWN * 0.5))
    self.play(actions["fadeIn"](corrienteCuatro, shift=RIGHT * 0.5))
    self.play(actions["fadeIn"](corrienteCinco, shift=RIGHT * 0.5))
    self.play(actions["fadeIn"](corrienteSeis, shift=RIGHT * 0.5))
    self.play(actions["fadeIn"](corrienteSiete, shift=RIGHT * 0.5))
    self.play(actions["fadeIn"](corrienteOcho, shift=UP * 0.5))
    self.play(actions["fadeIn"](corrienteNueve, shift=UP * 0.5))
    self.play(actions["fadeIn"](corrienteDiez, shift=LEFT * 0.5))
    self.wait(0.5)
    self.play(
        actions["fadeOut"](
            corrienteUno,
            corrienteDos,
            corrienteTres,
            corrienteCuatro,
            corrienteCinco,
            corrienteSeis,
            corrienteSiete,
            corrienteOcho,
            corrienteNueve,
            corrienteDiez,
            self.hazDeLuz,
        )
    )
    self.wait(0.5)
    self.play(actions["fadeIn"](hazDeLuzIzq, hazDeLuzDer))
    self.wait(5)
