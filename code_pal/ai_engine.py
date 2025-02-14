#!/usr/bin/env python3

"""
Description: This module contains the AI engine for Code-Pal,
an AI-powered code automation tool.

Author: Niloy Debnath
Email: debnath.niloy1988@gmail.com
"""

import os
import re

from openai import OpenAI
from code_pal.task_manager import register_command

def extract_code_blocks(response_text):
    """Extracts only the code blocks from OpenAI responses."""
    matches = re.findall(r"```[a-zA-Z]*\n(.*?)```", response_text, flags=re.DOTALL)
    return "\n".join(matches).strip() if matches else response_text.strip()

def generate_code_modification(code, system_content, model, temperature):
    """Generates code modifications using AI."""

    openai = OpenAI()

    response = openai.chat.completions.create(
        model=model,
        temperature=temperature,
        messages=[
            {"role": "system", "content": system_content},
            {"role": "user", "content": code},
        ],
    )
    return extract_code_blocks(response.choices[0].message.content)


@register_command("add_code_comments")
def add_code_comments(code, module_path, model, temperature):
    """Analyze the given code and add meaningful comments or docstrings where necessary."""

    return generate_code_modification(
        code,
        "Analyze the given code and add meaningful comments or docstrings where necessary.",
        model,
        temperature,
    )


@register_command("write_tests")
def write_tests(code, module_path, model, temperature):
    """Generate unit tests for the given module."""

    return generate_code_modification(
        code,
        "Generate unit tests for the given module.",
        model,
        temperature,
    )
