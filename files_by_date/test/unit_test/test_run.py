from unittest import TestCase
from unittest.mock import patch

import pytest

from files_by_date.app.run import run


class TestRun(TestCase):
    def test_run(self):
        with pytest.raises(BaseException):
            run()


@patch('files_by_date.validators.argument_validator.ArgumentValidator')
def test_run(ArgumentValidator):
    ArgumentValidator.validate_arguments = lambda x: True
    run(args='input_dir target_dir'.split())

    # ArgumentValidator.validate_arguments = lambda x: raise_error(AssertionError())
    # with pytest.raises(AssertionError):
    #     run(args='input_dir target_dir'.split())

def raise_error(error):
    raise error