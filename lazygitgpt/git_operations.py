import os
from git import Repo, GitCommandError

def clone_repository(repo_url):
    """
    Clones a git repository from the given URL to the current working directory.

    :param repo_url: URL of the repository to clone.
    """
    try:
        # Get the name of the repository by parsing the URL
        repo_name = os.path.basename(repo_url)
        # If the URL ends with '.git', remove it
        if repo_name.endswith('.git'):
            repo_name = repo_name[:-4]
        # Use the current working directory as the destination
        destination = os.path.join(os.getcwd(), repo_name)
        Repo.clone_from(repo_url, destination)
        print(f"Repository cloned successfully to {destination}")
    except GitCommandError as e:
        print(f"Error cloning repository: {e}")

def checkout_branch(branch_name):
    """
    Checks out a specified branch in the current working directory.

    :param branch_name: Name of the branch to checkout.
    """
    try:
        # Use the current working directory as the repository path
        repo_path = os.getcwd()
        repo = Repo(repo_path)
        repo.git.checkout(branch_name)
        print(f"Checked out to branch {branch_name}")
    except GitCommandError as e:
        print(f"Error checking out branch: {e}")

def create_branch(branch_name):
    """
    Creates a new branch in the current working directory.

    :param branch_name: Name of the branch to create.
    """
    try:
        # Use the current working directory as the repository path
        repo_path = os.getcwd()
        repo = Repo(repo_path)
        repo.git.checkout('-b', branch_name)
        print(f"Created and checked out to new branch {branch_name}")
    except GitCommandError as e:
        print(f"Error creating new branch: {e}")