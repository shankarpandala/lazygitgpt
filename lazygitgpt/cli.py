import argparse
from lazygitgpt.git_operations import clone_repository, checkout_branch
from lazygitgpt.ai_operations import generate_response

def main():
    parser = argparse.ArgumentParser(description="lazygitgpt: Manage git repos and perform AI operations with GPT-4.")
    
    # Subparsers for different operations
    subparsers = parser.add_subparsers(dest='command', required=True)

    # Subparser for cloning a repository
    parser_clone = subparsers.add_parser('clone', help='Clone a git repository')
    parser_clone.add_argument('repo_url', type=str, help='URL of the git repository')
    parser_clone.add_argument('destination', type=str, help='Local path to clone the repository to')

    # Subparser for checking out a branch
    parser_checkout = subparsers.add_parser('checkout', help='Checkout a branch in a git repository')
    parser_checkout.add_argument('repo_path', type=str, help='Local path to the git repository')
    parser_checkout.add_argument('branch_name', type=str, help='Name of the branch to checkout')

    # Subparser for AI operations
    parser_ai = subparsers.add_parser('ai', help='Perform an AI operation using GPT-4')
    parser_ai.add_argument('input_text', type=str, help='Input text for the AI model')

    # Parse the arguments
    args = parser.parse_args()

    if args.command == 'clone':
        clone_repository(args.repo_url, args.destination)
    elif args.command == 'checkout':
        checkout_branch(args.repo_path, args.branch_name)
    elif args.command == 'ai':
        response = generate_response(args.input_text)
        print(f"AI Response: {response}")

if __name__ == '__main__':
    main()
