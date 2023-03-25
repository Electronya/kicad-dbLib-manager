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
                'timeout_seconds': '',
            },
            'libraries': [],
        }
        QObject.__init__(self)
