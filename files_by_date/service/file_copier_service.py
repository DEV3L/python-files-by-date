class FileCopierService:
    def __init__(self, *, input_dir, target_dir):
        self.input_dir = input_dir
        self.target_dir = target_dir

        # def copy_files(self):
        #     files = FilesService.gather_files(self.input_dir, list())
        #     FilesService.group_files_by_modified_date()
