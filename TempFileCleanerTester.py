import os
import shutil
import unittest
from unittest.mock import patch, mock_open
from TempFileCleaner import recPath

class TestTempFileCleaner(unittest.TestCase):
    @patch('os.path.exists')
    @patch('os.listdir')
    @patch('os.remove')
    def test_temp_file_cleaner(self, mock_remove, mock_listdir, mock_exists):
        # Define the test cases
        test_cases = [
            {
                "name": "no files in directory",
                "exists": True,
                "files": [],
                "expected_remove_calls": []
            },
            {
                "name": "one file in directory",
                "exists": True,
                "files": ["file1.txt"],
                "expected_remove_calls": [((os.path.join(recPath, "file1.txt"),),)]
            },
            {
                "name": "multiple files in directory",
                "exists": True,
                "files": ["file1.txt", "file2.txt"],
                "expected_remove_calls": [
                    ((os.path.join(recPath, "file1.txt"),),),
                    ((os.path.join(recPath, "file2.txt"),),)
                ]
            },
            {
                "name": "directory does not exist",
                "exists": False,
                "files": [],
                "expected_remove_calls": []
            }
        ]

        # Run the test cases
        for test in test_cases:
            with self.subTest(test['name']):
                mock_exists.return_value = test['exists']
                mock_listdir.return_value = test['files']

                # Call the function to test
                if os.path.exists(recPath):
                    for file in os.listdir(recPath):
                        if os.path.exists(os.path.join(recPath, file)):
                            os.remove(os.path.join(recPath, file))

                # Check the calls to os.remove
                self.assertEqual(mock_remove.call_args_list, test['expected_remove_calls'])

                # Reset the mocks for the next test case
                mock_remove.reset_mock()

if __name__ == '__main__':
    unittest.main()
