import copy
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
        self.copyPkg = 'pkgs.dbLibrary.dbLibrary.copy'
        self.jsonPkg = 'pkgs.dbLibrary.dbLibrary.json'
        self.getDsnList = 'pkgs.dbLibrary.dbLibrary.getDsnList'
        self.loggingPkg = 'pkgs.dbLibrary.dbLibrary.logging'
        self.mockedLogger = Mock()
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
        with open('./tests/unit/dbLibrary/testDbLib.kicad_dbl') as fd:
            self.libConfig = json.load(fd)
            fd.seek(0)
            self.libConfigStr = fd.read()
        self.libPath = '/home/jbacon/test'
        with patch(self.loggingPkg), patch.object(DbLibrary, '_openLib'):
            self.dut = DbLibrary(self.libPath)
        self.dut._config = self.libConfig
        self.dut._savedConfig = copy.deepcopy(self.libConfig)

    def test_constructorGetLogger(self) -> None:
        """
        The constructor must get the appropriate logger.
        """
        with patch(self.loggingPkg) as mockedLogPkg, \
                patch.object(DbLibrary, '_createNewLib'):
            DbLibrary(self.libPath, isNew=True)
            mockedLogPkg.getLogger.assert_called_once_with('app.library')

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
                patch(self.copyPkg) as mockedCopyPkg, \
                patch(self.jsonPkg) as mockedJsonPkg:
            mockedCopyPkg.deepcopy.return_value = copy.deepcopy(self.template)
            self.dut._createNewLib()
            mockedOpen.assert_called_once_with(self.dut._path, 'w')
            mockedJsonPkg.dump.assert_called_once_with(self.template,
                                                       mockedOpen().__enter__(),    # noqa: E501
                                                       indent=4)
            mockedCopyPkg.deepcopy.assert_called_once_with(self.dut._config)
            self.assertEqual(self.dut._config, self.template,
                             '_createNewLib failed to save the template '
                             'config.')
            self.assertEqual(self.dut._config, self.dut._savedConfig,
                             '_createNewLib failed to copy the configuration '
                             'for change management.')

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
                as mockedOpen, patch(self.copyPkg) as mockedCopyPkg, \
                patch(self.jsonPkg) as mockedJsonPkg:
            mockedCopyPkg.deepcopy.return_value = copy.deepcopy(self.libConfig)
            mockedJsonPkg.load.return_value = self.libConfig
            self.dut._openLib()
            mockedOpen.assert_called_once_with(self.dut._path)
            mockedJsonPkg.load.assert_called_once_with(mockedOpen().__enter__())    # noqa: E501
            mockedCopyPkg.deepcopy.assert_called_once_with(self.dut._config)
            self.assertEqual(self.dut._config, self.libConfig,
                             '_openLib failed to load the library config.')
            self.assertEqual(self.dut._config, self.dut._savedConfig,
                             '_createNewLib failed to copy the configuration '
                             'for change management.')

    def test_isSavedChangesSaved(self) -> None:
        """
        The isSaved method must return true if any and all configuration
        changes have been saved.
        """
        result = self.dut.isSaved()
        self.assertTrue(result, 'isSaved failed to return true when any and '
                        'all changes have been saved.')

    def test_isSavedChangesUnsaved(self) -> None:
        """
        The isSaved method must return false if the library have unsaved
        changes in its configuration.
        """
        self.dut._config['name'] = 'new name'
        result = self.dut.isSaved()
        self.assertFalse(result, 'isSaved failed to return false when there '
                         'is unsaved changes.')

    def test_discardChanges(self) -> None:
        """
        The discardChanges method must discard any and all unsaved changes.
        """
        self.dut._config['name'] = 'new name'
        self.dut._config['source']['dsn'] = 'new dsn name'
        self.dut.discardChanges()
        self.assertTrue(self.dut._config == self.dut._savedConfig,
                        'discardChanges failed to discard any and all unsaved '
                        'configuration changes.')

    def test_getPath(self) -> None:
        """
        The getPath method must return the DB Library file path.
        """
        path = self.dut.getPath()
        self.assertEqual(path, self.libPath,
                         'getPath failed to return the DB library file path.')

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

    def test_getSourceType(self) -> None:
        """
        The getSourceType method must return the DB library data source type.
        """
        type = self.dut.getSourceType()
        self.assertEqual(type, self.libConfig['source']['type'],
                         'getSourceType failed to return the DB library '
                         'data source type.')

    def test_setSourceType(self) -> None:
        """
        The setSourceType method must update the DB library data source type.
        """
        sourceType = 'test sourceType'
        self.dut.setSourceType(sourceType)
        self.assertEqual(self.dut._config['source']['type'], sourceType,
                         'setSourceType failed to update the DB library '
                         'data source type.')

    def test_getSourceDsn(self) -> None:
        """
        The getSourceDsn method must return the DB library data source name.
        """
        dsn = self.dut.getSourceDsn()
        self.assertEqual(dsn, self.libConfig['source']['dsn'],
                         'getSourceDsn failed to return the DB library '
                         'dsn.')

    def test_setSourceDsn(self) -> None:
        """
        The setSourceDsn method must update the DB library data source name.
        """
        dsn = 'test dsn'
        self.dut.setSourceDsn(dsn)
        self.assertEqual(self.dut._config['source']['dsn'], dsn,
                         'setSourceDsn failed to update the DB library '
                         'dsn.')

    def test_getSourceUsername(self) -> None:
        """
        The getSourceUsername method must return the DB library data source
        username.
        """
        username = self.dut.getSourceUsername()
        self.assertEqual(username, self.libConfig['source']['username'],
                         'getSourceUsername failed to return the DB library '
                         'data source username.')

    def test_setSourceUsername(self) -> None:
        """
        The setSourceUsername method must update the DB library data source
        username.
        """
        username = 'test username'
        self.dut.setSourceUsername(username)
        self.assertEqual(self.dut._config['source']['username'], username,
                         'setSourceUsername failed to update the DB library '
                         'data source username.')

    def test_getSourcePassword(self) -> None:
        """
        The getSourcePassword method must return the DB library data source
        password.
        """
        password = self.dut.getSourcePassword()
        self.assertEqual(password, self.libConfig['source']['password'],
                         'getSourcePassword failed to return the DB library '
                         'data source password.')

    def test_setSourcePassword(self) -> None:
        """
        The setSourcePassword method must update the DB library data source
        password.
        """
        password = 'test password'
        self.dut.setSourcePassword(password)
        self.assertEqual(self.dut._config['source']['password'], password,
                         'setSourcePassword failed to update the DB library '
                         'data source password.')

    def test_getSourceConnStr(self) -> None:
        """
        The getSourceConnStr method must return the DB library data source
        connection string.
        """
        connStr = self.dut.getSourceConnStr()
        self.assertEqual(connStr,
                         self.libConfig['source']['connection_string'],
                         'getSourceConnStr failed to return the DB library '
                         'data source connection string.')

    def test_setSourceConnStr(self) -> None:
        """
        The setSourceConnStr method must update the DB library data source
        connection string.
        """
        connStr = 'test connection string'
        self.dut.setSourceConnStr(connStr)
        self.assertEqual(self.dut._config['source']['connection_string'],
                         connStr,
                         'setSourceConnStr failed to update the DB library '
                         'data source connection string.')

    def test_getSourceTimeout(self) -> None:
        """
        The getSourceTimeout method must return the DB library data source
        timeout.
        """
        timeout = self.dut.getSourceTimeout()
        self.assertEqual(timeout,
                         self.libConfig['source']['timeout_seconds'],
                         'getSourceTimeout failed to return the DB library '
                         'data source timeout.')

    def test_setSourceTimeout(self) -> None:
        """
        The setSourceTimeout method must update the DB library data source
        timeout.
        """
        timeout = 32
        self.dut.setSourceTimeout(timeout)
        self.assertEqual(self.dut._config['source']['timeout_seconds'],
                         timeout,
                         'setSourceTimeout failed to update the DB library '
                         'data source timeout.')

    def test_saveOpenFileError(self) -> None:
        """
        The save method must raise an exception when opening the library
        file.
        """
        errMsg = 'test error'
        with patch('builtins.open') as mockedOpen, \
                self.assertRaises(OSError) as context:
            mockedOpen.side_effect = OSError(errMsg)
            self.dut.save()
        self.assertEqual(str(context.exception), errMsg,
                         'save failed to raise an exception when opening '
                         'the library file fails.')

    def test_saveDumpError(self) -> None:
        """
        The save method must raise an exception when dumping the configuration
        fails.
        """
        errMsg = 'test error'
        with patch('builtins.open'), patch(self.jsonPkg) as mockedJsonPkg, \
                self.assertRaises(json.JSONDecodeError) as context:
            mockedJsonPkg.dump.side_effect = json.JSONDecodeError(errMsg,
                                                                  'test', 2)
            self.dut.save()
        self.assertEqual(str(context.exception),
                         f"{errMsg}: line 1 column 3 (char 2)",
                         'save failed to raise an exception when dumping the '
                         'configuration fails.')

    def test_saveOriginal(self) -> None:
        """
        The save method must save the configuration changes as the original
        library file when no new path is given.
        """
        self.dut._config['name'] = 'new name'
        with patch('builtins.open') as mockedOpen, \
                patch(self.jsonPkg) as mockedJsonPkg:
            self.dut.save()
            mockedOpen.assert_called_once_with(self.libPath, 'w')
            mockedJsonPkg.dump.assert_called_once_with(self.dut._config,
                                                       mockedOpen().__enter__())    # noqa: E501
            self.assertEqual(self.dut._path, self.libPath,
                             'save failed to save the config changes as the '
                             'original library file.')
            self.assertEqual(self.dut._savedConfig, self.dut._config,
                             'save failed to copy the config in order to '
                             'manage changes.')

    def test_saveAs(self) -> None:
        """
        The save method must save the configuration changes as a new library
        file when a new path is given.
        """
        newPath = 'new/path/to/library.kicad_dbl'
        self.dut._config['name'] = 'new name'
        with patch('builtins.open') as mockedOpen, \
                patch(self.jsonPkg) as mockedJsonPkg:
            self.dut.save(newPath)
            mockedOpen.assert_called_once_with(newPath, 'w')
            mockedJsonPkg.dump.assert_called_once_with(self.dut._config,
                                                       mockedOpen().__enter__())    # noqa: E501
            self.assertEqual(self.dut._path, newPath,
                             'save failed to save the config changes as the '
                             'original library file.')
            self.assertEqual(self.dut._savedConfig, self.dut._config,
                             'save failed to copy the config in order to '
                             'manage changes.')

    def test_getOdbcDsnList(self) -> None:
        """
        The getOdbcDsnList method must get and return the list of ODBC DSN
        sources.
        """
        testDsnList = ('dsn 1', 'dsn 2', 'dsn 3')
        with patch(self.getDsnList) as mockedGetDsnList:
            mockedGetDsnList.return_value = testDsnList
            result = self.dut.getOdbcDsnList()
            mockedGetDsnList.assert_called_once_with(self.dut._logger)
            self.assertEqual(result, testDsnList,
                             'getOdbcDsnList failed to return the DSN list.')
