import datetime
import os
import shutil
import time

from files_by_date.validators.argument_validator import ArgumentValidator


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

    @classmethod
    def copy_files(cls, file_groups, target_dir):
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        for group in file_groups:
            # group_dir = f'{target_dir}{os.sep}{group}' # 3.6
            group_dir = '{target_dir}{os_sep}{group}'.format(target_dir=target_dir, os_sep=os.sep, group=group)
            ArgumentValidator.validate_target_dir(group_dir)

            if not os.path.exists(group_dir):
                os.makedirs(group_dir)

            for file in file_groups[group]:
                # file_path = f'{group_dir}{os.path.basename(file)}' # 3.6
                file_path = '{group_dir}{os.path.basename(file)}'
                if not os.path.exists(file_path):
                    shutil.copy2(file, group_dir)

    @staticmethod
    def _get_directory_tag_for_file(file):
        return datetime.datetime.strptime(time.ctime(os.path.getmtime(file)), "%a %b %d %H:%M:%S %Y").strftime('%Y%m')
