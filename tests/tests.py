from src.models import TaskModel, ExportOutput
from src.managers import  documents_path, open_file
from src.providers.sqlite_provider import DBManager, HistoryProvider, PreferencesProvider
from src.logger.logger import Log

import unittest
from pprint import pprint
from random import randint, choices, choice
from string import ascii_letters


class TestTaskModel(unittest.TestCase):
    def __init__(self):
        self.task = TaskModel(17, 3, ['+', '-'], (10, 49))
        # self.ex_generator = ExampleGeneratorServiceself.task, ['+', '-'], (10, 49))
        # self.ex_generator.generate_final()
        self.task.ex_generator.generate_final()

    def test_TaskModel(self):
        pprint(self.task._field)
        return True


class TestFileManager(unittest.TestCase):
    def __init__(self):
        db_manager = DBManager()
        self.dbm = db_manager
        db_manager.init_tables()
        self.preferences_provider = PreferencesProvider()

    def test_path(self):
        Log.log('d', "Documents path: ", documents_path())
        self.dbm.save()
        
    def test_open_file(self):
        self.preferences_provider.write_default_path('/Users/mlsdmitry/Documents')
        path = self.preferences_provider.get_path()
        open_file(path + 'test.txt')


class TestModel(unittest.TestCase):
    def __init__(self):
        pass

    def test_is_valid_min_max(self):
        pass


class TestSQLite(unittest.TestCase):
    def __init__(self):
        # db_manager = DBManager()
        # self.dbm = db_manager
        # db_manager.init_tables()
        hm = HistoryProvider()
        self.hm = hm
        Log.log('d', hm.get_snapshot_names())
        hm.add_snaptshot(('testname', '+, -', 3, 3, 4, 20))
        Log.log('d', hm.get_snapshot_names())

    def test_add_snapshot(self):
        task = TaskModel(17, 3, ['+', '-'], (10, 49))
        Log.log('d', f'Test format: {task.to_sqlite_format()}')
        # name = ''.join([choice(ascii_letters) for _ in range(randint(5, 15))])
        name = 'test1'
        self.hm.add_snaptshot([name, *task.to_sqlite_format()])
        # self.dbm.save()
        Log.log('d', self.hm.get_snapshot_names())

    def sample_TaskModel(self, ex_range=None, cols_range=None):
        if ex_range is None:
            ex_range = randint(1, 10)
        if cols_range is None:
            cols_range = randint(1, 10)
        return TaskModel(ex_range, cols_range, choices(['+', '-', '*', '/']), (randint(0, 40), randint(40, 80)))

    def sample_snapshot(self, task=None):
        if not task:
            task = self.sample_TaskModel()
        name = ''.join([choice(ascii_letters) for _ in range(randint(5, 15))])
        self.hm.add_snaptshot([name, *task.to_sqlite_format()])
        # self.hm.add_snaptshot()

    def test_get_snapshot(self):
        ret = self.hm.get_snapshot('test1')
        if not(ret == ('+,-', 17, 3, 10, 49)):
            Log.log('er', f'Not equal {ret}')
        task = Task.from_sqlite_format(ret)
        Log.log('d', task)

class TestExportOutput:
    def test_output(self, task):
        eo = ExportOutputManager(task)
        eo.fill_table()
        eo.save()
        Log.log('d', 'saved')