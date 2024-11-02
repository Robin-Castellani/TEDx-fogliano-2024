"""
Common functions.
"""

from pathlib import Path
import matplotlib.font_manager as font_manager

this_filepath = Path(__file__).parent.resolve()


def load_font():
    """
    Load the font from local folders..
    """
    for font in font_manager.findSystemFonts(str(this_filepath / "fonts")):
        font_manager.fontManager.addfont(font)
