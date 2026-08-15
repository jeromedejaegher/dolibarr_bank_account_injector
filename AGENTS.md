# Project AGENTS.md

## Project Overview
- **Description**: Streamlit web application to securely inject bank statements using the Dolibarr API. Allows users to upload Excel bank statements and sync them with Dolibarr bank accounts.
- **Primary Language**: Python 3.12+
- **Framework**: Streamlit
- **Architecture**: Single-file Streamlit web application with REST API integration (Dolibarr)
- **Key Dependencies**: python-dotenv, streamlit, loguru, numpy, pandas, openpyxl, requests

## Commands

### Installation
```bash
# Create virtual environment and install
uv venv
source .venv/bin/activate  # Linux/Mac
.\.venv\Scripts\activate   # Windows

# Install package in development mode
uv pip install -e .
```

### Building
```bash
# No build step required for Streamlit apps
# To create a distributable package:
pip wheel --no-deps .
```

### Testing
```bash
# No formal test suite defined yet
# To run the app for manual testing:
streamlit run dolibarr_injector.py
```

### Linting
```bash
# Recommended: Use ruff or flake8
ruff check .
# or
flake8 .
```

### Deployment
```bash
# Run the Streamlit application
streamlit run dolibarr_injector.py

# Or use the convenience scripts (when available)
account_injector.sh    # Linux
account_injector.bat  # Windows
```

## Code Style & Conventions
- **Naming Conventions**: snake_case for variables and functions, PascalCase for classes (PEP 8)
- **Import Order**: Standard library, third-party, local (grouped, alphabetical within groups)
- **Formatting**: 4-space indentation, double quotes for strings, no trailing commas in single-line constructs
- **Type Annotations**: Use Python type hints where beneficial for clarity
- **Comment Style**: Inline comments for non-obvious logic, docstrings for public functions
- **File Organization**: Single main module (dolibarr_injector.py) with helper functions

## Directory Structure
```
dolibarr_bank_account_injector/
├── dolibarr_injector.py    # Main Streamlit application
├── pyproject.toml          # Project metadata and dependencies
├── README.md               # Project documentation
├── LICENSE                 # GNU GPL v3 license
├── .gitignore              # Git ignore patterns
├── .env                    # Environment variables (API_URL, DOLAPIKEY) - NOT COMMITTED
└── .vibe/                  # Vibe configuration
    └── project_knowledge.md # Project knowledge base
```

## Boundaries & Security
- **Prohibitions**: 
  - Never commit `.env` file containing API_URL or DOLAPIKEY
  - Never push directly to main branch
  - Never hardcode Dolibarr API keys in source code
  - Always use environment variables for sensitive configuration
  - Never expose `.env` or secrets in logs or error messages
- **Approval Workflows**: 
  - Code review required for all pull requests
  - Security review required for any authentication/authorization changes
  - Manual testing required before merging API-related changes
- **Architectural Constraints**:
  - All Dolibarr API calls must go through the central API endpoint
  - API keys must be loaded from environment variables via python-dotenv
  - No direct database access - only through Dolibarr REST API
  - Excel uploads are validated before processing

## Testing Guidelines
- **Running Tests**: Currently manual testing via Streamlit interface
- **Test Structure**: N/A - no formal test framework configured
- **Mocking Strategy**: Mock Dolibarr API responses for future unit tests
- **Test Coverage Requirements**: Aim for 80%+ coverage when test suite is established
- **Adding New Tests**: Place in `tests/` directory with pytest naming convention
- **Test Data**: Use sample Excel files for bank statement testing
