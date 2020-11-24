from .task_test import TestTask, TestUtils
from src.logger.logger import Log

if __name__ == '__main__':
    log = Log()
    

    tt = TestTask()

    tt.test_task()

    tu = TestUtils()

    tu.test_path()

