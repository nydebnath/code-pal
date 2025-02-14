#!/usr/bin/env python3

"""
Description: This module contains functions for performing
Git operations such as pushing code to GitHub and creating pull requests.

Author: Niloy Debnath
Email: debnath.niloy1988@gmail.com
"""

import logging
import subprocess


def push_to_github(commit_message: str, module_path: str):
    """Pushes code changes to GitHub."""

    try:
        subprocess.run(["git", "add", module_path], check=True)
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        subprocess.run(["git", "push"], check=True)
        logging.info("Code pushed to GitHub successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Git command failed: {e}")


def create_pull_request():
    """Creates a pull request on GitHub."""

    try:
        subprocess.run(
            [
                "gh",
                "pr",
                "create",
                "--title",
                "Auto PR",
                "--body",
                "Generated by Code-Pal",
            ],
            check=True,
        )
        logging.info("Pull request created successfully.")

    except subprocess.CalledProcessError as e:
        logging.error(f"GitHub PR creation failed: {e}")
