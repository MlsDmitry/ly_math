from src.task import Task, ExampleGenerator
from src.file_manager import app_path, documents_path

import unittest
from pprint import pprint


class TestTask(unittest.TestCase):
    def __init__(self):
        self.task = Task(17, 3)
        self.ex_generator = ExampleGenerator(self.task, ['+', '-'], (10, 49))
        self.ex_generator.generate_final()

    def test_task(self):
        pprint(self.task._field)
        return True


class TestUtils(unittest.TestCase):
    def __init__(self):
        pass

    def test_path(self):
        print("Documents path: ", documents_path())
        return True
        