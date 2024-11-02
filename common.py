"""
Common functions.
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

this_filepath = Path(__file__).parent.resolve()


def load_font():
    """
    Load the font from local folders..
    """
    for font in font_manager.findSystemFonts(str(this_filepath / "fonts")):
        font_manager.fontManager.addfont(font)


# Define high-contrast colors that work well on black background
colors = {
    "Sviluppo sostenibile": "#00ff00",  # green
    "Metà strada": "#00ffff",  # cyan
    "Rivalità regionali": "#ff00ff",  # magenta
    # "Diseguaglianza": "#ff8c00",  # orange
    "Diseguaglianza": "#ffdf91",  # orange
    # "Sviluppo basato sui combustibili fossili": "#ff0000",  # red
    "Sviluppo basato sui combustibili fossili": "#ff9191",  # red
    "Storico": "#ffffff",  # white
}


def set_plot_style():
    """
    Set the plot style.
    """
    plt.rcParams.update(
        {
            "figure.dpi": 300,
            "font.family": "Helvetica",
            "figure.facecolor": "black",
            "axes.facecolor": "black",
            "axes.edgecolor": "white",
            "axes.labelcolor": "white",
            "axes.titlecolor": "white",
            "xtick.color": "white",
            "ytick.color": "white",
            "text.color": "white",
            "grid.color": "#404040",
            "savefig.facecolor": "black",
            "axes.titlesize": 16,
        }
    )
