from files_by_date.service.files_service import FilesService
from files_by_date.test.integration_test import RESOURCES_INPUT_DIR, RESOURCES_OUTPUT_DIR


def test_gather_files():
    files = FilesService.gather_files(RESOURCES_INPUT_DIR, list())
    assert len(files) == 4


def test_group_files_by_modified_date():
    files = FilesService.gather_files(RESOURCES_INPUT_DIR, list())
    grouped_files = FilesService.group_files_by_modified_date(files)
    print(grouped_files)
    # need better tests


def test_copy_files():
    files = FilesService.gather_files(RESOURCES_INPUT_DIR, list())
    grouped_files = FilesService.group_files_by_modified_date(files)
    FilesService.copy_files(grouped_files, RESOURCES_OUTPUT_DIR, False)
    FilesService.copy_files(grouped_files, RESOURCES_OUTPUT_DIR, True)
    # need better tests