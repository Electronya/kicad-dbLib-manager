import json

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
        self.template = {
            'meta': {'version': 0},
            'name': 'New database library',
            'description': 'A new database of components.',
            'source': {
                'type': 'odbc',
                'dsn': '',
                'username': '',
                'password': '',
                'connection_string': '',
                'timeout_seconds': 2,
            },
            'libraries': [],
        }
        with open(('./tests/unit/dbLibrary/testDbLib.kicad_dbl')) as fd:
            self.libConfig = json.load(fd)
        self.libPath = '/home/jbacon/test'
        with patch.object(DbLibrary, '_openLib'):
            self.dut = DbLibrary(self.libPath)

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

    def test_createNewLibCreateFileError(self) -> None:
        """
        The _createNewLib method must raise an exception when creating the new
        DB library file fails.
        """
        errMsg = 'test error'
        with patch('builtins.open') as mockedOpen, \
                self.assertRaises(OSError) as context:
            mockedOpen.side_effect = OSError(errMsg)
            self.dut._createNewLib()
        self.assertEqual(str(context.exception), errMsg,
                         '_createNewLib failed to raise an exception when '
                         'creating the new file fails.')

    def test_createNewLibDumpError(self) -> None:
        """
        The _createNewLib method must raise an exception when dumping the
        default config fails.
        """
        errMsg = 'test error'
        with patch('builtins.open'), patch(self.jsonPkg) as mockedJsonPkg, \
                self.assertRaises(json.JSONDecodeError) as context:
            mockedJsonPkg.dump.side_effect = json.JSONDecodeError(errMsg,
                                                                  'test', 2)
            self.dut._createNewLib()
        self.assertEqual(str(context.exception),
                         f"{errMsg}: line 1 column 3 (char 2)",
                         '_createNewLib failed to raise an exception when '
                         'dumping the default config in the new file fails.')

    def test_createNewLib(self) -> None:
        """
        The _createNewLib method must save the template config in the new
        DB library file.
        """
        with patch('builtins.open') as mockedOpen, \
                patch(self.jsonPkg) as mockedJsonPkg:
            self.dut._createNewLib()
            mockedOpen.assert_called_once_with(self.dut._path, 'w')
            mockedJsonPkg.dump.assert_called_once_with(self.template,
                                                       mockedOpen().__enter__(),    # noqa: E501
                                                       indent=4)
            self.assertEqual(self.dut._config, self.template,
                             '_createNewLib failed to save the template '
                             'config.')
