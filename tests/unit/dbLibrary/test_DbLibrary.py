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
            fd.seek(0)
            self.libConfigStr = fd.read()
        self.libPath = '/home/jbacon/test'
        with patch.object(DbLibrary, '_openLib'):
            self.dut = DbLibrary(self.libPath)
        self.dut._config = self.libConfig

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

    def test_openLibOpenFileError(self) -> None:
        """
        The _openLib method must raise an exception when opening the
        DB library file fails.
        """
        errMsg = 'test error'
        with patch('builtins.open') as mockedOpen, \
                self.assertRaises(OSError) as context:
            mockedOpen.side_effect = OSError(errMsg)
            self.dut._openLib()
        self.assertEqual(str(context.exception), errMsg,
                         '_openLib failed to raise an exception when opening '
                         'the library file.')

    def test_openLibLoadError(self) -> None:
        """
        The _openLib method must raise an exception when loading the config
        fails.
        """
        errMsg = 'test error'
        with patch('builtins.open', mock_open(read_data=self.libConfigStr)), \
                patch(self.jsonPkg) as mockedJsonPkg, \
                self.assertRaises(json.JSONDecodeError) as context:
            mockedJsonPkg.load.side_effect = json.JSONDecodeError(errMsg,
                                                                  'test', 2)
            self.dut._openLib()
        self.assertEqual(str(context.exception),
                         f"{errMsg}: line 1 column 3 (char 2)",
                         '_openLib failed to raise an exception when '
                         'loading the config from the library file fails.')

    def test_openLib(self) -> None:
        """
        The _openLib method must read the DB library file and load the library
        configuration.
        """
        with patch('builtins.open', mock_open(read_data=self.libConfigStr)) \
                as mockedOpen, patch(self.jsonPkg) as mockedJsonPkg:
            mockedJsonPkg.load.return_value = self.libConfig
            self.dut._openLib()
            mockedOpen.assert_called_once_with(self.dut._path)
            mockedJsonPkg.load.assert_called_once_with(mockedOpen().__enter__())    # noqa: E501
            self.assertEqual(self.dut._config, self.libConfig,
                             '_openLib failed to load the library config.')

    def test_getVersion(self) -> None:
        """
        The getVersion method must return the DB library configuration
        version.
        """
        version = self.dut.getVersion()
        self.assertEqual(version, self.libConfig['meta']['version'],
                         'getVersion failed to return the DB library '
                         'configuration version')

    def test_setVersion(self) -> None:
        """
        The setVersion method must update the DB library configuration
        version with the received one.
        """
        version = 32
        self.dut.setVersion(version)
        self.assertEqual(self.dut._config['meta']['version'], version,
                         'setVersion failed to update the DB library '
                         'configuration version.')

    def test_getName(self) -> None:
        """
        The getName method must return the DB library name.
        """
        name = self.dut.getName()
        self.assertEqual(name, self.libConfig['name'],
                         'getName failed to return the DB library name.')

    def test_setName(self) -> None:
        """
        The setName method must update the DB library name.
        """
        name = 'test name'
        self.dut.setName(name)
        self.assertEqual(self.dut._config['name'], name,
                         'setName failed to update the DB library name.')

    def test_getDescription(self) -> None:
        """
        The getDescription method must return the DB library description.
        """
        description = self.dut.getDescription()
        self.assertEqual(description, self.libConfig['description'],
                         'getDescription failed to return the DB library '
                         'description.')

    def test_setDescription(self) -> None:
        """
        The setDescription method must update the DB library description.
        """
        description = 'test description'
        self.dut.setDescription(description)
        self.assertEqual(self.dut._config['description'], description,
                         'setDescription failed to update the DB library '
                         'description.')
