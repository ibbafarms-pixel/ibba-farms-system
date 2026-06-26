# IBBA Farms Management System - Setup Guide

## Quick Start with Docker Compose

The easiest way to get the entire system running is with Docker Compose.

### Prerequisites

- Docker
- Docker Compose
- Git

### Steps

1. **Clone the repository**
```bash
git clone https://github.com/ibbafarms-pixel/ibba-farms-system.git
cd ibba-farms-system
```

2. **Start all services**
```bash
docker-compose up
```

This will start:
- PostgreSQL database on `localhost:5432`
- Redis cache on `localhost:6379`
- FastAPI backend on `http://localhost:8000`
- React frontend on `http://localhost:5173`

3. **Access the application**

- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **Alternative API Docs**: http://localhost:8000/redoc

### Stop the services

```bash
docker-compose down
```

### View logs

```bash
# All services
docker-compose logs -f

# Specific service
docker-compose logs -f backend
docker-compose logs -f frontend
```

---

## Local Development Setup

If you prefer to run services locally without Docker:

### Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env

# Edit .env with your database URL
# DATABASE_URL=postgresql://ibba_user:ibba_password@localhost:5432/ibba_farms

# Run migrations
alembic upgrade head

# Start development server
uvicorn app.main:app --reload
```

The backend will be available at `http://localhost:8000`

### Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Create .env file
cp .env.example .env

# Start development server
npm run dev
```

The frontend will be available at `http://localhost:5173`

---

## Database Setup

### PostgreSQL Installation

**macOS:**
```bash
brew install postgresql@15
brew services start postgresql@15
```

**Ubuntu/Debian:**
```bash
sudo apt-get install postgresql postgresql-contrib
sudo systemctl start postgresql
```

**Windows:**
Download from https://www.postgresql.org/download/windows/

### Create Database

```bash
# Connect to PostgreSQL
psql -U postgres

# Create user
CREATE USER ibba_user WITH PASSWORD 'ibba_password';

# Create database
CREATE DATABASE ibba_farms OWNER ibba_user;

# Grant privileges
GRANT ALL PRIVILEGES ON DATABASE ibba_farms TO ibba_user;

# Exit
\q
```

---

## Initial User Setup

Once the application is running:

1. Access the backend container/shell:
```bash
docker-compose exec backend bash
# or if running locally
cd backend
```

2. Create admin user via Python script:
```python
# backend/create_admin.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import User, UserRole
from app.auth.security import hash_password
from app.database import Base

# This will be implemented in Phase 1
```

For now, use the login page with test credentials (to be implemented).

---

## Testing

### Backend Tests

```bash
cd backend
pytest
```

### Frontend Tests

```bash
cd frontend
npm test
```

---

## Development Workflow

### Making Changes

1. Create a feature branch:
```bash
git checkout -b feature/your-feature-name
```

2. Make your changes in either `backend/` or `frontend/` directories

3. Commit with descriptive messages:
```bash
git commit -m "feat: add feature description"
git commit -m "fix: bug description"
git commit -m "docs: documentation update"
```

4. Push and create a pull request:
```bash
git push origin feature/your-feature-name
```

### Code Quality

**Backend:**
```bash
cd backend
black app/  # Format code
flake8 app/  # Lint code
isort app/  # Sort imports
```

**Frontend:**
```bash
cd frontend
npm run format  # Format code
npm run lint  # Lint code
```

---

## Environment Variables

### Backend (.env)

See `backend/.env.example` for all available options.

Key variables:
- `DATABASE_URL`: PostgreSQL connection string
- `SECRET_KEY`: JWT signing key (change in production)
- `DEBUG`: Enable debug mode
- `ALLOWED_ORIGINS`: CORS allowed origins

### Frontend (.env)

See `frontend/.env.example` for all available options.

Key variables:
- `VITE_API_URL`: Backend API URL
- `VITE_DEBUG`: Enable debug mode

---

## Troubleshooting

### Port Already in Use

```bash
# Find process using port
lsof -i :8000  # Backend
lsof -i :5173  # Frontend
lsof -i :5432  # Database

# Kill process
kill -9 <PID>
```

### Database Connection Error

1. Ensure PostgreSQL is running
2. Check database URL in `.env`
3. Verify credentials
4. Test connection:
```bash
psql postgresql://ibba_user:ibba_password@localhost:5432/ibba_farms
```

### Docker Issues

```bash
# Rebuild containers
docker-compose build --no-cache

# Remove all containers and volumes
docker-compose down -v

# Start fresh
docker-compose up
```

### npm or pip Package Issues

```bash
# Clear package caches
npm cache clean --force
rm -rf node_modules package-lock.json
npm install

# For Python
rm -rf backend/venv
python -m venv backend/venv
source backend/venv/bin/activate
pip install -r backend/requirements.txt
```

---

## Next Steps

1. **Read the documentation**:
   - [API Specification](docs/API_SPEC.md)
   - [Database Schema](docs/DATABASE_SCHEMA.md)
   - [Architecture](docs/ARCHITECTURE.md)
   - [Development Guide](docs/DEVELOPMENT.md)

2. **Start developing**:
   - Pick a feature from the [Roadmap](ROADMAP.md)
   - Create a feature branch
   - Implement and test
   - Submit a pull request

3. **Review code standards**:
   - Python: Follow PEP 8 with Black formatter
   - JavaScript: Use ESLint and Prettier
   - Both: Add tests for new features

---

## Support

For issues or questions:
1. Check existing GitHub issues
2. Review the documentation
3. Create a new GitHub issue with detailed description

---

*Last Updated: 2026-06-26*
