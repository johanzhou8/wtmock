from unittest import TestCase, mock

from b_patching_classes.worker import Worker, Helper


class TestWorker(TestCase):

    def test_patching_class(self):
        with mock.patch('b_patching_classes.worker.Helper') as MockHelper:
            MockHelper.return_value.get_path.return_value = 'testing'
            worker = Worker()
            MockHelper.assert_called_once_with('db')
            self.assertEqual(worker.work(), 'testing')

    def test_patching_class_with_typo(self):
        with mock.patch('b_patching_classes.worker.Helper') as MockHelper:
            MockHelper.return_value.get_path.return_value = 'testing'
            worker = Worker()
            MockHelper.assrt_called_once_with('db')
            self.assertEqual(worker.work(), 'testing')

    def test_patching_class_with_spec(self):
        with mock.patch('b_patching_classes.worker.Helper', autospec=True) as MockHelper:
            MockHelper.return_value.get_path.return_value = 'testing'
            worker = Worker()
            MockHelper.assert_called_once_with('db')
            self.assertEqual(worker.work(), 'testing')

    def test_partial_patching(self):
        with mock.patch.object(Helper, 'get_path', return_value='testing'):
            worker = Worker()
            self.assertEqual(worker.helper.path, 'db')
            self.assertEqual(worker.work(), 'testing')


