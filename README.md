# Code-Pal
![Image](./images/code-pal-pic.png)

## Overview
Code-Pal is an AI-powered coding assistant that interprets **natural language commands** and automates code modifications, documentation, testing, and GitHub operations. While tools like GitHub Copilot assist in code generation, they don't provide an end-to-end pipeline for automating coding tasks. Code-Pal is my take on how such a tool should function, integrating **code changes, testing, and Git automation** into a seamless workflow.

### **Assumption:**
Before using Code-Pal, ensure that you have **`gh` (GitHub CLI) and `git`** installed on your system.

---

## Project Structure

```
code-pal/
│── app/
│   ├── __init__.py
│   ├── __main__.py               # Entry point for CLI
│   ├── cli.py                    # CLI argument handling
│   ├── command_parser.py         # Natural language command interpretation
│   ├── ai_engine.py              # AI-powered code modification
│   ├── git_operations.py         # GitHub & Git operations
│   ├── task_manager.py           # Task execution system
│── pyproject.toml                # Project metadata & dependencies
│── README.md                     # Documentation
```

---

## `command.ini` File Format

Users define their commands in **natural language** inside `command.ini`. Example:

```ini
[commands]
1 = Add docstrings to all Python functions
2 = Write a test case for the module
3 = Push the code to GitHub repository
4 = Create a pull request
```

The AI will **interpret these commands** and execute the appropriate actions.

---

## Installation & Setup

### **1️⃣ Install Dependencies & Build the Package**
```sh
pip install .
```
This will install **Code-Pal** globally and make it available as a command-line tool.

### **2️⃣ Set Your OpenAI API Key**
Before using Code-Pal, set up your **OpenAI API Key**:
```sh
export OPENAI_API_KEY="your-api-key-here"
```

### **3️⃣ Run Code-Pal as a CLI**
```sh
code-pal --module sample.py --commands command.ini
```

or via Python module execution:
```sh
python -m code_pal --module sample.py --commands command.ini
```

### **4️⃣ Customize AI Settings (Optional)**
You can specify:
```sh
code-pal --module sample.py --commands command.ini --model gpt-4 --temperature 0.5
```
- **Defaults**: `gpt-4` as model, `0.7` as temperature.
- This makes **AI behavior more customizable**.

---

## Features & How It Works
✅ **Natural Language Commands** (No need to learn special syntax!)  
✅ **Automatic Docstring & Comment Addition** (Works for any language)  
✅ **Unit Test Generation**  
✅ **GitHub Automation** (Push commits & create PRs via `gh` CLI)  
✅ **Configurable AI Model & Temperature**  
✅ **Cross-Project Support** (Works in **any workspace**, whether Python, Java, or Perl)  

---

## Example Usage in a Python Project
Imagine you are inside a Python project and want to:
- Add **docstrings** to all functions.
- Generate **unit tests**.
- Push the code to GitHub.
- Create a pull request.

### **Steps:**
1. **Create a `command.ini` file** with the following:
   ```ini
   [commands]
   1 = Add docstrings to all Python functions
   2 = Write a test case for the module
   3 = Push the code to GitHub repository
   4 = Create a pull request
   ```
2. **Run the tool**:
   ```sh
   code-pal --module my_script.py --commands command.ini
   ```

