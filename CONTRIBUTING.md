# Contributing Guidelines

## Getting Started

1. Fork the repository
2. Clone your fork
3. Create a feature branch: `git checkout -b feature/amazing-feature`
4. Make your changes
5. Commit: `git commit -m 'Add amazing feature'`
6. Push: `git push origin feature/amazing-feature`
7. Open a Pull Request

## Code Standards

### Backend (Python)
- Use black for formatting
- Use flake8 for linting
- Use mypy for type checking
- Write docstrings for all functions
- Target 80% code coverage

### Frontend (TypeScript/React)
- Use ESLint for linting
- Use Prettier for formatting
- Component-based architecture
- Proper TypeScript typing
- Unit tests for utilities

## Testing

### Backend
```bash
cd backend
pytest tests/ -v --cov=app
```

### Frontend
```bash
cd frontend
npm test
```

## Commit Messages

Use conventional commits:
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation
- `style:` Formatting
- `refactor:` Code restructuring
- `test:` Test additions
- `chore:` Maintenance

Example: `feat: Add user profile page`

## Pull Request Process

1. Update documentation
2. Add/update tests
3. Ensure all tests pass
4. Update CHANGELOG
5. Get code review approval
6. Squash and merge

## Reporting Issues

Include:
- Detailed description
- Steps to reproduce
- Expected vs actual behavior
- Environment details
- Screenshots/logs if applicable

## License

MIT License - see LICENSE file
