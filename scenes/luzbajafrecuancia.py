from manim import Text, UP, LEFT, DOWN, BOLD
from utils.actions import actions
from utils.colors import colors


def luzBajaFrecuencia(self):
    self.play(
        actions["transform"](
            self.titulo_base,
            Text(
                "Luz de baja frecuencia → sin efecto",
                font_size=28,
                color=colors["colorRedB"],
            ).to_edge(UP, buff=0.4),
        )
    )

    # Etiqueta frecuencia
    freq_label = Text(
        "f  <  f₀   (frecuencia umbral)", font_size=24, color=colors["colorRedB"]
    )
    freq_label.to_edge(LEFT, buff=0.5).shift(UP * 0.8)
    self.play(actions["write"](freq_label))

    # Fotones de color rojo (baja frecuencia) cayendo
    for _ in range(3):
        foton = self.crear_foton(color=colors["colorRed"])
        foton.move_to(UP * 3 + LEFT * 2)
        self.play(
            foton.animate.move_to(DOWN * 1.8 + LEFT * 2),
            run_time=0.7,
            # rate_func=linear,
        )

        # Rebota (no hay emisión)
        rebote = Text("✗", font_size=34, color=colors["colorRed"], weight=BOLD)
        rebote.move_to(DOWN * 1.6 + LEFT * 2)
        self.play(actions["fadeIn"](rebote, scale=1.5), actions["fadeOut"](foton))
        self.play(actions["fadeOut"](rebote))

    nota = Text(
        "El electrón NO absorbe suficiente energía",
        font_size=22,
        color=colors["colorOrange"],
    )
    nota.next_to(freq_label, DOWN, buff=0.3)
    self.play(actions["write"](nota))
    self.wait(1.2)
    self.play(actions["fadeOut"](freq_label), actions["fadeOut"](nota))
