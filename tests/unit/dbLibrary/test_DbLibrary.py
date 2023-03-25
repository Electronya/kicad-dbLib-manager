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
        self.jsonPkg = 'pkgs.dbLibrary.dbLibrary.json'

    def test_constructorCreateNewError(self) -> None:
        """
        The constructor must raise an exception when creating the new
        DB Library file fails.
        """
        testPath = '/home/jbacon/test'
        errMsg = 'test error'
        with patch.object(DbLibrary, '_createNewLib') as mockedCreateNewLib, \
                self.assertRaises(OSError) as context:
            mockedCreateNewLib.side_effect = OSError(errMsg)
            DbLibrary(testPath, isNew=True)
        self.assertEqual(str(context.exception), errMsg,
                         'The constructor failed to raise an exception when '
                         'creating the new file fails.')

    def test_constructorCreateNew(self) -> None:
        """
        The constructor must create the new DB library when specifying it.
        """
        testPath = '/home/jbacon/test'
        with patch.object(DbLibrary, '_createNewLib') as mockedCreateNewLib:
            DbLibrary(testPath, isNew=True)
            mockedCreateNewLib.assert_called_once()

    def test_constructorOpenLibError(self) -> None:
        """
        The constructor must raise an exception when opening an existing
        DB Library fails.
        """
        testPath = '/home/jbacon/test'
        errMsg = 'test error'
        with patch.object(DbLibrary, '_openLib') as mockedOpenLib, \
                self.assertRaises(OSError) as context:
            mockedOpenLib.side_effect = OSError(errMsg)
            DbLibrary(testPath)
        self.assertEqual(str(context.exception), errMsg,
                         'The constructor failed to raise an exception when '
                         'opening the library file fails.')

    def test_constructorOpenExisting(self) -> None:
        """
        The constructor must open an existing DB library when specifying it.
        """
        testPath = '/home/jbacon/test'
        with patch.object(DbLibrary, '_openLib') as mockedOpenLib:
            DbLibrary(testPath)
            mockedOpenLib.assert_called_once()
