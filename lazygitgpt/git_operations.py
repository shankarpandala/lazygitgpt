from git import Repo, GitCommandError

def clone_repository(repo_url, destination):
    """
    Clones a git repository from the given URL to the specified destination.

    :param repo_url: URL of the repository to clone.
    :param destination: Local path where the repository should be cloned.
    """
    try:
        Repo.clone_from(repo_url, destination)
        print(f"Repository cloned successfully to {destination}")
    except GitCommandError as e:
        print(f"Error cloning repository: {e}")

def checkout_branch(repo_path, branch_name):
    """
    Checks out a specified branch in a given repository.

    :param repo_path: Local path to the git repository.
    :param branch_name: Name of the branch to checkout.
    """
    try:
        repo = Repo(repo_path)
        repo.git.checkout(branch_name)
        print(f"Checked out to branch {branch_name}")
    except GitCommandError as e:
        print(f"Error checking out branch: {e}")
