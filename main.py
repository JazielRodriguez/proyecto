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
        self.escena_titulo()
        self.escena_metal_y_electrones()
        self.escena_luz_baja_frecuencia()
        self.escena_luz_alta_frecuencia()
        self.escena_ecuacion()
        self.escena_grafica()

    def camara_config(self):
        self.camera.background_color = "#0f0f1a"

    superficie()
    crearElectron()
    crearFoton()
    titulo()
    metalElectrones()
    luzBajaFrecuencia()
    luzAltaFrecuencia()
    ecuacion()
    grafica()
    final()
