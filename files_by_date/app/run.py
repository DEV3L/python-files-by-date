from files_by_date.parsers.command_line_argument_parser import CommandLineArgumentParser


def run(*, args=None):
    command_line_argument_parser = CommandLineArgumentParser()
    arguments = command_line_argument_parser.parse(args=args)

    print(f'Copying files within {arguments.input_dir} to {arguments.target_dir} in YYYYMM formatted subdirectories')
