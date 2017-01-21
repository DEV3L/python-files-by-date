import argparse


class CommandLineArgumentParser():
    def __init__(self):
        self.argument_parser = argparse.ArgumentParser('files_by_date')
        self._add_arguments()

    def parse(self):
        return self.argument_parser.parse_args()

    def help(self):
        self.argument_parser.print_help()

    def _add_arguments(self):
        self.argument_parser.add_argument("source_dir", type=str, help="source directory")
        self.argument_parser.add_argument("target_dir", type=str, help="target directory")
