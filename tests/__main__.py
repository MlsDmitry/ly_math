from .tests import TestTask, TestUtils, TestSQLite
from src.logger.logger import Log

if __name__ == '__main__':
    log = Log()


    tt = TestTask()

    tt.test_task()

    tu = TestUtils()

    tu.test_path()

    tsql = TestSQLite()
    tsql.test_add_snapshot()
    tsql.test_get_snapshot()
    # tsql

