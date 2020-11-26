from .tests import *
from src.logger.logger import Log

if __name__ == '__main__':
    log = Log()


    tt = TestTaskModel()
    tt.test_TaskModel()

    tfm = TestFileManager()
    tfm.test_path()
    # tfm.test_open_file()

    tsql = TestSQLite()
    tsql.test_add_snapshot()
    tsql.test_get_snapshot()
    # tsql

    # test_model = TestModel()
    # test_model.test_is_valid_min_max()

    # Docx Generation
    eo = TestExportManager()
    # for _ in range(10):
    task = tsql.sample_TaskModel(randint(30, 40), randint(10, 30))
    # task = TaskModel(14, 4, ['+', '-'], (1, 100))
    task.ex_generator.generate_final()
    eo.test_output(task)




