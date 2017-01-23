from unittest import TestCase

import pytest

from files_by_date.app.run import run


class TestRun(TestCase):
    def test_run(self):
        with pytest.raises(BaseException):
            run()

    run(args='input_dir target_dir'.split())
