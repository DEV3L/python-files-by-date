import os


class ArgumentValidator:
    @staticmethod
    def validate_input_dir(path):
        if not os.path.exists(os.path.dirname(path)) and os.access(os.path.dirname(path), os.R_OK):
            raise AssertionError(f'Invalid input directory: {path}')

        @staticmethod
        def validate_target_dir(path):
            if not os.access(os.path.dirname(path), os.W_OK):
                raise AssertionError(f'Invalid target directory: {path}')
