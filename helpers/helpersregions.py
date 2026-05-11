from manim import LEFT, UP, VGroup, RIGHT, Arrow, DOWN
from utils.figures import figures
from utils.objetos import helperParaRegions
from utils.colors import colors

helperUnoIzq = VGroup(helperParaRegions(UP * 2.80 + LEFT * 2.75, 0.1225))
helperDosIzq = VGroup(helperParaRegions(UP * 2.40 + LEFT * 2.75, 0.1225))
helperTresIzq = VGroup(helperParaRegions(UP * 2 + LEFT * 2.75, 0.1225))
helperCuatroIzq = VGroup(helperParaRegions(UP * 1.6 + LEFT * 2.75, 0.1225))
helperCincoIzq = VGroup(helperParaRegions(UP * 1.2 + LEFT * 2.75, 0.1225))
helperSeisIzq = VGroup(helperParaRegions(UP * 2.8 + LEFT * 2.35, 0.1225))
helperSieteIzq = VGroup(helperParaRegions(UP * 2.8 + LEFT * 1.95, 0.1225))
helperOchoIzq = VGroup(helperParaRegions(UP * 2 + LEFT * 2.35, 0.1225))
helperNueveIzq = VGroup(helperParaRegions(UP * 1.2 + LEFT * 2.35, 0.1225))
helperDiezIzq = VGroup(helperParaRegions(UP * 1.2 + LEFT * 1.95, 0.1225))
helperLineaUnoIzq = figures["line"](
    start=LEFT * 2.5 + UP * 2.4, end=UP * 2.4 + LEFT * 2.25, color=colors["colorPurple"]
)
helperLineaDosIzq = figures["line"](
    start=LEFT * 2.5 + UP * 1.6, end=UP * 1.6 + LEFT * 2.25, color=colors["colorPurple"]
)


helperUnoDer = VGroup(helperParaRegions(UP * 2.40 + RIGHT * 2.35, 0.1225))
helperDosDer = VGroup(helperParaRegions(UP * 1.6 + RIGHT * 2.35, 0.1225))
helperLineaUnoDer = figures["line"](
    start=RIGHT * 2.90 + UP * 2.8,
    end=UP * 2.8 + RIGHT * 2.60,
    color=colors["colorPurple"],
)
helperLineaDosDer = figures["line"](
    start=RIGHT * 2.90 + UP * 2.4,
    end=UP * 2.4 + RIGHT * 2.60,
    color=colors["colorPurple"],
)
helperLineaTresDer = figures["line"](
    start=RIGHT * 2.90 + UP * 2, end=UP * 2 + RIGHT * 2.60, color=colors["colorPurple"]
)
helperLineaCuatroDer = figures["line"](
    start=RIGHT * 2.90 + UP * 1.6,
    end=UP * 1.6 + RIGHT * 2.60,
    color=colors["colorPurple"],
)
helperLineaCincoDer = figures["line"](
    start=RIGHT * 2.90 + UP * 1.2,
    end=UP * 1.2 + RIGHT * 2.60,
    color=colors["colorPurple"],
)
helperLineaSeisDer = figures["line"](
    start=RIGHT * 2.50 + UP * 2.8,
    end=UP * 2.8 + RIGHT * 2.20,
    color=colors["colorPurple"],
)
helperLineaSieteDer = figures["line"](
    start=RIGHT * 2.50 + UP * 2,
    end=UP * 2 + RIGHT * 2.20,
    color=colors["colorPurple"],
)
helperLineaOchoDer = figures["line"](
    start=RIGHT * 2.50 + UP * 1.2,
    end=UP * 1.2 + RIGHT * 2.20,
    color=colors["colorPurple"],
)
helperLineaNueveDer = figures["line"](
    start=RIGHT * 2.10 + UP * 2.8,
    end=UP * 2.8 + RIGHT * 1.80,
    color=colors["colorPurple"],
)
helperLineaDiezDer = figures["line"](
    start=RIGHT * 2.10 + UP * 1.2,
    end=UP * 1.2 + RIGHT * 1.80,
    color=colors["colorPurple"],
)
corrienteUno = Arrow(
    start=LEFT * 3.2 + UP * 2,
    end=LEFT * 3.8 + UP * 2,
    stroke_width=128,
    buff=0,
    color=colors["colorOrange"],
)
corrienteDos = Arrow(
    start=LEFT * 4 + UP * 1.50,
    end=LEFT * 4 + UP * 0.25,
    stroke_width=128,
    buff=0,
    color=colors["colorOrange"],
)
corrienteTres = Arrow(
    start=LEFT * 4 + DOWN * 0.25,
    end=LEFT * 4 + DOWN * 1.50,
    stroke_width=128,
    buff=0,
    color=colors["colorOrange"],
)
corrienteCuatro = Arrow(
    start=LEFT * 3.75 + DOWN * 2,
    end=LEFT * 2.5 + DOWN * 2,
    stroke_width=128,
    buff=0,
    color=colors["colorOrange"],
)
corrienteCinco = Arrow(
    start=LEFT * 2 + DOWN * 2,
    end=LEFT * 0.75 + DOWN * 2,
    stroke_width=128,
    buff=0,
    color=colors["colorOrange"],
)
corrienteSeis = Arrow(
    start=RIGHT * 0.75 + DOWN * 2,
    end=RIGHT * 2 + DOWN * 2,
    stroke_width=128,
    buff=0,
    color=colors["colorOrange"],
)
corrienteSiete = Arrow(
    start=RIGHT * 2.5 + DOWN * 2,
    end=RIGHT * 3.75 + DOWN * 2,
    stroke_width=128,
    buff=0,
    color=colors["colorOrange"],
)
corrienteOcho = Arrow(
    start=RIGHT * 4 + DOWN * 1.5,
    end=RIGHT * 4 + DOWN * 0.25,
    stroke_width=128,
    buff=0,
    color=colors["colorOrange"],
)
corrienteNueve = Arrow(
    start=RIGHT * 4 + UP * 0.25,
    end=RIGHT * 4 + UP * 1.50,
    stroke_width=128,
    buff=0,
    color=colors["colorOrange"],
)
corrienteDiez = Arrow(
    start=RIGHT * 3.8 + UP * 2,
    end=RIGHT * 3.2 + UP * 2,
    stroke_width=128,
    buff=0,
    color=colors["colorOrange"],
)
