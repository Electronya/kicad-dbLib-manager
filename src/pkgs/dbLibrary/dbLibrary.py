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
