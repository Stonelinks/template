# Project Template

My personal project template, flexible but mainly for Python and TypeScript projects with full formatting, type safety, environment isolation, and dependency management.

## Features

- **Multi-language support**: Python and TypeScript in a single project. Golang is installed too, but its just used for mvdan.cc/sh/v3/cmd/shfmt
- **Type safety**: Pyright for Python, Bun / TypeScript with strict settings
- **Environment isolation**: No actual need for virtualenvs. `direnv` / `env.sh` sets up a dedicated, scoped directory for the project in your home folder for all dependencies and modifies $PATH for you to use them. Adding support for new languages is pretty easy, just add a shell script for it in `/bin`.
- **Dependency management**: `uv` / requirements.txt for Python, `node` and `bun` for TypeScript (try to use `bun` where possible). Consume random 3rd party repos in an efficient, structured way via the `update-3rdparty-deps` script.
- **Code formatting / Linting**: Combined into one step, check out the `format-*` scripts.
- **Cross-platform support**: macOS and Linux, any arch

## Project Structure

```
.
├── bin/               # Build and setup scripts
├── mc/                # Example python source code
├── ts/                # Example typeScript source code
├── typings/           # Generated python type definitions
├── .envrc / env.sh    # Environment configuration
```

## Getting Started

### Prerequisites

- macOS or Linux
- Bash shell
- Git
- direnv

### Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/project-template.git
   cd project-template
   ```

2. **Set up the environment:**

   ```bash
   direnv allow
   setup-local
   ```

   This script will:
   - Install Python, Node.js, and Go
   - Set up virtual environments
   - Install dependencies

3. **(Optional) Create a `secrets.sh` file:**

   Create a `secrets.sh` file in the root directory and keep any secrets in there

### Usage

#### Development

- **Run Python code:**

  ```bash
  python mc/hello.py
  ```

  By default this will run python formatters / typecheckers before running the script. If you want to skip this, just run `python3` directly

- **Run TypeScript code:**

  ```bash
  bun run ts/main.ts
  ```

- **Format code:**

  ```bash
  format
  ```

  This runs all formatters and linters

- **Format code:**

  ```bash
  setup-local
  ```

  This will install everything needed to run the project
  
