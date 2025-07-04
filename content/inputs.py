##############################################################################################################################################
#
# Definition of actions for switches
# (Galgo usage of Kemper)
#
##############################################################################################################################################

from pyswitch.hardware.devices.pa_midicaptain_mini_6 import *

from display import DISPLAY_HEADER_1, DISPLAY_HEADER_2, DISPLAY_FOOTER_1, DISPLAY_FOOTER_2

from pyswitch.clients.kemper.actions.bank_up_down import BANK_UP, BANK_DOWN
from pyswitch.clients.kemper.actions.rig_up_down import RIG_UP, RIG_DOWN

from pyswitch.clients.kemper.actions.rig_select import RIG_SELECT, RIG_SELECT_DISPLAY_TARGET_RIG
from pyswitch.clients.kemper.actions.morph import MORPH_DISPLAY

from pyswitch.clients.kemper.actions.rig_volume_boost import RIG_VOLUME_BOOST
from pyswitch.clients.kemper.actions.tuner import TUNER_MODE

# Defines the switch assignments
Inputs = [

    # Switch 1
    {
        "assignment": PA_MIDICAPTAIN_MINI_SWITCH_1,
        "actions": [
            BANK_DOWN(
                display = DISPLAY_HEADER_1
            )
        ]
    },

    # Switch 2
    {
        "assignment": PA_MIDICAPTAIN_MINI_SWITCH_2,
        "actions": [
            BANK_UP(
                display = DISPLAY_HEADER_2
            )
        ]
    },

    # Switch 3
    {
        "assignment": PA_MIDICAPTAIN_MINI_SWITCH_3,
        "actions": [
            TUNER_MODE()
        ]
    },


    # Switch A
    {
        "assignment": PA_MIDICAPTAIN_MINI_SWITCH_A,
        "actions": [
            RIG_SELECT(
                rig = 4,
                display_mode = RIG_SELECT_DISPLAY_TARGET_RIG,
				display = DISPLAY_FOOTER_1
            )
        ],
    },

    # Switch B
    {
        "assignment": PA_MIDICAPTAIN_MINI_SWITCH_B,
        "actions": [
            RIG_SELECT(
                rig = 5,
                display_mode = RIG_SELECT_DISPLAY_TARGET_RIG,
				display = DISPLAY_FOOTER_2
            )
        ],
    },

    # Switch C
    {
        "assignment": PA_MIDICAPTAIN_MINI_SWITCH_C,
        "actions": [
            RIG_VOLUME_BOOST(
                boost_volume = 0.625  # +3dB          # Value im [0..1] representing the Rig Volume Knob. Examples: 0.5 = 0dB (no boost), 0.75 = +6dB, 1.0 = +12dB
            )
        ]
    }

]
