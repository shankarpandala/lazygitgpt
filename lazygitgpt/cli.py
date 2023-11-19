#!/usr/bin/env python3

import click
from lazygitgpt.git_operations import clone_repository, checkout_branch, create_branch
from lazygitgpt.ai_operations import generate_response

@click.group()
def cli():
    pass

@cli.command()
@click.argument('repo_url')
def clone(repo_url):
    """Clone a git repository"""
    clone_repository(repo_url)

@cli.command()
@click.argument('branch_name')
def checkout(branch_name):
    """Checkout a branch in a git repository"""
    checkout_branch(branch_name)

@cli.command()
@click.argument('branch_name')
def branch(branch_name):
    """Checkout a branch in a git repository"""
    create_branch(branch_name)

@cli.command()
@click.argument('input_text')
def ai(input_text):
    """Perform an AI operation using GPT-4"""
    response = generate_response(input_text)
    click.echo(f"AI Response: {response}")

if __name__ == '__main__':
    cli()
