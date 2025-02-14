#!/usr/bin/env python3

"""
Description: This module is responsible for managing tasks using Code-Pal.

Author: Niloy Debnath
Email: debnath.niloy1988@gmail.com
"""

import logging
from code_pal.git_operations import push_to_github, create_pull_request
import os

COMMANDS = {}


def register_command(name):
    """Decorator to register a command function."""

    def decorator(func):
        COMMANDS[name] = func
        return func

    return decorator


def execute_tasks(commands, module_path, model, temperature):
    """Executes tasks based on user commands."""

    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )

    try:
        # Lazy Import to Avoid Circular Dependency
        import code_pal.ai_engine

        with open(module_path, "r") as file:
            code = file.read()

        print(f"Commands: {commands}")

        for command, enabled in commands.items():
            if enabled and command in COMMANDS:
                logging.info(f"Executing: {command}...")

                if command == "add_code_comments":
                    code = COMMANDS[command](code, module_path, model, temperature)
                    with open(module_path, "w") as file:
                        file.write(code)

                elif command == "write_tests":
                    test_code = COMMANDS[command](code, module_path, model, temperature)
                    test_file = os.path.basename(module_path).replace(".py", "_test.py")
                    test_dir = os.path.join(os.path.dirname(module_path), "tests")
                    os.makedirs(test_dir, exist_ok=True)

                    with open(os.path.join(test_dir, test_file), "w") as file:
                        file.write(test_code)

        if commands.get("push_code", False):
            push_to_github("Automated changes by Code-Pal", module_path)

        if commands.get("create_pull_request", False):
            create_pull_request()

        logging.info("All tasks executed successfully.")

    except Exception as e:
        logging.error(f"Execution failed: {e}")
