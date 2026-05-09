from manim import BOLD, Text, DOWN, VGroup, UP, RIGHT, LEFT
from utils.actions import actions
from utils.colors import colors
from utils.objetos import crearFotodiodo, crearFoton


def escenaFotodiodo(self):
    titulo = Text(
        "Efecto Fotoeléctrico con Fotodiodo",
        font_size=52,
        color=colors["colorYellow"],
        weight=BOLD,
    )
    fotodiodo = crearFotodiodo()
    positionElectron = UP * 4.5

    fotonUno = VGroup(crearFoton(positionElectron))
    fotonDos = VGroup(crearFoton(positionElectron))
    fotonTres = VGroup(crearFoton(positionElectron))
    entradaDeLuz = Text(
        "Entrada de luz", font_size=32, color=colors["colorYellow"], weight=BOLD
    )
    entradaDeLuz.shift(UP * 3.5 + RIGHT * 2.5)
    anode = Text("Anodo", font_size=32, color=colors["colorYellow"], weight=BOLD)
    cathode = Text("Catodo", font_size=32, color=colors["colorYellow"], weight=BOLD)
    anode.shift(LEFT * 1.75 + UP * 0.5)
    cathode.shift(RIGHT * 1.75 + UP * 0.5)
    corrienteNegativa = Text("-", font_size=24, color=colors["colorBlue"],weight=BOLD)
    corrientePositiva = Text("+", font_size=24, color=colors["colorRed"],weight=BOLD)
    corrienteNegativa.shift(DOWN * 1.75 + LEFT * 0.50)
    corrientePositiva.shift(DOWN * 1.75 + RIGHT * 0.50)

    self.play(actions["write"](titulo), run_time=1.5)
    self.wait(1.5)
    self.play(actions["fadeOut"](titulo))
    self.fotodiodo=fotodiodo
    self.play(actions["fadeIn"](self.fotodiodo))
    self.add(fotonUno)
    self.add(fotonDos)
    self.add(fotonTres)
    self.play(fotonUno.animate.move_to(DOWN * -2.25), actions["write"](entradaDeLuz))
    self.play(
        actions["write"](anode),
        actions["write"](cathode),
        actions["write"](corrientePositiva),
        actions["write"](corrienteNegativa),
    )
    # self.play(actions["write"](entradaDeLuz), run_time=0.75)
    self.wait(0.5)
    self.play(actions["fadeOut"](fotonUno))
    self.play(fotonDos.animate.move_to(DOWN * -2.25))
    self.wait(0.5)
    self.play(actions["fadeOut"](fotonDos))
    self.play(fotonTres.animate.move_to(DOWN * -2.25))
    self.wait(1.5)
