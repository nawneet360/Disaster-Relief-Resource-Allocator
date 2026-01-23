# Contributing to Disaster Relief Resource Allocator

Thank you for your interest in contributing to the Disaster Relief Resource Allocator! This document provides guidelines and instructions for contributing.

## Code of Conduct

By participating in this project, you agree to maintain a respectful, inclusive, and collaborative environment for all contributors.

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue with:
- Clear description of the bug
- Steps to reproduce
- Expected vs actual behavior
- Your environment (OS, Python version, etc.)
- Relevant logs or screenshots

### Suggesting Features

We welcome feature suggestions! Please create an issue with:
- Clear description of the feature
- Use case and benefits
- Potential implementation approach (if you have ideas)

### Pull Requests

1. **Fork the repository** and create a new branch from `main`
2. **Make your changes** following our coding standards
3. **Add tests** for any new functionality
4. **Update documentation** as needed
5. **Run tests** to ensure everything passes
6. **Submit a pull request** with a clear description

## Development Guidelines

### Code Style

- Follow PEP 8 guidelines for Python code
- Use meaningful variable and function names
- Add docstrings to all classes and functions
- Keep functions focused and single-purpose
- Comment complex logic

### Testing

- Write unit tests for all new features
- Maintain or improve test coverage
- Ensure all tests pass before submitting PR
- Use pytest for testing

### Documentation

- Update README.md for user-facing changes
- Add docstrings following Google/NumPy style
- Include code examples where appropriate
- Keep documentation clear and concise

## Development Setup

1. Fork and clone the repository:
```bash
git clone https://github.com/YOUR-USERNAME/Disaster-Relief-Resource-Allocator.git
cd Disaster-Relief-Resource-Allocator
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run tests:
```bash
pytest tests/
```

## Commit Messages

Write clear, descriptive commit messages:
- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")
- First line should be concise (50 chars or less)
- Provide additional details in the body if needed

Example:
```
Add water resource tracking feature

- Implement water quantity monitoring
- Add tests for water allocation
- Update documentation with water examples
```

## Review Process

1. Maintainers will review your PR within a few days
2. Address any feedback or requested changes
3. Once approved, your PR will be merged
4. Your contribution will be acknowledged in the release notes

## Questions?

Feel free to open an issue for any questions about contributing.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

Thank you for helping improve disaster relief efforts! 🙏
