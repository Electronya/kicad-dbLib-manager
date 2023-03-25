from unittest import TestCase
from unittest.mock import call, Mock, mock_open, patch

import os
import sys

sys.path.append(os.path.abspath('./src'))

from pkgs.dbLibrary.dbLibrary import DbLibrary      # noqa: E402


class TestDbLibrary(TestCase):
    """
    The DbLibrary class test cases.
    """
    def setUp(self) -> None:
        """
        The test cases set up.
        """
