# ING3513 - Introduction to artificial intelligence and machine learning

Lab material for [ING3513](https://www.forsvaret.no/utdanning/emner/ING3513).

## Setup Instructions

### Prerequisites

Before starting, ensure you have:

- A GitHub account
- Access to the `ing3513/course-materials` repository

### Installation Steps

1. **Install WSL (Windows Subsystem for Linux)**
   - Open PowerShell as Administrator
   - Run: `wsl --install`
   - Restart your computer when prompted

2. **Install Visual Studio Code**
   - Download from [https://code.visualstudio.com/](https://code.visualstudio.com/)
   - Run the installer and follow the setup wizard

3. **Install WSL Extension**
   - Download from [https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl)
   - Or in VS Code: Go to Extensions (Ctrl+Shift+X), search for "WSL" and install the official Microsoft WSL extension

4. **Connect to WSL**
   - Press F1 to open the Command Palette
   - Type and select: `WSL: Connect to WSL`
   - VS Code will reopen in your Linux home directory (~ or /home/<username>)

5. **Login with GitHub**
   - Open the Accounts menu in VS Code (bottom left corner)
   - Select "Sign in with GitHub"
   - Follow the authentication process

6. **Clone Repository**
   - Open the Source Control view (Ctrl+Shift+G)
   - Click "Clone Repository" or press F1 and type `Git: Clone`
   - Enter the repository URL: `https://github.com/ing3513/course-materials.git`
   - Select a folder location and open the cloned repository

7. **Install Recommended Extensions**
   - When you open the repository, VS Code will prompt you to install recommended extensions
   - Click "Install" to automatically install Python, Jupyter, and WSL extensions
   - Alternatively, you can manually install them from the Extensions view (Ctrl+Shift+X)

8. **Setup Python Environment**
   - Open a terminal in VS Code (Ctrl+`)
   - Run the setup script: `./scripts/setupPythonEnvironment.sh`
   - This will install uv, Python 3.13, and all project dependencies
   - If this is your first run, restart your terminal or run: `source ~/.bashrc`

9. **Verify Installation**
   - Open `labs/lab00/lab00.ipynb` in VS Code
   - Click "Select Kernel" in the top right corner of the notebook
   - Choose "Python Environments..." and select the `ing3513` environment
   - Run the verification cell (click the play button or press Shift+Enter)
   - You should see pandas version information and a success message

**Congratulations! You are now set up and ready to work with Jupyter notebooks in this course.**

## About the Python Environment

This course uses [uv](https://docs.astral.sh/uv/), a modern Python package and project manager. uv is significantly faster than pip and provides better dependency resolution.

### Key Features

- Automatic Python version management
- Fast dependency resolution and installation
- Reproducible environments via lockfiles
- All-in-one tool replacing pip, venv, and virtualenv

### Common Commands

- `uv run <command>` - Run a command in the project's virtual environment
- `uv add <package>` - Add a new dependency
- `uv sync --locked` - Sync dependencies from lockfile (use `--locked` to ensure exact versions match)
- `uv python install` - Install Python versions

## Code Formatting and Linting

This project uses [Ruff](https://docs.astral.sh/ruff/) for code formatting and linting. Ruff is an extremely fast Python linter and formatter.

### Automatic Formatting

VS Code is configured to automatically format your code on save, both in Python files and Jupyter notebooks. This includes:

- Code formatting (consistent style)
- Import sorting
- Auto-fixing common issues

### Manual Commands

If you need to run formatting or linting manually:

- `uv run ruff format .` - Format all Python files
- `uv run ruff check .` - Check for linting issues
- `uv run ruff check --fix .` - Auto-fix linting issues where possible
