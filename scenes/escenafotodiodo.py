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
    positionEntradaFoton = UP * 4.5

    fotonEntradaUno = VGroup(crearFoton(positionEntradaFoton))
    fotonEntradaDos = VGroup(crearFoton(positionEntradaFoton))
    fotonEntradaTres = VGroup(crearFoton(positionEntradaFoton))

    entradaDeLuz = Text(
        "Entrada de luz", font_size=32, color=colors["colorYellow"], weight=BOLD
    )
    entradaDeLuz.shift(UP * 3.5 + RIGHT * 2.5)
    anode = Text("Anodo", font_size=32, color=colors["colorYellow"], weight=BOLD)
    cathode = Text("Catodo", font_size=32, color=colors["colorYellow"], weight=BOLD)
    anode.shift(LEFT * 1.75 + UP * 0.5)
    cathode.shift(RIGHT * 1.75 + UP * 0.5)
    corrienteNegativa = Text("-", font_size=24, color=colors["colorBlue"], weight=BOLD)
    corrientePositiva = Text("+", font_size=24, color=colors["colorRed"], weight=BOLD)
    corrienteNegativa.shift(DOWN * 1.75 + LEFT * 0.50)
    corrientePositiva.shift(DOWN * 1.75 + RIGHT * 0.50)
    self.play(actions["fadeOut"](*self.mobjects))
    self.wait(0.5)
    self.play(actions["write"](titulo), run_time=1.5)
    self.wait(1.5)
    self.play(actions["fadeOut"](titulo))
    self.fotodiodo = fotodiodo
    self.corrientePositiva = corrientePositiva
    self.corrienteNegativa = corrienteNegativa
    self.entradaDeLuz = entradaDeLuz
    self.anode = anode
    self.cathode = cathode
    self.play(actions["fadeIn"](self.fotodiodo))
    self.add(fotonEntradaUno)
    self.add(fotonEntradaDos)
    self.add(fotonEntradaTres)
    self.play(
        fotonEntradaUno.animate.move_to(DOWN * -2.25), actions["write"](entradaDeLuz)
    )
    self.play(
        actions["write"](anode),
        actions["write"](cathode),
        actions["write"](corrientePositiva),
        actions["write"](corrienteNegativa),
    )
    # self.play(actions["write"](entradaDeLuz), run_time=0.75)
    self.wait(0.5)
    self.play(actions["fadeOut"](fotonEntradaUno))
    self.play(fotonEntradaDos.animate.move_to(DOWN * -2.25))
    self.wait(0.5)
    self.play(actions["fadeOut"](fotonEntradaDos))
    self.play(fotonEntradaTres.animate.move_to(DOWN * -2.25))
    self.wait(1.5)
    self.play(actions["fadeOut"](fotonEntradaTres))
