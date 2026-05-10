from utils.figures import figures
from utils.colors import colors
from manim import DOWN, VGroup, Text, BOLD, UP, LEFT, RIGHT


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


def crearElectron(position,radius):
    electron = figures["circle"](
        radius=radius,
        color=colors["colorYellow"],
        fill_color=colors["colorYellow"],
        fill_opacity=1,
    )
    electron.move_to(position)
    minus = Text("⁻", font_size=18, color=colors["colorBlack"], weight=BOLD)
    minus.move_to(electron.get_center())
    return VGroup(electron, minus)


def crearFoton(positon):
    foton = figures["circle"](
        radius=0.2,
        color=colors["colorWhite"],
        fill_color=colors["colorWhite"],
        fill_opacity=0.9,
    )
    foton.move_to(positon)
    gamma = Text("γ", font_size=18, color=colors["colorBlack"], weight=BOLD)
    gamma.move_to(foton.get_center())
    return VGroup(foton, gamma)


def crearFotodiodo():
    receptorDeLuz = figures["rectangle"](
        width=2.5, height=1, color=colors["colorGray"], stroke_width=16
    )
    receptorDeLuz.set_z_index(5)
    cathode = figures["line"](
        start=RIGHT * 0.75 + UP * 1.8,
        end=RIGHT * 0.75 + DOWN * 0.50,
        color=colors["colorRed"],
        stroke_width=8,
    )
    cathode.set_z_index(1)
    supportCathode = figures["line"](
        start=RIGHT * 0.75 + DOWN * 0.5, end=RIGHT * 1.5 + DOWN * 0.5
    )
    supportCathodeConnector = figures["line"](
        start=RIGHT * 1.5 + DOWN * 0.5, end=RIGHT * 1.5 + DOWN * 2
    )
    anode = figures["line"](
        start=LEFT * 0.75 + UP * 1.8,
        end=LEFT * 0.75 + DOWN * 1,
        color=colors["colorBlue"],
        stroke_width=8,
    )
    anode.set_z_index(1)
    supportAnode = figures["line"](
        start=LEFT * 0.75 + DOWN * 1, end=LEFT * 1.5 + DOWN * 1
    )
    supportAnodeConnector = figures["line"](
        start=LEFT * 1.5 + DOWN * 1, end=LEFT * 1.5 + DOWN * 2
    )
    connectorAnode = figures["line"](
        start=LEFT * 1.5 + DOWN * 2, end=DOWN * 2 + LEFT * 0.30
    )
    connectorCathode = figures["line"](
        start=RIGHT * 1.5 + DOWN * 2, end=DOWN * 2 + RIGHT * 0.30
    )
    padAnode = figures["line"](
        start=LEFT * 0.30 + DOWN * 2.25, end=LEFT * 0.30 + DOWN * 1.75
    )
    padCathode = figures["line"](
        start=RIGHT * 0.30 + DOWN * 2.5, end=RIGHT * 0.30 + DOWN * 1.5
    )

    receptorDeLuz.move_to(UP * 2.3)
    return VGroup(
        padAnode,
        padCathode,
        receptorDeLuz,
        cathode,
        anode,
        supportCathode,
        connectorCathode,
        supportAnode,
        connectorAnode,
        supportCathodeConnector,
        supportAnodeConnector,
    )


def crearLed():
    receptorDeLuz = figures["rectangle"](
        width=2.5, height=1, color=colors["colorGray"], stroke_width=16
    )
    receptorDeLuz.set_z_index(5)
    cathode = figures["line"](
        start=RIGHT * 0.75 + UP * 1.8,
        end=RIGHT * 0.75 + DOWN * 0.50,
        color=colors["colorRed"],
        stroke_width=8,
    )
    cathode.set_z_index(1)
    supportCathode = figures["line"](
        start=RIGHT * 0.75 + DOWN * 0.5, end=RIGHT * 1.5 + DOWN * 0.5
    )
    supportCathodeConnector = figures["line"](
        start=RIGHT * 1.5 + DOWN * 0.5, end=RIGHT * 1.5 + DOWN * 2
    )
    anode = figures["line"](
        start=LEFT * 0.75 + UP * 1.8,
        end=LEFT * 0.75 + DOWN * 1,
        color=colors["colorBlue"],
        stroke_width=8,
    )
    anode.set_z_index(1)
    supportAnode = figures["line"](
        start=LEFT * 0.75 + DOWN * 1, end=LEFT * 1.5 + DOWN * 1
    )
    supportAnodeConnector = figures["line"](
        start=LEFT * 1.5 + DOWN * 1, end=LEFT * 1.5 + DOWN * 2
    )
    connectorAnode = figures["line"](
        start=LEFT * 1.5 + DOWN * 2, end=DOWN * 2 + LEFT * 0.30
    )
    connectorCathode = figures["line"](
        start=RIGHT * 1.5 + DOWN * 2, end=DOWN * 2 + RIGHT * 0.30
    )
    padAnode = figures["line"](
        start=LEFT * 0.30 + DOWN * 2.25, end=LEFT * 0.30 + DOWN * 1.75
    )
    padCathode = figures["line"](
        start=RIGHT * 0.30 + DOWN * 2.5, end=RIGHT * 0.30 + DOWN * 1.5
    )

    receptorDeLuz.move_to(UP * 2.3)
    return VGroup(
        padAnode,
        padCathode,
        receptorDeLuz,
        cathode,
        anode,
        supportCathode,
        connectorCathode,
        supportAnode,
        connectorAnode,
        supportCathodeConnector,
        supportAnodeConnector,
    )


def crearRegiones():
    centralRegion = figures["square"](
        side_length=2,
    )
    nRegion = figures["square"](
        side_length=2,
    )
    pRegion = figures["square"](
        side_length=2,
    )
    connectorPRegion = figures["line"](
        start=LEFT * 3 + UP * 2, end=LEFT * 4 + UP * 2, color=colors["colorBlue"]
    )
    connectorNRegion = figures["line"](
        start=RIGHT * 3 + UP * 2, end=RIGHT * 4 + UP * 2, color=colors["colorRed"]
    )
    connectorLeft = figures["line"](
        start=LEFT * 4 + UP * 2, end=LEFT * 4 + DOWN * 2, color=colors["colorBlue"]
    )
    connectorRight = figures["line"](
        start=RIGHT * 4 + UP * 2, end=RIGHT * 4 + DOWN * 2, color=colors["colorRed"]
    )
    connectorNegative = figures["line"](
        start=LEFT * 4 + DOWN * 2, end=LEFT * 0.5 + DOWN * 2, color=colors["colorBlue"]
    )
    connectorPositive = figures["line"](
        start=RIGHT * 4 + DOWN * 2, end=RIGHT * 0.5 + DOWN * 2, color=colors["colorRed"]
    )
    padNegative = figures["line"](
        start=LEFT * 0.5 + DOWN * 2.5,
        end=LEFT * 0.5 + DOWN * 1.5,
        color=colors["colorBlue"],
    )
    padPositive = figures["line"](
        start=RIGHT * 0.5 + DOWN * 3,
        end=RIGHT * 0.5 + DOWN * 1,
        color=colors["colorRed"],
    )
    centralRegion.move_to(UP * 2)
    nRegion.move_to(UP * 2 + RIGHT * 2)
    pRegion.move_to(UP * 2 + LEFT * 2)
    return VGroup(
        centralRegion,
        nRegion,
        pRegion,
        connectorPRegion,
        connectorNRegion,
        connectorLeft,
        connectorRight,
        connectorNegative,
        connectorPositive,
        padNegative,
        padPositive,
    )


def crearProton(position,radius):
    proton = figures["circle"](
        radius=radius,
        color=colors["colorBlue"],
        fill_color=colors["colorBlue"],
        fill_opacity=0.9,
    )
    proton.move_to(position)
    carga = Text("+", font_size=18, color=colors["colorWhite"], weight=BOLD)
    carga.move_to(proton.get_center())
    return VGroup(proton, carga)


def helperParaRegions(position,radius):
    helper = figures["circle"](
        radius=radius,
        color=colors["colorGreen"],
        fill_color=colors["colorGreen"],
        fill_opacity=1,
    )
    helper.move_to(position)
    return VGroup(helper)
