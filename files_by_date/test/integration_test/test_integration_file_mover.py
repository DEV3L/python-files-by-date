from files_by_date.service.file_mover import FileMover


def test_validate_input_dir():
    files = FileMover.gather_files('./resources', list())
    print(files)
