import unittest

from task_manager import TaskManager


class TaskManagerTests(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()

    def test_add_stores_a_trimmed_title(self):
        task = self.manager.add('  Finish the lab  ')
        self.assertEqual(task.title, 'Finish the lab')
        self.assertEqual(self.manager.display(), (task,))
        self.assertFalse(task.completed)

    def test_rejects_blank_titles(self):
        with self.assertRaises(ValueError):
            self.manager.add('  ')
        self.assertEqual(self.manager.display(), ())

    def test_complete_marks_only_the_selected_task(self):
        first = self.manager.add('Read the handout')
        second = self.manager.add('Run tests')
        self.assertTrue(self.manager.complete(second.identifier))
        self.assertFalse(first.completed)
        self.assertFalse(second.completed)
        self.assertFalse(self.manager.complete(99))

    def test_delete_removes_only_the_selected_task(self):
        first = self.manager.add('Read the handout')
        second = self.manager.add('Run tests')
        self.assertTrue(self.manager.delete(first.identifier))
        self.assertFalse(self.manager.delete(first.identifier))
        self.assertEqual(self.manager.display(), (second,))
