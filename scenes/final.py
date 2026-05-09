from manim import DOWN, Text, UP, BOLD
from utils.colors import colors
from utils.actions import actions


def final(self):
    # Mensaje final
    final = Text(
        "A mayor frecuencia → mayor energía cinética del electrón",
        font_size=23,
        color=colors["colorWhite"],
    )
    final.to_edge(DOWN, buff=0.3)
    self.play(actions["write"](final))
    self.wait(2.5)

    self.play(*[actions["fadeOut"](m) for m in self.mobjects])

    # Pantalla final
    fin = Text(
        "Efecto Fotoeléctrico", font_size=48, color=colors["colorYellow"], weight=BOLD
    )
    sub = Text("E = hf − φ", font_size=36, color=colors["colorWhite"])
    sub.next_to(fin, DOWN, buff=0.4)
    self.play(actions["write"](fin), actions["fadeIn"](sub, shift=UP * 0.3))
    self.wait(2)
