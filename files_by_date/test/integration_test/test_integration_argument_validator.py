from unittest.mock import patch

import pytest

from files_by_date.validators.argument_validator import ArgumentValidator


def test_validate_input_dir():
    assert not ArgumentValidator.validate_input_dir('./resources')
    with pytest.raises(AssertionError):
        ArgumentValidator.validate_input_dir('./resourcesX')


def test_validate_target_dir():
    assert not ArgumentValidator.validate_target_dir('./resources')
    assert not ArgumentValidator.validate_target_dir('./resourcesX')


@patch('files_by_date.validators.argument_validator.os')
def test_validate_target_dir_with_exception(os):
    os.access = lambda x, y: False

    with pytest.raises(AssertionError):
        ArgumentValidator.validate_target_dir('test')
