from manim import Text, LEFT, UP, ORIGIN, DOWN, RIGHT, Arrow, GrowArrow
from utils.actions import actions
from utils.colors import colors
from utils.objetos import crearElectron,crearFoton


def luzAltaFrecuencia(self):
    self.play(
        actions["transform"](
            self.titulo_base,
            Text(
                "Luz de alta frecuencia → electrón liberado",
                font_size=28,
                color=colors["colorGreenB"],
            ).to_edge(UP, buff=0.4),
        )
    )

    freq_label = Text("f  ≥  f₀", font_size=26, color=colors["colorGreenB"])
    freq_label.to_edge(LEFT, buff=0.5).shift(UP * 0.8)
    self.play(actions["write"](freq_label))

    # Tres fotones de alta frecuencia (violeta) → cada uno libera un electrón
    impactos = [
        (LEFT * 3, LEFT * 3 + DOWN * 2.2),
        (ORIGIN, ORIGIN + DOWN * 2.1),
        (RIGHT * 3, RIGHT * 3 + DOWN * 2.2),
    ]

    electrones_libres = []
    for start_x, e_pos in impactos:
        foton = crearFoton(UP*4)
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
        e_libre = crearElectron(e_pos,0.2)
        self.play(actions["fadeOut"](e_libre, scale=0.5))
        flecha = Arrow(
            e_pos, e_pos + UP * 1.8 + start_x * 0.1, color=colors["colorYellow"], buff=0
        )
        self.play(GrowArrow(flecha), e_libre.animate.shift(UP * 1.8), run_time=0.6)
        electrones_libres.extend([e_libre, flecha])

    self.wait(0.8)
    self.play(
        *[actions["fadeOut"](m) for m in electrones_libres],
        actions["fadeOut"](freq_label),
    )
