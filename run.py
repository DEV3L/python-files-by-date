from files_by_date.parsers.command_line_argument_parser import CommandLineArgumentParser


def run():
    command_line_argument_parser = CommandLineArgumentParser()
    arguments = command_line_argument_parser.parse()
    print(arguments.source)
    print(arguments.target)
    pass

if __name__ == "__main__":
    run()
