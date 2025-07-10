# UV Setup for microcosm-4x

This project is now configured to use [uv](https://docs.astral.sh/uv/) for dependency management and virtual environment handling.

## Quick Start

1. **Install uv** (if not already installed):
   ```bash
   pip install uv
   ```

2. **Sync dependencies** (creates virtual environment and installs all dependencies):
   ```bash
   python -m uv sync
   ```

3. **Run the game**:
   ```bash
   python -m uv run python microcosm.py
   # or
   python -m uv run microcosm
   ```

## Development Commands

- **Add a new dependency**:
  ```bash
  python -m uv add package-name
  ```

- **Add a development dependency**:
  ```bash
  python -m uv add --dev package-name
  ```

- **Run tests**:
  ```bash
  python -m uv run python -m pytest source/tests/
  ```

- **Run linting**:
  ```bash
  python -m uv run pylint source/
  ```

- **Run any command in the virtual environment**:
  ```bash
  python -m uv run <command>
  ```

- **Show dependency tree**:
  ```bash
  python -m uv tree
  ```

## Project Configuration

The project dependencies are configured in `pyproject.toml`:

- **Main dependencies**: Required for running the game
- **Development dependencies**: Tools for development (pylint, coverage, nuitka, etc.)

## Notes

- **VLC Media Player**: The `python-vlc` dependency requires VLC Media Player to be installed on your system for audio functionality.
- **Windows Compatibility**: The project is configured for Windows development with appropriate package versions.
- **miniupnpc**: Currently disabled for Windows to avoid compilation issues. Can be re-enabled if needed.

## Troubleshooting

- If you encounter build errors, try: `python -m uv sync --reinstall`
- To see all available commands: `python -m uv --help`
- To activate the virtual environment manually: `python -m uv shell`
