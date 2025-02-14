#!/usr/bin/env python3

"""
Description: This module contains the CLI (Command Line Interface) 
for Code-Pal, an AI-powered code automation tool.

Author: Niloy Debnath
"""

import argparse
from code_pal.command_parser import parse_commands
from code_pal.task_manager import execute_tasks


def main():
    """Code-Pal: AI-powered code automation tool."""

    parser = argparse.ArgumentParser(
        description="Code-Pal: AI-powered code automation tool.",
    )
    parser.add_argument(
        "--module",
        required=True,
        help="Path to the source code file",
    )
    parser.add_argument(
        "--commands",
        required=True,
        help="Path to the command.ini file",
    )
    parser.add_argument(
        "--model",
        default="gpt-4o-mini",
        help="Specify the OpenAI model (default: gpt-4)",
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=0.7,
        help="Set OpenAI temperature (default: 0.7)",
    )
    args = parser.parse_args()

    commands = parse_commands(args.commands, args.model, args.temperature)
    execute_tasks(commands, args.module, args.model, args.temperature)


if __name__ == "__main__":
    main()
