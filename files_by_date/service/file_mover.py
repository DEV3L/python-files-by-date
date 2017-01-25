import os
import os.path, time


class FileMover:
    def __init__(self, *, input_dir, target_dir):
        self.input_dir = input_dir
        self.target_dir = target_dir

    # def move_files(self):
    #     files = self.gather_files(self.input_dir)
    #     pass

    @classmethod
    def gather_files(cls, parent_directory, files):
        for dir_name, subdir_list, file_list in os.walk(parent_directory):
            if file_list:
                files.append(
                    ['{dir_name}{os_sep}{file_name}'.format(dir_name=dir_name, os_sep=os.sep, file_name=file) for file
                     in file_list])
            for subdir in subdir_list:
                files = cls.gather_files(subdir, files)

        return files

# print("last modified: %s" % time.ctime(os.path.getmtime(file)))
# print("created: %s" % time.ctime(os.path.getctime(file)))
