import argparse


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("type")
    parser.add_argument("--name")
    return parser.parse_args()
