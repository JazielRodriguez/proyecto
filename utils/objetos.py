from utils.figures import figures
from utils.colors import colors
from manim import DOWN, VGroup, Text, BOLD


def superficie():
    """Rectángulo que representa la superficie metálica."""
    metal = figures["rectangle"](
        width=10,
        height=1.6,
        color=colors["colorGray"],
        fill_color="#3a3a5c",
        fill_opacity=1,
    )
    metal.move_to(DOWN * 2.5)
    label = Text("Superficie metálica", font_size=22, color=colors["colorGrayB"])
    label.move_to(metal.get_center())
    return VGroup(metal, label)


def crearElectron(pos):
    e = figures["circle"](
        radius=0.18,
        color=colors["colorYellow"],
        fill_color=colors["colorYellow"],
        fill_opacity=1,
    )
    e.move_to(pos)
    minus = Text("e⁻", font_size=14, color=colors["colorBlack"], weight=BOLD)
    minus.move_to(pos)
    return VGroup(e, minus)


def crearFoton(color=colors["colorBlue"]):
    foton = figures["circle"](
        radius=0.2, color=color, fill_color=color, fill_opacity=0.9
    )
    gamma = Text("γ", font_size=18, color=colors["colorWhite"], weight=BOLD)
    gamma.move_to(foton.get_center())
    return VGroup(foton, gamma)
