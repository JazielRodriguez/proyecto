from manim import (
    Rectangle,
    Polygon,
    WHITE,
    DashedLine,
    Arrow,
    Text,
    UP,
    VGroup,
    Dot,
    YELLOW,
    PINK,
    FadeIn,
    DOWN,
    Line,
    LEFT,
)


def escenaCorrienteOscura(self):
    # --- Límites de regiones ---
    x_izq = -4
    x_p_dep = -1.8
    x_dep_n = 1.8
    x_der = 4

    # --- Niveles de banda ---
    cond_p_y_top, cond_p_y_bot = 1.6, 0.6
    vale_p_y_top, vale_p_y_bot = -0.1, -1.1

    offset = -1.4
    cond_n_y_top = cond_p_y_top + offset
    cond_n_y_bot = cond_p_y_bot + offset
    vale_n_y_top = vale_p_y_top + offset
    vale_n_y_bot = vale_p_y_bot + offset

    banda_color = "#4a5a8a"

    def banda(x1, y_bot, x2, y_top):
        return Rectangle(
            width=x2 - x1,
            height=y_top - y_bot,
            fill_color=banda_color,
            fill_opacity=0.7,
            stroke_color=banda_color,
            stroke_width=1,
        ).move_to([(x1 + x2) / 2, (y_top + y_bot) / 2, 0])

    cond_p = banda(x_izq, cond_p_y_bot, x_p_dep, cond_p_y_top)
    vale_p = banda(x_izq, vale_p_y_bot, x_p_dep, vale_p_y_top)
    cond_n = banda(x_dep_n, cond_n_y_bot, x_der, cond_n_y_top)
    vale_n = banda(x_dep_n, vale_n_y_bot, x_der, vale_n_y_top)

    cond_dep = Polygon(
        [x_p_dep, cond_p_y_bot, 0],
        [x_p_dep, cond_p_y_top, 0],
        [x_dep_n, cond_n_y_top, 0],
        [x_dep_n, cond_n_y_bot, 0],
        fill_color=banda_color,
        fill_opacity=0.7,
        stroke_color=banda_color,
        stroke_width=1,
    )
    vale_dep = Polygon(
        [x_p_dep, vale_p_y_bot, 0],
        [x_p_dep, vale_p_y_top, 0],
        [x_dep_n, vale_n_y_top, 0],
        [x_dep_n, vale_n_y_bot, 0],
        fill_color=banda_color,
        fill_opacity=0.7,
        stroke_color=banda_color,
        stroke_width=1,
    )

    linea1 = DashedLine(
        start=[x_p_dep, -2.5, 0],
        end=[x_p_dep, 2.5, 0],
        color=WHITE,
        dash_length=0.15,
        stroke_width=1.5,
    )
    linea2 = DashedLine(
        start=[x_dep_n, -2.5, 0],
        end=[x_dep_n, 2.5, 0],
        color=WHITE,
        dash_length=0.15,
        stroke_width=1.5,
    )

    eje_y = Arrow(start=[-4, -2.5, 0], end=[-4, 2.5, 0], color=WHITE, buff=0)
    label_energy = Text("Energy", font_size=28, color=WHITE).next_to(
        eje_y, UP, buff=0.1
    )
    label_cero = Text("0", font_size=24, color=WHITE).next_to(eje_y, DOWN, buff=0.1)

    label_cond = Text("Conduction\nBand", font_size=22, color=WHITE).move_to(
        LEFT * 5 + UP * 1.1,
    )
    label_vale = Text("Valence\nBand", font_size=22, color=WHITE).move_to(
        LEFT * 5 + DOWN * 0.6
    )

    label_p = Text("P Region", font_size=24, color=WHITE).move_to(
        [(x_izq + x_p_dep) / 2, -3.0, 0]
    )
    label_dep = Text("Depletion Region", font_size=24, color=WHITE).move_to(
        [(x_p_dep + x_dep_n) / 2, -3.0, 0]
    )
    label_n = Text("N Region", font_size=24, color=WHITE).move_to(
        [(x_dep_n + x_der) / 2, -3.0, 0]
    )

    def puntos(posiciones, color):
        return VGroup(
            *[
                Dot(point=pos, radius=0.18, color=color, fill_opacity=1)
                for pos in posiciones
            ]
        )

    def lineas(posiciones, color):
        return VGroup(
            *[
                Line(
                    start=[pos[0] - 0.2, pos[1], 0],
                    end=[pos[0] + 0.2, pos[1], 0],
                    color=color,
                    stroke_width=8,
                )
                for pos in posiciones
            ]
        )

    huecos_cond_p = lineas(
        [
            [-3.3, 1.2, 0],
            [-3.6, 0.8, 0],
            [-2.8, 1, 0],
        ],
        PINK,
    )
    electrones_vale_p = puntos(
        [
            [-3.3, -0.5, 0],
            [-3.6, -0.8, 0],
            [-2.8, -0.4, 0],
        ],
        YELLOW,
    )
    huecos_cond_n = lineas([[2.4, 0, 0], [2.9, -0.5, 0], [3.4, -0.2, 0]], PINK)
    electrones_vale_n = puntos([[2.4, -2, 0], [2.9, -1.8, 0], [3.4, -2, 0]], YELLOW)

    todo = VGroup(
        cond_p,
        vale_p,
        cond_dep,
        vale_dep,
        cond_n,
        vale_n,
        linea1,
        linea2,
        eje_y,
        label_energy,
        label_cero,
        label_cond,
        label_vale,
        label_p,
        label_dep,
        label_n,
        huecos_cond_p,
        electrones_vale_p,
        huecos_cond_n,
        electrones_vale_n,
    )

    self.play(FadeIn(todo))
    self.wait(1)
