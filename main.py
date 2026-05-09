from manim import Scene
from utils.objetos import crearElectron, superficie, crearFoton
from scenes.escenatitulo import titulo
from scenes.escenametalelectrones import metalElectrones
from scenes.luzbajafrecuancia import luzBajaFrecuencia
from scenes.luzaltafrecuencia import luzAltaFrecuencia
from scenes.ecuacion import ecuacion
from scenes.grafica import grafica
from scenes.final import final


class EfectoFotoelectrico(Scene):
    def construct(self):
        self.camara_config()
        self.escenas()

    def camara_config(self):
        self.camera.background_color = "#0f0f1a"

    def objetos():
        superficie()
        crearElectron()
        crearFoton()

    def escenas(self):

        titulo(self)
        metalElectrones(self)
        luzBajaFrecuencia(self)
        luzAltaFrecuencia(self)
        ecuacion(self)
        grafica(self)
        final(self)
