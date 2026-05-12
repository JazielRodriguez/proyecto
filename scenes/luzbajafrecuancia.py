from manim import Text, UP, LEFT, DOWN, BOLD
from utils.actions import actions
from utils.colors import colors
from utils.objetos import crearFoton


def luzBajaFrecuencia(self):
    self.electrones_impares = self.electrones_impares
    textoBajaFrecuencia = Text(
        "Luz incidente de baja frecuencia",
        font_size=28,
        color=colors["colorRedB"],
    )
    textoBajaFrecuencia.to_edge(UP, buff=0.4)
    freq_label = Text(
        "f  <  f₀   (frecuencia menor a la frecuencia umbral)",
        font_size=24,
        color=colors["colorRedB"],
    )
    freq_label.move_to(UP * 3)
    self.wait(0.25)
    self.play(
        actions["write"](textoBajaFrecuencia),
        actions["write"](freq_label),
        run_time=1.5,
    )
    self.wait(0.5)
    self.play(actions["fadeOut"](textoBajaFrecuencia, freq_label))
    self.wait(0.5)
    for _ in range(3):
        foton = crearFoton(UP * 4)
        foton.move_to(UP * 4.5 + LEFT * 2)
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
        "El electrón NO absorbe suficiente energía para salir de la superficie metalica",
        font_size=24,
        weight=BOLD,
        color=colors["colorWhite"],
    )
    self.nota = nota
    nota.next_to(freq_label, DOWN, buff=0.3)
    self.play(actions["write"](nota))
    self.wait(1.2)
