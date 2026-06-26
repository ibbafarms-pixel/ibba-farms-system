# Contributing to IBBA Farms Management System

## Code of Conduct

Be respectful, inclusive, and professional in all interactions.

## How to Contribute

### 1. Fork and Clone

```bash
fork the repository on GitHub
git clone https://github.com/YOUR_USERNAME/ibba-farms-system.git
cd ibba-farms-system
git remote add upstream https://github.com/ibbafarms-pixel/ibba-farms-system.git
```

### 2. Create Feature Branch

```bash
git checkout -b feature/your-feature-name
```

### 3. Make Changes

- Follow the code style guidelines
- Add tests for new features
- Update documentation
- Keep commits focused and descriptive

### 4. Commit Messages

Use conventional commits:

```
feat: add new feature
fix: fix bug in module
docs: update documentation
test: add unit tests
refactor: refactor code structure
style: format code
chore: update dependencies
```

### 5. Push and Create Pull Request

```bash
git push origin feature/your-feature-name
```

Then create a pull request on GitHub with:
- Clear title and description
- Reference to any related issues
- Testing instructions

### 6. Code Review

- Address feedback from reviewers
- Make requested changes
- Re-request review when ready

### 7. Merge

Once approved, your changes will be merged to the main branch.

---

## Development Guidelines

### Backend (Python/FastAPI)

- **Style Guide**: PEP 8 (enforced by Black)
- **Type Hints**: Use type hints for all functions
- **Docstrings**: Google-style docstrings
- **Tests**: Pytest with >80% coverage goal
- **Linting**: Flake8 and isort

### Frontend (React/JavaScript)

- **Style Guide**: Airbnb JavaScript Style Guide
- **Components**: Functional components with hooks
- **Testing**: Vitest and React Testing Library
- **Formatting**: Prettier for consistent style
- **Linting**: ESLint

### Database

- **Migrations**: Use Alembic for schema changes
- **Version Control**: Always create migration file for schema changes
- **Testing**: Test with actual database in tests

---

## Testing Requirements

### Backend

```bash
# Run tests
pytest

# With coverage
pytest --cov=app

# Specific test file
pytest tests/test_production.py
```

**Coverage Goal**: >80%

### Frontend

```bash
# Run tests
npm test

# With coverage
npm test -- --coverage
```

**Coverage Goal**: >75%

---

## Documentation

- Update relevant documentation files when making changes
- Keep README.md current
- Document new API endpoints
- Add comments for complex logic
- Update ROADMAP.md for significant changes

---

## Project Structure

Familiarize yourself with:

- `backend/app/models/` - Database models
- `backend/app/services/` - Business logic
- `backend/app/routers/` - API endpoints
- `frontend/src/pages/` - Page components
- `frontend/src/components/` - Reusable components
- `frontend/src/services/` - API client services

---

## Common Tasks

### Add a New API Endpoint

1. Create schema in `backend/app/schemas/`
2. Create service method in `backend/app/services/`
3. Create router in `backend/app/routers/`
4. Add tests in `backend/tests/`
5. Update API documentation

### Add a New Database Table

1. Create model in `backend/app/models/`
2. Create migration: `alembic revision --autogenerate -m "description"`
3. Create repository in `backend/app/repositories/`
4. Create schema in `backend/app/schemas/`
5. Create service in `backend/app/services/`

### Add a New Frontend Page

1. Create page component in `frontend/src/pages/`
2. Create API service in `frontend/src/services/`
3. Add route in `frontend/src/App.jsx`
4. Add navigation link in sidebar
5. Add styling and tests

---

## Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Documentation](https://react.dev/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Project Roadmap](ROADMAP.md)
- [Architecture Guide](docs/ARCHITECTURE.md)

---

*Last Updated: 2026-06-26*
