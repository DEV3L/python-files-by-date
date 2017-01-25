import datetime
import os
import time


class FilesService:
    def __init__(self):
        raise NotImplementedError

    @classmethod
    def gather_files(cls, parent_directory, files):
        for dir_name, subdir_list, file_list in os.walk(parent_directory):
            if file_list:
                files.extend(
                    ['{dir_name}{os_sep}{file_name}'.format(dir_name=dir_name, os_sep=os.sep, file_name=file) for file
                     in file_list])
                # [f'{dir_name}{os.sep}{file}' for file in file_list] # 3.6
            for subdir in subdir_list:
                files = cls.gather_files(subdir, files)

        return files

    @classmethod
    def group_files_by_modified_date(cls, files):
        grouped_files = {}

        for file in files:
            directory_tag = cls._get_directory_tag_for_file(file)
            file_group = grouped_files.get(directory_tag, list())
            file_group.append(file)
            grouped_files[directory_tag] = file_group

        return grouped_files

    @staticmethod
    def _get_directory_tag_for_file(file):
        return datetime.datetime.strptime(time.ctime(os.path.getmtime(file)), "%a %b %d %H:%M:%S %Y").strftime('%Y%m')
