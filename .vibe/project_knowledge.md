# Project Knowledge Base

## Architecture Decisions

### Major Architectural Choices

- **Decision**: Use Streamlit as the web framework
  - **Rationale**: Streamlit provides rapid development for data-focused web applications with built-in UI components. Perfect for a bank statement injection tool that needs file upload and data display capabilities.
  - **Alternatives Considered**: Flask, FastAPI, Django
  - **Date**: 2026
  - **Status**: Active

- **Decision**: Direct Dolibarr REST API integration
  - **Rationale**: Dolibarr provides a comprehensive REST API that exposes bank account and transaction data. Direct integration is simpler than using a client library.
  - **Alternatives Considered**: Custom Dolibarr Python SDK, SQL direct access
  - **Date**: 2026
  - **Status**: Active

- **Decision**: Environment variables for configuration
  - **Rationale**: Using python-dotenv with `.env` files keeps API keys and server URLs out of version control, following security best practices.
  - **Alternatives Considered**: Config files, command-line arguments
  - **Date**: 2026
  - **Status**: Active

- **Decision**: Excel file upload for bank statements
  - **Rationale**: Excel (.xlsx) is the most common format for bank statements from financial institutions. openpyxl provides robust parsing.
  - **Alternatives Considered**: CSV, PDF parsing, OFX format
  - **Date**: 2026
  - **Status**: Active

### Patterns in Use

- **Pattern Name**: Session state for API configuration
  - **Description**: Using Streamlit's `st.session_state` to store API URL and key across page interactions
  - **Benefits**: Persists configuration between user interactions without requiring re-entry
  - **Examples**: `dolibarr_injector.py:53-54`

- **Pattern Name**: Centralized header generation
  - **Description**: `get_header()` function creates consistent HTTP headers with API key
  - **Benefits**: DRY principle, single place to update header format
  - **Examples**: `dolibarr_injector.py:11-15`

- **Pattern Name**: Logging with loguru
  - **Description**: Comprehensive logging for debugging and audit purposes
  - **Benefits**: Easy debugging, persistent logs, structured output
  - **Examples**: Throughout `dolibarr_injector.py`

### Anti-Patterns to Avoid

- **Anti-Pattern**: Hardcoding API endpoints as strings throughout the code
  - **Reason**: Makes maintenance difficult if API changes; violates DRY
  - **Better Alternative**: Centralize API base URL in configuration/environment

- **Anti-Pattern**: Storing API keys in source code
  - **Reason**: Security risk, exposes credentials in version control
  - **Better Alternative**: Always use environment variables with `.env` files in `.gitignore`

- **Anti-Pattern**: Not validating uploaded Excel files
  - **Reason**: Could lead to errors or security issues with malformed files
  - **Better Alternative**: Validate file structure before processing

## Test Coverage
- **Overall Coverage**: 0% (no tests currently defined)
- **Coverage by Module**: 
  - `dolibarr_injector.py`: 0% (no unit tests)
  - API integration: 0% (no integration tests)
- **Coverage Gaps**: Entire codebase lacks test coverage
- **Coverage Tools**: pytest recommended (compatible with Python 3.12+)
- **How to Check**: `pytest --cov=dolibarr_injector --cov-report=term`

## Important Patterns

### Design Patterns
- **Repository Pattern**: Implicit in API data fetching (get_all_accounts, get_all_lines)
- **Factory Pattern**: Header creation via get_header() function
- **MVC-like**: Streamlit handles View/Controller, API provides Model

### Coding Patterns
- **Functional Decomposition**: Small, focused functions (get_header, get_all_accounts, get_all_lines)
- **Error Logging**: Consistent error logging before user-facing messages
- **Environment-first**: Always load .env at startup before any API calls

### File Organization Patterns
- **Single-module**: All code in one file (appropriate for small Streamlit apps)
- **Flat structure**: No nested directories (simple project)

## Errors to Avoid

### Common Mistakes
- **Missing .env file**: Application fails silently or shows confusing errors
  - **Solution**: Check for .env existence at startup and show clear error message
- **Incorrect API URL format**: Missing http:// or https:// prefix
  - **Solution**: Validate URL format before making requests
- **API key not accepted**: Dolibarr API key may have expired or wrong permissions
  - **Solution**: Verify DOLAPIKEY has correct permissions in Dolibarr admin

### Pitfalls
- **Streamlit session state**: Session state resets on script reload - don't store critical data only in session state
- **Excel parsing**: Different banks format Excel differently - column names may vary
- **API rate limiting**: Dolibarr may have rate limits on API calls

### Performance Traps
- **Unbounded API calls**: Fetching all lines without pagination for accounts with many transactions
- **Large Excel files**: Loading very large Excel files into memory without chunking
- **No caching**: Repeatedly fetching the same account data without caching

### Security Issues
- **Secrets in logs**: loguru may log sensitive data from API responses
  - **Mitigation**: Filter sensitive fields before logging
- **API key exposure**: Browser JavaScript could potentially access session state
  - **Mitigation**: Streamlit runs server-side, but still be cautious
- **No input sanitization**: Excel uploads could contain malicious content
  - **Mitigation**: Validate and sanitize all uploaded data

## Useful Commands & Tips

### Debugging
```bash
# Run with verbose logging
streamlit run dolibarr_injector.py --logger.level=debug

# Check installed dependencies
uv pip list

# Verify .env is loaded
python -c "from dotenv import load_dotenv; import os; load_dotenv(); print('API_URL:', os.getenv('API_URL')); print('DOLAPIKEY:', os.getenv('DOLAPIKEY', 'NOT SET'))"
```

### Profiling
```bash
# Profile the application
python -m cProfile -s cumulative dolibarr_injector.py
```

### Logging
- Streamlit logs appear in the terminal where the app is running
- loguru logs are also captured by Streamlit's logging system
- Use `logger.info()`, `logger.error()`, etc. for application-level logging

### Environment Setup
```bash
# Create fresh environment
rm -rf .venv
uv venv
source .venv/bin/activate
uv pip install -e .

# Update dependencies
uv pip install --upgrade package-name
```

## External Resources

### Documentation
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Dolibarr API Documentation](https://wiki.dolibarr.org/index.php/Module_REST_API)
- [python-dotenv Documentation](https://saurabh-kumar.com/python-dotenv/)
- [loguru Documentation](https://github.com/Delgan/loguru)
- [pandas Documentation](https://pandas.pydata.org/docs/)

### Tutorials
- [Streamlit File Upload](https://docs.streamlit.io/library/api-reference/widgets/st.file_uploader)
- [Dolibarr REST API Examples](https://www.dolibarr.org/forum/)
- [Building Streamlit Apps with APIs](https://blog.streamlit.io/)

### Community
- [Streamlit Community Forum](https://discuss.streamlit.io/)
- [Dolibarr Forum](https://www.dolibarr.org/forum/)
- [Dolibarr GitHub](https://github.com/Dolibarr/dolibarr)
