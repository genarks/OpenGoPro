# params.py/Open GoPro, Version 2.0 (C) Copyright 2021 GoPro, Inc. (http://gopro.com/OpenGoPro).
# This copyright was auto-generated on Tue Sep  7 21:35:53 UTC 2021

# pylint: disable=missing-class-docstring

"""Updates to parameter definitions for GoPro BLE and WiFi commands for Open GoPro version 2.0

Note these have to be IntEnum's in order to be correctly built when sending commands
"""

import enum
from open_gopro.api.v1_0.params import ParamsV1_0


class ParamsV2_0(ParamsV1_0):
    class Resolution(enum.IntEnum):
        RES_4K = 1
        RES_2_7K = 4
        RES_2_7K_4_3 = 6
        RES_1080 = 9
        RES_4K_4_3 = 18
        RES_5_K_4_3 = 25
        RES_5_3_K = 100

    class Preset(enum.IntEnum):
        ACTIVITY = 1
        BURST_PHOTO = 65538
        CINEMATIC = 2
        LIVE_BURST = 65537
        NIGHT_PHOTO = 65539
        NIGHT_LAPSE = 131074
        PHOTO = 65536
        SLO_MO = 3
        STANDARD = 0
        TIME_LAPSE = 131073
        TIME_WARP = 131072
        MAX_PHOTO = 262144
        MAX_TIMEWARP = 327680
        MAX_VIDEO = 196608

    class CameraControlStatus(enum.IntEnum):
        IDLE = 1
        CAMERA = 2
        EXTERNAL = 3

    class VideoFOV(enum.IntEnum):
        WIDE = 0
        NARROW = 2
        SUPERVIEW = 3
        LINEAR = 4
        MAX_SUPERVIEW = 7
        LINEAR_HORIZON = 8

    class PhotoFOV(enum.IntEnum):
        WIDE = 101
        LINEAR = 102
        NARROW = 19
        MAX_SUPERVIEW = 100

    class MultishotFOV(enum.IntEnum):
        NARROW = 19
        MAX_SUPERVIEW = 100
        WIDE = 101
