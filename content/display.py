#!/usr/bin/env python3
from micropython import const
from pyswitch.colors import DEFAULT_LABEL_COLOR
from pyswitch.ui.ui import DisplayElement, DisplayBounds
from pyswitch.ui.elements import DisplayLabel
from pyswitch.clients.kemper import TunerDisplayCallback

_DISPLAY_WIDTH = const(240)
_DISPLAY_HEIGHT = const(240)

# Larger font and full height centered text
_CENTER_LABEL_LAYOUT = {
    "font": "/fonts/PTSans-NarrowBold-40.pcf",
    "backColor": DEFAULT_LABEL_COLOR,
    "textColor": (255, 255, 255),
    "stroke": 1
}

DISPLAY_STATUS = DisplayLabel(
    layout=_CENTER_LABEL_LAYOUT,
    bounds=DisplayBounds(
        x=0,
        y=80,  # Adjusted for vertical center
        w=_DISPLAY_WIDTH,
        h=80
    )
)

Splashes = TunerDisplayCallback(
    splash_default=DisplayElement(
        bounds=DisplayBounds(
            x=0,
            y=0,
            w=_DISPLAY_WIDTH,
            h=_DISPLAY_HEIGHT
        ),
        children=[
            DISPLAY_STATUS
        ]
    )
)
