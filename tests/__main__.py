from .tests import *
from src.logger.logger import Log

if __name__ == '__main__':
    log = Log()


    tt = TestTask()
    tt.test_task()

    tfm = TestFileManager()
    tfm.test_path()
    tfm.test_open_file()

    tsql = TestSQLite()
    tsql.test_add_snapshot()
    tsql.test_get_snapshot()
    # tsql

    # test_model = TestModel()
    # test_model.test_is_valid_min_max()

    # Docx Generation
    eo = TestExportOutput()
    # for _ in range(10):
    task = tsql.sample_task(randint(30, 40), randint(10, 30))
    # task = Task(14, 4, ['+', '-'], (1, 100))
    task.ex_generator.generate_final()
    eo.test_output(task)




