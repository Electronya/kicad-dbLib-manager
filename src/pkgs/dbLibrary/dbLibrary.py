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
        self._path = f"{path}.kicad_dbl"
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
