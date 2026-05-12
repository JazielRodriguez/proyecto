from manim import Scene
from scenes.escenatitulo import titulo
from scenes.escenametalelectrones import metalElectrones
from scenes.luzbajafrecuancia import luzBajaFrecuencia
from scenes.luzaltafrecuencia import luzAltaFrecuencia
from scenes.ecuacion import ecuacion
from scenes.grafica import grafica
from scenes.final import final
from scenes.escenafotodiodo import escenaFotodiodo
from scenes.comparacionled import escenaComparacionLed
from scenes.corrienteoscura import escenaCorrienteOscura
from scenes.regions import escenaRegiones
from scenes.fotocorriente import escenaFotoCorriente
from scenes.fotocorrientedos import escenaFotoCorrienteDos


class EfectoFotoelectrico(Scene):
    def construct(self):
        self.camara_config()
        self.escenas()
        # self.testEscenas()

    def camara_config(self):
        self.camera.background_color = "#0f0f1a"

    def escenas(self):
        titulo(self)
        metalElectrones(self)
        luzBajaFrecuencia(self)
        luzAltaFrecuencia(self)
        grafica(self)
        ecuacion(self)
        escenaFotodiodo(self)
        escenaComparacionLed(self)
        escenaRegiones(self)
        escenaCorrienteOscura(self)
        escenaFotoCorriente(self)
        escenaFotoCorrienteDos(self)
        final(self)

    # def testEscenas(self):
