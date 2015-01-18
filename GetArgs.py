import argparse


def get_args():

    def parse_command_line():
        parser = argparse.ArgumentParser()
        parser.add_argument("--config", help="Path to configuration file")
        return parser.parse_args()

    args = parse_command_line()
    args_dict = dict()
    args_dict["config"] = args.config
    return args_dict