import os
import sys
import argparse
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))


def record_options():
    a = argparse.ArgumentParser()

    a.add_argument("--display_volume",
                   help = "Specify if input volume should be displayed.",
                   dest = "display_volume",
                   required=False,
                   default=False,
                   type=bool,
                   nargs=1)

    a.add_argument("--display_predictions",
                   help="Specify if prediction values should be displayed.",
                   dest = "display_prediction",
                   required=False,
                   default=False,
                   type=bool,
                   nargs=1)

    a.add_argument("--play_midi",
                   help="Specify if midi should be sent with python-rt-midi.",
                   dest="play_midi",
                   required=False,
                   default=True,
                   type=bool,
                   nargs=1)

    a.add_argument("--filtered",
                   help="filter out redundant notes).",
                   dest="filtered",
                   required=False,
                   default=False,
                   type=bool,
                   nargs=1)

    return a.parse_args()
