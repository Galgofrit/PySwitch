#!/usr/bin/env python3
from pyswitch.clients.local.actions.custom import CUSTOM_MESSAGE
from pyswitch.hardware.devices.pa_midicaptain_mini_6 import *
from display import DISPLAY_STATUS

Inputs = [
    # Clean
    {
        "assignment": PA_MIDICAPTAIN_MINI_SWITCH_A,
        "actions": [
            # MS-4: PC #0 → channel 3 + screen update
            CUSTOM_MESSAGE(
                message = [194, 0],
                display = DISPLAY_STATUS,
                text = "CLEAN",
                color = (255, 255, 255)
            ),

            # CBA Preamp MkII: CC#102 val 0 → channel 1
            CUSTOM_MESSAGE(message = [176, 102, 0]),

            # OneControl: Loop 1 off (PC#10), Loop 2 off (PC#20) → channel 2
            CUSTOM_MESSAGE(message = [193, 10]),
            CUSTOM_MESSAGE(message = [193, 20]),
        ],
    },

    # Rhythm
    {
        "assignment": PA_MIDICAPTAIN_MINI_SWITCH_B,
        "actions": [
            # MS-4: PC #1 → channel 3 + screen update
            CUSTOM_MESSAGE(
                message = [194, 1],
                display = DISPLAY_STATUS,
                text = "RHYTHM",
                color = (255, 140, 0)
            ),

            # CBA Preamp MkII: CC#102 val 127 → channel 1
            CUSTOM_MESSAGE(message = [176, 102, 127]),

            # OneControl: Loop 1 on (PC#11), Loop 2 off (PC#20) → channel 2
            CUSTOM_MESSAGE(message = [193, 11]),
            CUSTOM_MESSAGE(message = [193, 20]),
        ],
    },

    # Lead
    {
        "assignment": PA_MIDICAPTAIN_MINI_SWITCH_C,
        "actions": [
            # MS-4: PC #2 → channel 3 + screen update
            CUSTOM_MESSAGE(
                message = [194, 2],
                display = DISPLAY_STATUS,
                text = "LEAD",
                color = (255, 60, 60)
            ),

            # CBA Preamp MkII: CC#102 val 127 → channel 1
            CUSTOM_MESSAGE(message = [176, 102, 127]),

            # OneControl: Loop 1 on (PC#11), Loop 2 on (PC#21) → channel 2
            CUSTOM_MESSAGE(message = [193, 11]),
            CUSTOM_MESSAGE(message = [193, 21]),
        ],
    }
]
