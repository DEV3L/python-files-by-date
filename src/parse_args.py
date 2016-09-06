class FilesByDateArgumentParser():
    def __init__(self):
        import argparse

        self.argument_parser = argparse.ArgumentParser('files_by_date')
        # self.argument_parser.add_argument("a")

    def parse(self):
        return self.argument_parser.parse_args()

    def help(self):
        self.argument_parser.print_help()