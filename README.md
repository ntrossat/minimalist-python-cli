# Minimalist Python CLI
Minimalist Python CLI tool using [click](https://click.palletsprojects.com/en/stable/) and [uv](https://docs.astral.sh/uv/).

## Installation
```bash
# Clone the repository
git clone git@github.com:ntrossat/minimalist-python-cli.git
cd minimalist-python-cli

# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install the Python dependencies
uv sync
```

## Usage
```bash
# Run the CLI
uv run hello-world --help

# Run the CLI in the virtual environment
source .venv/bin/activate
hello-world --help
```

