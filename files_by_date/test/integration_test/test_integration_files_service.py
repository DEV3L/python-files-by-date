import datetime
import os
import shutil
from unittest import TestCase

from files_by_date.service.files_service import FilesService
from files_by_date.test.integration_test import RESOURCES_INPUT_DIR


class TestIntegrationFilesService(TestCase):
    # TEST_DIR = f'./{datetime.datetime.now().microsecond}' # 3.6
    TEST_DIR = './{time}'.format(time=datetime.datetime.now().microsecond)

    def setUp(self):
        os.makedirs(TestIntegrationFilesService.TEST_DIR)

    def tearDown(self):
        if os.path.exists(TestIntegrationFilesService.TEST_DIR):
            shutil.rmtree(TestIntegrationFilesService.TEST_DIR)

    def test_gather_files(self):
        files = FilesService.gather_files(RESOURCES_INPUT_DIR, list())
        assert len(files) == 4

    def test_group_files_by_modified_date(self):
        files = FilesService.gather_files(RESOURCES_INPUT_DIR, list())
        grouped_files = FilesService.group_files_by_modified_date(files)
        print(grouped_files)
        # TODO: need better tests

    def test_copy_files(self):
        files = FilesService.gather_files(RESOURCES_INPUT_DIR, list())
        grouped_files = FilesService.group_files_by_modified_date(files)
        FilesService.copy_files(grouped_files, TestIntegrationFilesService.TEST_DIR, False)
        FilesService.copy_files(grouped_files, TestIntegrationFilesService.TEST_DIR, True)
        # TODO: need better tests
