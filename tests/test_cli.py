import unittest
from unittest.mock import patch
from lazygitgpt.cli import main

class TestCLI(unittest.TestCase):

    @patch('lazygitgpt.cli.argparse.ArgumentParser.parse_args')
    @patch('lazygitgpt.git_operations.clone_repository')
    def test_clone_command(self, mock_clone_repo, mock_parse_args):
        mock_parse_args.return_value = argparse.Namespace(
            command='clone', repo_url='https://example.com/repo.git', destination='/path/to/destination')
        
        main()
        mock_clone_repo.assert_called_once_with('https://example.com/repo.git', '/path/to/destination')

    @patch('lazygitgpt.cli.argparse.ArgumentParser.parse_args')
    @patch('lazygitgpt.git_operations.checkout_branch')
    def test_checkout_command(self, mock_checkout_branch, mock_parse_args):
        mock_parse_args.return_value = argparse.Namespace(
            command='checkout', repo_path='/path/to/repo', branch_name='feature-branch')
        
        main()
        mock_checkout_branch.assert_called_once_with('/path/to/repo', 'feature-branch')

    @patch('lazygitgpt.cli.argparse.ArgumentParser.parse_args')
    @patch('lazygitgpt.ai_operations.generate_response')
    def test_ai_command(self, mock_generate_response, mock_parse_args):
        mock_parse_args.return_value = argparse.Namespace(
            command='ai', input_text='Hello, AI!')
        
        main()
        mock_generate_response.assert_called_once_with('Hello, AI!')

if __name__ == '__main__':
    unittest.main()
