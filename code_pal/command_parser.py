#!/usr/bin/env python3

"""
Description: This module provides functions for parsing
and interpreting user instructions using AI. The `parse_commands`
function reads a command file and extracts instructions. It then
calls the `interpret_commands` function to map the instructions
to available commands using AI.

Author: Niloy Debnath
Email: debnath.niloy1988@gmail.com
"""

import configparser
import os
import json

from openai import OpenAI


def parse_commands(command_file: str, model: str, temperature: float):
    """Reads a command file and extracts instructions."""

    config = configparser.ConfigParser()
    config.read(command_file)

    instructions = [config["commands"][key] for key in config["commands"]]
    return interpret_commands(instructions, model, temperature)


def interpret_commands(instructions: str, model: str, temperature: float):
    """Uses AI to map user instructions to available commands."""

    prompt = f"""
    The following are user instructions for a code automation tool.
    Convert them into structured command names that match existing functionalities.

    Available commands:
    - add_code_comments
    - write_tests
    - push_code
    - create_pull_request

    Instructions:
    {instructions}

    Output should be a JSON dictionary mapping structured command names to True/False.
    Example output:
    {{"add_code_comments": true, "write_tests": true, "push_code": false, "create_pull_request": true}}
    """

    openai = OpenAI()

    response = openai.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "Convert user instructions into structured command names.",
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        temperature=temperature,
    )

    return json.loads(response.choices[0].message.content.replace("```json", "").replace("```", ""))
