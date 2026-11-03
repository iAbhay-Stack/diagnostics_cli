# 🩺 Developer Environment Diagnostics CLI

A Python command-line tool that inspects a developer's machine, checks the development environment, analyzes diagnostic event logs, and generates comprehensive health reports in both text and JSON formats.

This project was developed to demonstrate Python packaging, CLI development, testing, logging, and software engineering best practices.

---

## 📌 Features

- 🔍 Inspect machine information
  - Python version
  - Operating system
  - System architecture
  - Disk usage
  - Current working directory

- 🌍 Inspect environment variables
  - PATH
  - HOME
  - USER / USERNAME
  - Virtual environment detection

- 🛠 Detect installed developer tools
  - Git
  - Python
  - Pip
  - Docker
  - Node.js
  - npm
  - Visual Studio Code

- 📊 Analyze diagnostic event logs
  - Total events
  - Error count
  - Warning count
  - Failed requests
  - Average latency
  - Highest latency
  - Service-wise statistics

- 📄 Generate reports
  - Human-readable text report
  - JSON report

- 💾 Save reports to a file

- ⚠ Return meaningful exit codes

- ✅ Unit tested using Pytest

- ✨ Code quality enforced with Ruff

---

# 📂 Project Structure

```text
diagnostic_cli/
│
├── sample_data/
│   └── diagnostic-events.json
│
├── src/
│   └── diagnostics/
│       ├── __init__.py
│       ├── __main__.py
│       ├── checks.py
│       ├── cli.py
│       ├── constants.py
│       ├── events.py
│       ├── inspector.py
│       ├── logger.py
│       ├── models.py
│       ├── report.py
│       └── version.py
│
├── tests/
│
├── pyproject.toml
├── README.md
├── LICENSE
└── .gitignore
```

---

# ⚙ Requirements

- Python 3.10+
- pip

---

# 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/iAbhay-Stack/diagnostics_cli.git
cd diagnostic-cli
```

Install the project in editable mode:

```bash
pip install -e .
```

---

# 💻 Usage

### Generate a diagnostics report

```bash
diagnostics
```

---

### Generate a JSON report

```bash
diagnostics --json
```

---

### Analyze an event log

```bash
diagnostics --events sample_data/diagnostic-events.json
```

---

### Save report to a file

```bash
diagnostics --output report.txt
```

---

### Save JSON report

```bash
diagnostics --json --output report.json
```

---

### Display version

```bash
diagnostics --version
```

---

# 📊 Example Output

```text
============================================================
Developer Environment Diagnostics
============================================================

Machine Information
------------------------------
Python Version      : 3.14
Operating System    : Windows
Architecture        : AMD64

Environment Variables
------------------------------
PATH                : Present
HOME                : Present

Developer Tools
------------------------------
Git                 : Installed
Docker              : Installed
Node                : Installed

Event Analysis
------------------------------
Total Events        : 5
Errors              : 2
Warnings            : 1
Average Latency     : 620.50 ms

============================================================
Overall Health

Status : WARNING
```

---

# 🧪 Running Tests

Run all unit tests:

```bash
pytest
```

Generate a coverage report:

```bash
pytest --cov=diagnostics
```

---

# 🧹 Code Quality

Run Ruff checks:

```bash
ruff check .
```

Automatically fix issues:

```bash
ruff check . --fix
```

Format the project:

```bash
ruff format .
```

---

# 🏗 Technologies Used

- Python
- argparse
- dataclasses
- JSON
- logging
- pathlib
- shutil
- pytest
- pytest-cov
- Ruff

---

# 📦 Build Package

Build a distributable package:

```bash
python -m build
```

This creates:

```
dist/
├── diagnostics_cli-1.0.0-py3-none-any.whl
└── diagnostics_cli-1.0.0.tar.gz
```

Install the generated wheel:

```bash
pip install dist/diagnostics_cli-1.0.0-py3-none-any.whl
```

---

# 🎯 Learning Outcomes

This project demonstrates:

- Python package development
- Modular application architecture
- Command-line interface design
- Environment inspection
- Log analysis
- JSON serialization
- Unit testing
- Code quality and linting
- Error handling
- Python packaging and distribution

---

# 📈 Future Improvements

Potential enhancements include:

- Configuration file support
- Plugin system for custom checks
- HTML report generation
- Rich terminal UI
- Docker support
- GitHub Actions for CI/CD
- Publish to PyPI

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**iAbhay-Stack**

MCA Student | Python Developer | Passionate about Software Development

If you found this project interesting, feel free to ⭐ the repository and share your feedback!