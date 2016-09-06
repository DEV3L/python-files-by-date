
def execute():
    from src.parse_args import FilesByDateArgumentParser
    files_by_date_argument_parser = FilesByDateArgumentParser()
    arguments = files_by_date_argument_parser.parse()
    files_by_date_argument_parser.help()

#
#
# def print_hello_world():
#     print(get_message())
#
#
#     from os import walk
#
#     f = []
#     for (dirpath, dirnames, filenames) in walk("."):
#         f.extend(filenames)
#         break
#
#     print(f)

if __name__ == "__main__":
    print("in main")
    execute()
