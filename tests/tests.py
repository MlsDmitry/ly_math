from src.task import Task, ExampleGenerator
from src.file_manager import app_path, documents_path
from src.providers.sqlite_provider import DBManager, HistoryModel, PreferencesModel
from src.logger.logger import Log
from src.module.model import Model, Config

import unittest
from pprint import pprint
from random import randint, choices, choice
from string import ascii_letters


class TestTask(unittest.TestCase):
    def __init__(self):
        self.task = Task(17, 3, ['+', '-'], (10, 49))
        # self.ex_generator = ExampleGenerator(self.task, ['+', '-'], (10, 49))
        # self.ex_generator.generate_final()
        self.task.ex_generator.generate_final()

    def test_task(self):
        pprint(self.task._field)
        return True


class TestUtils(unittest.TestCase):
    def __init__(self):
        pass

    def test_path(self):
        print("Documents path: ", documents_path())
        return True


class TestModel(unittest.TestCase):
    def __init__(self):
        pass

    def test_is_valid_min_max(self):
        config = Config()
        config.min_number = "a"
        config.max_number = "0"
        is_valid = Model.validate_min_max_number()
        print("Documents path: ", is_valid)
        return True


class TestSQLite(unittest.TestCase):
    def __init__(self):
        db_manager = DBManager()
        self.dbm = db_manager
        db_manager.init_tables()
        hm = HistoryModel()
        self.hm = hm
        Log.log('d', hm.get_snapshot_names())
        hm.add_snaptshot(('testname', '+, -', 3, 3, 4, 20))
        Log.log('d', hm.get_snapshot_names())

    def test_add_snapshot(self):
        task = Task(17, 3, ['+', '-'], (10, 49))
        Log.log('d', f'Test format: {task.to_sqlite_format()}')
        # name = ''.join([choice(ascii_letters) for _ in range(randint(5, 15))])
        name = 'test1'
        self.hm.add_snaptshot([name, *task.to_sqlite_format()])
        self.dbm.save()
        Log.log('d', self.hm.get_snapshot_names())

    def sample_task(self):
        return Task(randint(1, 10), randint(1, 10), choices(['+', '-', '*', '/']), (randint(0, 40), randint(40, 80)))

    def sample_snapshot(self, task=None):
        if not task:
            task = self.sample_task()
        name = ''.join([choice(ascii_letters) for _ in range(randint(5, 15))])
        self.hm.add_snaptshot([name, *task.to_sqlite_format()])
        # self.hm.add_snaptshot()

    def test_get_snapshot(self):
        ret = self.hm.get_snapshot('test1')
        if not(ret == ('+,-', 17, 3, 10, 49)):
            Log.log('er', f'Not equal {ret}')
        task = Task.from_sqlite_format(ret)
        Log.log('d', task)