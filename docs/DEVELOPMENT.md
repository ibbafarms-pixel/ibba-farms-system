# IBBA Farms Management System - Development Guide

## Getting Started

### Prerequisites

- Python 3.9 or higher
- Node.js 16 or higher
- PostgreSQL 12 or higher
- Docker and Docker Compose (optional but recommended)
- Git

### Quick Start with Docker Compose

```bash
# Clone the repository
git clone https://github.com/ibbafarms-pixel/ibba-farms-system.git
cd ibba-farms-system

# Start all services
docker-compose up

# The app will be available at:
# Frontend: http://localhost:3000
# Backend: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

---

## Local Development Setup

### Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env

# Edit .env with your settings
DATABASE_URL=postgresql://user:password@localhost:5432/ibba_farms
SECRET_KEY=your_secret_key_here
DEBUG=true

# Run migrations
alembic upgrade head

# Start development server
uvicorn app.main:app --reload
```

### Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Create .env file
cp .env.example .env

# Edit .env with API endpoint
VITE_API_URL=http://localhost:8000/api/v1

# Start development server
npm run dev
```

---

## Project Structure

### Backend Structure

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py                 # Application entry point
│   ├── config.py               # Configuration management
│   ├── database.py             # Database connection
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── dependencies.py     # JWT and auth dependencies
│   │   ├── jwt_handler.py      # JWT token management
│   │   └── security.py         # Password hashing
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── production.py
│   │   ├── sales.py
│   │   ├── expense.py
│   │   ├── feed.py
│   │   └── base.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── production.py
│   │   ├── sales.py
│   │   ├── expense.py
│   │   ├── feed.py
│   │   └── base.py
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── production.py
│   │   ├── sales.py
│   │   ├── expenses.py
│   │   ├── feed.py
│   │   ├── dashboard.py
│   │   └── health.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── production_service.py
│   │   ├── sales_service.py
│   │   ├── expense_service.py
│   │   ├── feed_service.py
│   │   ├── calculation_service.py
│   │   └── auth_service.py
│   ├── repositories/
│   │   ├── __init__.py
│   │   ├── base_repository.py
│   │   ├── production_repository.py
│   │   ├── sales_repository.py
│   │   ├── expense_repository.py
│   │   └── feed_repository.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── exceptions.py
│   │   ├── validators.py
│   │   ├── formatters.py
│   │   └── calculations.py
│   └── middleware/
│       ├── __init__.py
│       ├── error_handler.py
│       ├── logging_middleware.py
│       └── rate_limit.py
├── migrations/              # Alembic migrations
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_auth.py
│   ├── test_production.py
│   ├── test_sales.py
│   ├── test_expenses.py
│   ├── test_feed.py
│   └── test_dashboard.py
├── requirements.txt
├── .env.example
├── Dockerfile
└── README.md
```

### Frontend Structure

```
frontend/
├── src/
│   ├── assets/              # Static assets
│   │   ├── images/
│   │   ├── fonts/
│   │   └── icons/
│   ├── components/          # Reusable components
│   │   ├── common/
│   │   │   ├── Header.jsx
│   │   │   ├── Sidebar.jsx
│   │   │   ├── Footer.jsx
│   │   │   └── Loading.jsx
│   │   ├── forms/
│   │   │   ├── ProductionForm.jsx
│   │   │   ├── SalesForm.jsx
│   │   │   ├── ExpenseForm.jsx
│   │   │   └── FeedForm.jsx
│   │   ├── charts/
│   │   │   ├── ProductionChart.jsx
│   │   │   ├── RevenueChart.jsx
│   │   │   ├── ProfitChart.jsx
│   │   │   └── FeedChart.jsx
│   │   └── tables/
│   │       ├── ProductionTable.jsx
│   │       ├── SalesTable.jsx
│   │       └── ExpenseTable.jsx
│   ├── pages/               # Page components
│   │   ├── LoginPage.jsx
│   │   ├── DashboardPage.jsx
│   │   ├── ProductionPage.jsx
│   │   ├── SalesPage.jsx
│   │   ├── ExpensePage.jsx
│   │   ├── FeedPage.jsx
│   │   ├── ReportsPage.jsx
│   │   └── NotFoundPage.jsx
│   ├── context/             # React Context
│   │   ├── AuthContext.jsx
│   │   ├── AppContext.jsx
│   │   └── NotificationContext.jsx
│   ├── hooks/               # Custom hooks
│   │   ├── useAuth.js
│   │   ├── useApi.js
│   │   ├── usePagination.js
│   │   └── useNotification.js
│   ├── services/            # API service layer
│   │   ├── api.js
│   │   ├── authService.js
│   │   ├── productionService.js
│   │   ├── salesService.js
│   │   ├── expenseService.js
│   │   ├── feedService.js
│   │   └── dashboardService.js
│   ├── styles/              # Global styles
│   │   ├── global.css
│   │   ├── variables.css
│   │   └── responsive.css
│   ├── utils/               # Utility functions
│   │   ├── formatting.js
│   │   ├── validation.js
│   │   ├── localStorage.js
│   │   └── dateUtils.js
│   ├── App.jsx
│   └── index.jsx
├── public/
│   ├── index.html
│   └── favicon.ico
├── .env.example
├── package.json
├── vite.config.js
├── Dockerfile
└── README.md
```

---

## Development Workflow

### Creating a New Feature

1. **Create a feature branch**
```bash
git checkout -b feature/feature-name
```

2. **Implement backend changes**
   - Create/update models in `app/models/`
   - Create/update schemas in `app/schemas/`
   - Create service in `app/services/`
   - Create repository in `app/repositories/`
   - Create router in `app/routers/`
   - Add tests in `tests/`

3. **Implement frontend changes**
   - Create components in `src/components/`
   - Create pages in `src/pages/`
   - Create API service in `src/services/`
   - Add styling
   - Add tests

4. **Test locally**
```bash
# Backend tests
cd backend
pytest

# Frontend tests
cd ../frontend
npm test
```

5. **Commit changes**
```bash
git add .
git commit -m "feat: add feature description"
```

6. **Push and create pull request**
```bash
git push origin feature/feature-name
```

---

## Testing

### Backend Testing

```bash
cd backend

# Run all tests
pytest

# Run specific test file
pytest tests/test_production.py

# Run with coverage
pytest --cov=app tests/

# Run in verbose mode
pytest -v
```

### Frontend Testing

```bash
cd frontend

# Run all tests
npm test

# Run tests in watch mode
npm test -- --watch

# Run with coverage
npm test -- --coverage
```

### Test File Structure

```python
# tests/test_production.py
import pytest
from app.models import Production
from app.services import ProductionService

@pytest.fixture
def production_service(db_session):
    return ProductionService(db_session)

def test_record_production_success(production_service):
    """Test successful production recording"""
    data = ProductionCreate(
        date="2026-06-26",
        house="Layer 1",
        number_of_birds=1200,
        eggs_collected=1120
    )
    
    result = production_service.record_production(data)
    
    assert result.id is not None
    assert result.production_percentage == 93.33
    assert result.good_eggs == 1120

def test_record_production_validation_error(production_service):
    """Test validation error handling"""
    data = ProductionCreate(
        date="2026-06-26",
        house="Layer 1",
        number_of_birds=1200,
        eggs_collected=1500  # More than birds!
    )
    
    with pytest.raises(ValidationError):
        production_service.record_production(data)
```

---

## Database Migrations

### Creating a Migration

```bash
cd backend

# Auto-generate migration based on model changes
alembic revision --autogenerate -m "description of changes"

# Create empty migration
alembic revision -m "description of changes"
```

### Applying Migrations

```bash
# Upgrade to latest
alembic upgrade head

# Upgrade to specific revision
alembic upgrade abc123def456

# Downgrade one revision
alembic downgrade -1

# View migration history
alembic history
```

---

## Code Style & Conventions

### Python

- Follow PEP 8
- Use type hints
- Maximum line length: 88 characters (Black formatter)
- Use meaningful variable names

```python
# Good
def calculate_production_percentage(
    eggs_collected: int,
    number_of_birds: int
) -> float:
    if number_of_birds == 0:
        return 0.0
    return (eggs_collected / number_of_birds) * 100

# Format with Black
black app/ tests/

# Lint with flake8
flake8 app/ tests/
```

### JavaScript/React

- Use ESLint configuration
- Use Prettier for formatting
- Use camelCase for variables and functions
- Use PascalCase for components
- Use descriptive names

```javascript
// Good
const calculateDailyProfit = (revenue, expenses) => {
  return revenue - expenses;
};

const ProductionChart = ({ data }) => {
  return <div>{/* Component code */}</div>;
};

// Format with Prettier
npm run format

// Lint with ESLint
npm run lint
```

---

## Debugging

### Backend Debugging

```python
# Add print statements
print(f"Debug: production_data = {production_data}")

# Use Python debugger
import pdb; pdb.set_trace()

# Use logging
import logging
logger = logging.getLogger(__name__)
logger.debug(f"Production data: {production_data}")
```

### Frontend Debugging

```javascript
// Browser console
console.log('Debug:', data);
console.error('Error:', error);
console.warn('Warning:', warning);

// React DevTools
// Install browser extension for React DevTools

// Network tab
// Check API requests in browser DevTools Network tab
```

---

## Environment Variables

### Backend .env

```
DATABASE_URL=postgresql://user:password@localhost:5432/ibba_farms
SECRET_KEY=your-secret-key-change-in-production
DEBUG=true
ALLOWED_ORIGINS=http://localhost:3000
JWT_ALGORITHM=HS256
JWT_EXPIRE_HOURS=24
LOG_LEVEL=INFO
```

### Frontend .env

```
VITE_API_URL=http://localhost:8000/api/v1
VITE_APP_NAME=IBBA Farms
VITE_DEBUG=true
```

---

## Common Tasks

### Create a new API endpoint

1. Define schema in `schemas/`
2. Create service method in `services/`
3. Create router in `routers/`
4. Add route to `main.py`
5. Add tests

### Add a database table

1. Create model in `models/`
2. Create migration: `alembic revision --autogenerate -m "add table"`
3. Run migration: `alembic upgrade head`
4. Create repository in `repositories/`
5. Create schema in `schemas/`
6. Create service in `services/`

### Add a new page to frontend

1. Create component in `pages/`
2. Create API service in `services/`
3. Add route in routing configuration
4. Add navigation link
5. Add styling

---

## Troubleshooting

### Database connection errors

```bash
# Check if PostgreSQL is running
pg_isready -h localhost

# Verify DATABASE_URL in .env
echo $DATABASE_URL

# Check database exists
psql -l
```

### Port already in use

```bash
# Find process using port 8000
lsof -i :8000

# Kill process
kill -9 <PID>

# Or use different port
uvicorn app.main:app --port 8001 --reload
```

### Module not found errors

```bash
# Ensure virtual environment is activated
source venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt

# Check PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

---

*Development Guide Version: 1.0*
*Last Updated: 2026-06-26*