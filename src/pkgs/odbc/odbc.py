from logging import Logger

import pyodbc


def getDsnList(logger: Logger) -> tuple[str]:
    """
    Get the current system DSN list.

    Return
        A tuple containing the system current DSN list.
    """
    dsnList = pyodbc.dataSources()
    logger.debug(f"DSN list: {dsnList}")
    return tuple(dsnList.keys())


def connectionTest(logger: Logger, connStr: str) -> bool:
    """
    Test a database connection.

    Params
        connStr:    The connection string.

    Return
        True if the connection worked, False otherwise.
    """
    try:
        logger.debug(f"testing connection: {connStr}")
        pyodbc.connect(connStr)
    except Exception as e:
        logger.error(e)
        return False
    else:
        return True
