from manim import Text, UP, MathTex, VGroup, RIGHT, DOWN, BOLD, LEFT
from utils.actions import actions
from utils.colors import colors


def ecuacion(self):
    self.play(
        actions["fadeOut"](self.metal),
        actions["fadeOut"](self.electrones_base),
        actions["fadeOut"](self.titulo_base),
    )

    titulo_ec = Text(
        "Ecuación de Einstein", font_size=36, color=colors["colorYellow"], weight=BOLD
    )
    titulo_ec.to_edge(UP, buff=0.5)
    self.play(actions["write"](titulo_ec))

    # Ecuación principal
    eq = MathTex(r"E_k = h f - \phi", font_size=64, color=colors["colorWhite"])
    eq.move_to(UP * 0.8)
    self.play(actions["write"](eq), run_time=1.5)

    # Leyenda de términos
    terminos = VGroup(
        MathTex(r"E_k", color=colors["colorGreen"]).scale(1.1),
        Text(
            "= Energía cinética del electrón", font_size=22, color=colors["colorGreen"]
        ),
        MathTex(r"h", color=colors["colorBlue"]).scale(1.1),
        Text(
            "= Constante de Planck  (6.626×10⁻³⁴ J·s)",
            font_size=22,
            color=colors["colorBlue"],
        ),
        MathTex(r"f", color=colors["colorPurple"]).scale(1.1),
        Text("= Frecuencia de la luz", font_size=22, color=colors["colorPurple"]),
        MathTex(r"\phi", color=colors["colorOrange"]).scale(1.1),
        Text(
            "= Función de trabajo del metal", font_size=22, color=colors["colorOrange"]
        ),
    )

    filas = VGroup()
    for i in range(0, len(terminos), 2):
        fila = VGroup(terminos[i], terminos[i + 1]).arrange(RIGHT, buff=0.3)
        filas.add(fila)
    filas.arrange(DOWN, buff=0.25, aligned_edge=LEFT)
    filas.next_to(eq, DOWN, buff=0.6)

    self.play(
        actions["laggedStart"](*[actions["write"](f) for f in filas], lag_ratio=0.3),
        run_time=2,
    )
    self.wait(2)
    self.play(
        actions["fadeOut"](titulo_ec), actions["fadeOut"](eq), actions["fadeOut"](filas)
    )
