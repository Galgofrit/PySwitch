#!/usr/bin/env python3
from pyswitch.hardware.devices.pa_midicaptain_mini_6 import *
from pyswitch.clients.local.actions.pager import PagerAction
from pyswitch.clients.local.actions.custom import CUSTOM_MESSAGE
from pyswitch.colors import Colors
from display import DISPLAY_STATUS

pager = PagerAction(
    pages = [
        {
            "id": "clean",
            "text": "CLEAN",
            #  "color": (255, 255, 255),         # background
            "color": Colors.BLUE,
            "textColor": Colors.WHITE            # text
        },
        {
            "id": "rhythm",
            "text": "RHYTHM",
            "color": Colors.ORANGE,
            "textColor": Colors.BLACK
        },
        {
            "id": "lead",
            "text": "LEAD",
            "color": Colors.RED,
            "textColor": Colors.WHITE
        }
    ],
    select_page = "clean",
    display = DISPLAY_STATUS
)

Inputs = [
    # Switch A: main pager (cycles through all)
    {
        "assignment": PA_MIDICAPTAIN_MINI_SWITCH_A,
        "actions": [
            pager,

            # Nobles MS-4: PC #0 → channel 10 - 5150ii - select clean channel
            CUSTOM_MESSAGE(
                message=[201, 0],
                id="clean",
                enable_callback=pager.enable_callback
            ),

            # CBA Preamp MkII: CC#102 val 0 → channel 1
            CUSTOM_MESSAGE(
                message=[176, 102, 0],
                id="clean",
                enable_callback=pager.enable_callback
            ),

            # OneControl: Loop 1 off (val 10) → channel 2
            CUSTOM_MESSAGE(
                message=[193, 10],
                id="clean",
                enable_callback=pager.enable_callback
            ),

            # OneControl: Loop 2 off (val 20) → channel 2
            CUSTOM_MESSAGE(
                message=[193, 20],
                id="clean",
                enable_callback=pager.enable_callback
            )
        ]
    },

    # Switch B: direct to rhythm
    {
        "assignment": PA_MIDICAPTAIN_MINI_SWITCH_B,
        "actions": [
            pager.proxy("rhythm"),

            # Nobles MS-4: PC #1 → channel 10 - 5150ii - select lead channel
            CUSTOM_MESSAGE(
                message=[201, 1],
                id="rhythm",
                enable_callback=pager.enable_callback
            ),

            # CBA Preamp MkII: CC#102 val 127 → channel 1
            CUSTOM_MESSAGE(
                message=[176, 102, 127],
                id="rhythm",
                enable_callback=pager.enable_callback
            ),

            # OneControl: Loop 1 on (val 11) → channel 2
            CUSTOM_MESSAGE(
                message=[193, 11],
                id="rhythm",
                enable_callback=pager.enable_callback
            ),

            # OneControl: Loop 2 off (val 20) → channel 2
            CUSTOM_MESSAGE(
                message=[193, 20],
                id="rhythm",
                enable_callback=pager.enable_callback
            )
        ]
    },

    # Switch C: direct to lead
    {
        "assignment": PA_MIDICAPTAIN_MINI_SWITCH_C,
        "actions": [
            pager.proxy("lead"),

            # Nobles MS-4: PC #2 → channel 10 - 5150ii - select lead channel
            CUSTOM_MESSAGE(
                message=[201, 2],
                id="lead",
                enable_callback=pager.enable_callback
            ),

            # CBA Preamp MkII: CC#102 val 127 → channel 1
            CUSTOM_MESSAGE(
                message=[176, 102, 127],
                id="lead",
                enable_callback=pager.enable_callback
            ),

            # OneControl: Loop 1 on (val 11) → channel 2
            CUSTOM_MESSAGE(
                message=[193, 11],
                id="lead",
                enable_callback=pager.enable_callback
            ),

            # OneControl: Loop 2 on (val 21) → channel 2
            CUSTOM_MESSAGE(
                message=[193, 21],
                id="lead",
                enable_callback=pager.enable_callback
            )
        ]
    }
]
