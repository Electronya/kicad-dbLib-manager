import logging
import json

from PySide2.QtCore import QObject, Signal


class DbLibrary(QObject):
    """
    The database library class.
    """
    connTestSig = Signal(str)

    def __init__(self, path: str, isNew: bool = False) -> None:
        """
        Constructor.
        """
        QObject.__init__(self)
        self._logger = logging.getLogger('app.library')
        self._path = path
        if isNew:
            self._createNewLib()
        else:
            self._openLib()

    def _createNewLib(self) -> None:
        """
        Create a new DB library.
        """
        template = {
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
        with open(self._path, 'w') as fd:
            self._config = template
            self._savedConfig = self._config.copy()
            json.dump(template, fd, indent=4)

    def _openLib(self) -> None:
        """
        Open an existing DB library.
        """
        with open(self._path) as fd:
            self._config = json.load(fd)
            self._savedConfig = self._config.copy()

    def isSaved(self) -> bool:
        """
        Check if any and all changed have been saved.

        Return
            True if any and all changes have been saved, False otherwise.
        """
        return self._config == self._savedConfig

    def discardChanges(self) -> None:
        """
        Discard any and all unsaved changes.
        """
        self._config = self._savedConfig.copy()

    def getPath(self) -> str:
        """
        Get the library path.

        Return
            The library file path.
        """
        return self._path

    def getVersion(self) -> int:
        """
        Get the DB library configuration version.

        Return
            The DB library configuration version.
        """
        return self._config['meta']['version']

    def setVersion(self, version: int) -> None:
        """
        Set the DB library configuration version.

        Params
            version:    The DB library configuration version.
        """
        self._config['meta']['version'] = version

    def getName(self) -> str:
        """
        Get the DB library name.

        Return
            The DB library name.
        """
        return self._config['name']

    def setName(self, name: str) -> None:
        """
        Set the DB library name.

        Params
            name:   The DB library name.
        """
        self._config['name'] = name

    def getDescription(self) -> str:
        """
        Get the DB library description.

        Return
            The DB library description.
        """
        return self._config['description']

    def setDescription(self, description: str) -> None:
        """
        Set the DB library description.

        Params
            description:    The DB library description.
        """
        self._config['description'] = description

    def getSourceType(self) -> str:
        """
        Get the data source type.

        Return
            The data source type.
        """
        return self._config['source']['type']

    def setSourceType(self, type: str) -> None:
        """
        Set the data source type.

        Params
            type:   The data source type.
        """
        self._config['source']['type'] = type

    def getSourceDsn(self) -> str:
        """
        Get the data source name.

        Return
            The data source name.
        """
        return self._config['source']['dsn']

    def setSourceDsn(self, dsn: str) -> None:
        """
        Set the data source name.

        Params
            dsn:    The data source name.
        """
        self._config['source']['dsn'] = dsn

    def getSourceUsername(self) -> str:
        """
        Get the data source username.

        Return
            The data source username.
        """
        return self._config['source']['username']

    def setSourceUsername(self, username: str) -> None:
        """
        Set the data source username.

        Params
            username:   The data source username.
        """
        self._config['source']['username'] = username

    def getSourcePassword(self) -> str:
        """
        Get the data source password.

        Return
            The data source password.
        """
        return self._config['source']['password']

    def setSourcePassword(self, password: str) -> None:
        """
        Set the data source password.

        Params
            password:   The data source password.
        """
        self._config['source']['password'] = password

    def getSourceConnStr(self) -> str:
        """
        Get the data source connection string.

        Return
            The data source connection string.
        """
        return self._config['source']['connection_string']

    def setSourceConnStr(self, connStr: str) -> None:
        """
        Set the data source connection string.

        Params
            connStr:    The data source connection string.
        """
        self._config['source']['connection_string'] = connStr

    def getSourceTimeout(self) -> int:
        """
        Get the data source connection timeout.

        Return
            The data source connection timeout.
        """
        return self._config['source']['timeout_seconds']

    def setSourceTimeout(self, timeout: int) -> None:
        """
        Set the data source connection timeout.

        Params
            timeout:    The data source connection timeout.
        """
        self._config['source']['timeout_seconds'] = timeout

    def save(self, path: str = None) -> None:
        """
        Save the DB library. If a path is given, the library is saved as.

        Params:
            path:       The new library path if saving as.
        """
        if path is None:
            savePath = self._path
        else:
            savePath = path
        with open(savePath, 'w') as fd:
            json.dump(self._config, fd)
        self._path = savePath
        self._savedConfig = self._config.copy()

    def getOdbcDsnList(self) -> tuple:
        """
        Get the system active ODBC DSN list.

        Return
            A tuple containing the system ODBC DSN list.
        """
        return ()

    def testConnection(self) -> None:
        """
        Test the library DB connection.
        """
