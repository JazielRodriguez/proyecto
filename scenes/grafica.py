from manim import Text, UP, Axes, MathTex, DOWN, RIGHT, BOLD, Dot, DashedLine, LEFT
from utils.actions import actions
from utils.colors import colors


def grafica(self):
    titulo_g = Text(
        "Energía cinética  vs  Frecuencia",
        font_size=32,
        color=colors["colorYellow"],
        weight=BOLD,
    )
    titulo_g.to_edge(UP, buff=0.4)
    self.play(actions["write"](titulo_g))

    # Ejes
    axes = Axes(
        x_range=[0, 10, 2],
        y_range=[-2, 6, 2],
        x_length=8,
        y_length=5,
        axis_config={
            "color": colors["colorGray"],
            "include_tip": True,
            "tip_length": 0.2,
        },
        x_axis_config={"numbers_to_include": []},
        y_axis_config={"numbers_to_include": []},
    )
    axes.move_to(DOWN * 0.3)

    # Etiquetas de ejes
    x_label = MathTex(
        "f \\ (\\text{frecuencia})", font_size=28, color=colors["colorGrayB"]
    )
    x_label.next_to(axes.x_axis.get_right(), DOWN + RIGHT, buff=0.1)
    y_label = MathTex("E_k", font_size=28, color=colors["colorGreen"])
    y_label.next_to(axes.y_axis.get_top(), LEFT, buff=0.1)

    self.play(
        actions["create"](axes), actions["write"](x_label), actions["write"](y_label)
    )

    # Frecuencia umbral f₀ (x=3.5 en coords de eje)
    f0_x = 3.5
    phi = 1.5  # función de trabajo en unidades de la gráfica

    # Línea punteada en f₀
    f0_line = DashedLine(
        axes.c2p(f0_x, -2),
        axes.c2p(f0_x, 4),
        color=colors["colorOrange"],
        dash_length=0.15,
    )
    f0_label = MathTex("f_0", font_size=26, color=colors["colorOrange"])
    f0_label.next_to(axes.c2p(f0_x, -2), DOWN, buff=0.1)

    # Línea Eₖ = 0 (eje x) ya está, pero marcamos φ en y negativo
    phi_dot = Dot(axes.c2p(0, -phi), color=colors["colorOrange"], radius=0.1)
    phi_label = MathTex(r"-\phi", font_size=26, color=colors["colorOrange"])
    phi_label.next_to(phi_dot, LEFT, buff=0.1)

    self.play(actions["create"](f0_line), actions["write"](f0_label))
    self.play(actions["fadeIn"](phi_dot), actions["write"](phi_label))

    # Recta: Eₖ = h·f - φ  → pendiente positiva desde f₀ hacia arriba
    # Para f < f₀: Eₖ = 0 (no hay emisión, línea plana en 0)
    linea_cero = axes.plot(
        lambda x: 0,
        x_range=[0, f0_x],
        color=colors["colorRedB"],
        stroke_width=3,
    )
    linea_principal = axes.plot(
        lambda x: x - f0_x,  # pendiente h (normalizada a 1)
        x_range=[f0_x, 9.5],
        color=colors["colorGreen"],
        stroke_width=3,
    )

    leyenda_cero = Text("Sin emisión", font_size=20, color=colors["colorRedB"])
    leyenda_cero.move_to(axes.c2p(1.5, 0.6))

    leyenda_lineal = Text("Eₖ = hf − φ", font_size=20, color=colors["colorGreen"])
    leyenda_lineal.move_to(axes.c2p(7.5, 3.5))

    self.play(actions["create"](linea_cero), actions["write"](leyenda_cero))
    self.play(
        actions["create"](linea_principal),
        actions["write"](leyenda_lineal),
        run_time=1.5,
    )

    # Punto de ejemplo para una f alta
    f_ejemplo = 7.5
    ek_ejemplo = f_ejemplo - f0_x
    punto = Dot(
        axes.c2p(f_ejemplo, ek_ejemplo), color=colors["colorYellow"], radius=0.12
    )
    linea_v = DashedLine(
        axes.c2p(f_ejemplo, 0),
        axes.c2p(f_ejemplo, ek_ejemplo),
        color=colors["colorYellow"],
    )
    ek_ann = MathTex("E_k", font_size=22, color=colors["colorYellow"])
    ek_ann.next_to(axes.c2p(f_ejemplo, ek_ejemplo / 2), RIGHT, buff=0.1)

    self.play(
        actions["fadeIn"](punto), actions["create"](linea_v), actions["write"](ek_ann)
    )
    self.wait(2.5)
