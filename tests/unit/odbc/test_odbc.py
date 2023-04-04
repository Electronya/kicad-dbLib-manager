from unittest import TestCase
from unittest.mock import call, Mock, mock_open, patch


import pyodbc

import os
import sys

sys.path.append(os.path.abspath('./src'))

from pkgs.odbc.odbc import getDsnList, connectionTest       # noqa: E402


class TestOdbc(TestCase):
    """
    The ODBC module test cases.
    """
    def setUp(self) -> None:
        """
        The test cases setup.
        """
        self.pyodbcPkg = 'pkgs.odbc.odbc.pyodbc'
        self.mockedLogger = Mock()

    def test_getDsnListEmpty(self) -> None:
        """
        The getDsnList function must return an empty tuple if no DSN is
        found.
        """
        with patch(self.pyodbcPkg) as mockedOdbc:
            mockedOdbc.dataSources.return_value = {}
            result = getDsnList(self.mockedLogger)
            self.assertEqual(result, (), 'getOdbcDsnList failed to return '
                             'an empty tuple.')

    def test_getDsnList(self) -> None:
        """
        The getDsnList function must return the list of the DSN found in
        a tuple.
        """
        with patch(self.pyodbcPkg) as mockedOdbc:
            mockedOdbc.dataSources.return_value = {'DSN 1': 'DSN 1 connection',
                                                   'DSN 2': 'DSN 2 connection',
                                                   'DSN 3': 'DSN 3 connection'}
            result = getDsnList(self.mockedLogger)
            self.assertEqual(result, ('DSN 1', 'DSN 2', 'DSN 3'),
                             'getOdbcDsnList failed to return an empty tuple.')

    def test_connectionTestFail(self) -> None:
        """
        The connectionTest function must return false if the connection
        to the database fails.
        """
        with patch(self.pyodbcPkg) as mockedOdbc:
            mockedOdbc.connect.side_effect = pyodbc.OperationalError()
            result = connectionTest(self.mockedLogger, 'test conn. string')
            self.assertFalse(result, 'connectionTest failed to return false '
                             'when the connection test fails.')

    def test_connectionTestSuccess(self) -> None:
        """
        The connectionTest function must return true if the connection
        to the database succeed.
        """
        connStr = 'test conn. string'
        with patch(self.pyodbcPkg) as mockedOdbc:
            result = connectionTest(self.mockedLogger, connStr)
            mockedOdbc.connect.assert_called_once_with(connStr)
            self.assertTrue(result, 'connectionTest failed to return true '
                            'when the connection test succeeds.')
