from manim import Text, LEFT, UP, ORIGIN, DOWN, RIGHT, Arrow, GrowArrow
from utils.actions import actions
from utils.colors import colors
from utils.objetos import crearElectron, crearFoton


def luzAltaFrecuencia(self):
    self.play(actions["fadeOut"](self.nota))
    textoAltaFrecuencia = Text(
        "Luz incidente de alta frecuencia",
        font_size=28,
        color=colors["colorGreen"],
    )
    textoAltaFrecuencia.to_edge(UP, buff=0.4)

    freq_label = Text(
        "f  <  f₀   (frecuencia mayor a la frecuencia umbral)",
        font_size=24,
        color=colors["colorGreenB"],
    )
    freq_label.move_to(UP * 3)
    self.wait(0.25)
    self.play(
        actions["write"](textoAltaFrecuencia),
        actions["write"](freq_label),
        run_time=1.5,
    )
    self.wait(0.5)
    self.play(actions["fadeOut"](textoAltaFrecuencia, freq_label))
    self.wait(0.5)

    # Tres fotones de alta frecuencia (violeta) → cada uno libera un electrón
    impactos = [
        (LEFT * 3, LEFT * 3 + DOWN * 2.2),
        (ORIGIN, ORIGIN + DOWN * 2.1),
        (RIGHT * 3, RIGHT * 3 + DOWN * 2.2),
    ]

    electrones_libres = []
    for i,(start_x, e_pos) in enumerate(impactos):
        foton = crearFoton(UP * 4)
        foton.move_to(UP * 3 + start_x)

        self.play(foton.animate.move_to(e_pos + UP * 0.5), run_time=0.6)

        # Flash de impacto
        flash = actions["flash"](
            e_pos + UP * 0.3,
            color=colors["colorYellow"],
            flash_radius=0.4,
            line_length=0.2,
        )
        self.play(flash, actions["fadeOut"](foton))

        # Electrón sale disparado
        e_libre = crearElectron(e_pos, 0.2)
        self.play(actions["fadeOut"](e_libre, scale=0.5))
        # flecha = Arrow(
        #     e_pos, e_pos + UP * 1.8 + start_x * 0.1, color=colors["colorYellow"], buff=0
        # )
        self.play(e_libre.animate.shift(UP * 7),actions["fadeOut"](self.electrones_impares[i]))
        # electrones_libres.extend([e_libre, flecha])

    self.wait(0.8)
    self.play(
        *[actions["fadeOut"](m) for m in electrones_libres],
        actions["fadeOut"](freq_label),
    )
