from .text import joke
from .args import initial_args
from .plot import run_plotter

def run():
    """Start the main script"""
    print("--- Starting ---")
    args = initial_args()

    run_plotter(args)

    print("--- Stopping ---")


if __name__ == "__main__":
    run()