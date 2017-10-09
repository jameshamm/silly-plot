"""Take commands/arguments and
convert/pass them into the appropiate structure"""
import argparse


def initial_args():
    """Deal with the args passed to the program when it begins.
    """
    parser = argparse.ArgumentParser(
        description="Script that plots data in real-time"
    )

    # The required args
    parser.add_argument("--meh", action="store_true")


    args = parser.parse_args()
    # Sanity check on the args passed in

    if args.meh:
        print("I agree")

    return args