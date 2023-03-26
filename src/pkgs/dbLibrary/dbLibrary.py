import logging
import json

from PySide2.QtCore import QObject


class DbLibrary(QObject):
    """
    The database library class.
    """
    def __init__(self, path: str, isNew: bool = False) -> None:
        """
        Constructor.
        """
        QObject.__init__(self)
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
            json.dump(template, fd, indent=4)

    def _openLib(self) -> None:
        """
        Open an existing DB library.
        """
        with open(self._path) as fd:
            self._config = json.load(fd)

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

        Params:
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

        Params:
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

        Params:
            The data source type.
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

        Params:
            The data source name.
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

        Params:
            The data source username.
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

        Params:
            The data source password.
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

        Params:
            The data source connection string.
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

        Params:
            The data source connection timeout.
        """
        self._config['source']['timeout_seconds'] = timeout
