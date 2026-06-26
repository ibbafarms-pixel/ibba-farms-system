# IBBA Farms Management System - Architecture

## System Architecture Overview

This document describes the high-level architecture, design patterns, and technology stack for the IBBA Farms Management System.

---

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    Client Layer                              │
│  ┌──────────────────┐              ┌──────────────────┐    │
│  │  Web Browser     │              │  Mobile Browser  │    │
│  │  (React App)     │              │  (Responsive UI) │    │
│  └────────┬─────────┘              └────────┬─────────┘    │
└───────────┼──────────────────────────────────┼──────────────┘
            │ HTTPS/REST                       │
┌───────────┼──────────────────────────────────┼──────────────┐
│           │      API Gateway / Load Balancer │              │
│           │      (Nginx)                     │              │
│           └───────────┬──────────────────────┘              │
│                       │                                      │
│        Application Layer (FastAPI)                           │
│  ┌────────────────────┴─────────────────────┐              │
│  │                                           │              │
│  │  ┌─────────────────────────────────────┐ │              │
│  │  │  Routes & Middleware                │ │              │
│  │  │  - Authentication                   │ │              │
│  │  │  - Request validation               │ │              │
│  │  │  - Rate limiting                    │ │              │
│  │  │  - CORS                             │ │              │
│  │  └─────────────────────────────────────┘ │              │
│  │                                           │              │
│  │  ┌─────────────────────────────────────┐ │              │
│  │  │  API Routes                         │ │              │
│  │  │  - /auth                            │ │              │
│  │  │  - /production                      │ │              │
│  │  │  - /sales                           │ │              │
│  │  │  - /expenses                        │ │              │
│  │  │  - /feed                            │ │              │
│  │  │  - /dashboard                       │ │              │
│  │  └─────────────────────────────────────┘ │              │
│  │                                           │              │
│  │  ┌─────────────────────────────────────┐ │              │
│  │  │  Service Layer (Business Logic)     │ │              │
│  │  │  - ProductionService                │ │              │
│  │  │  - SalesService                     │ │              │
│  │  │  - ExpenseService                   │ │              │
│  │  │  - FeedService                      │ │              │
│  │  │  - CalculationService               │ │              │
│  │  │  - ReportService                    │ │              │
│  │  └─────────────────────────────────────┘ │              │
│  │                                           │              │
│  │  ┌─────────────────────────────────────┐ │              │
│  │  │  Data Access Layer (SQLAlchemy ORM)│ │              │
│  │  │  - Models                           │ │              │
│  │  │  - Schemas                          │ │              │
│  │  │  - Repositories                     │ │              │
│  │  └─────────────────────────────────────┘ │              │
│  │                                           │              │
│  └───────────────────────────────────────────┘              │
└──────────────────────┬───────────────────────────────────────┘
                       │ SQL/TCP
┌──────────────────────┴───────────────────────────────────────┐
│                    Data Layer                                │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  PostgreSQL Database                                │  │
│  │  - production_records                               │  │
│  │  - sales_records                                    │  │
│  │  - expense_records                                  │  │
│  │  - feed_inventory                                   │  │
│  │  - users                                            │  │
│  │  - customers                                        │  │
│  │  - suppliers                                        │  │
│  │  - audit_logs                                       │  │
│  └──────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Redis Cache (Optional)                             │  │
│  │  - Session management                               │  │
│  │  - Query result caching                             │  │
│  │  - Rate limit counters                              │  │
│  └──────────────────────────────────────────────────────┘  │
└───────────────────────────────────────────────────────────────┘
```

---

## Technology Stack

### Frontend
- **Framework**: React 18+
- **State Management**: Context API or Redux
- **HTTP Client**: Axios
- **Styling**: Tailwind CSS
- **UI Components**: Shadcn/ui or Material-UI
- **Charts**: Chart.js or Recharts
- **Form Handling**: React Hook Form
- **Date Handling**: date-fns
- **Build Tool**: Vite
- **Testing**: Vitest, React Testing Library

### Backend
- **Framework**: FastAPI 0.95+
- **Python Version**: 3.9+
- **ORM**: SQLAlchemy 2.0+
- **Database**: PostgreSQL 12+
- **Async Support**: Uvicorn
- **Authentication**: JWT (PyJWT)
- **Password Hashing**: Bcrypt
- **Data Validation**: Pydantic v2
- **API Documentation**: Swagger/OpenAPI
- **Testing**: pytest, pytest-asyncio
- **Logging**: Python logging, structlog

### Infrastructure
- **Containerization**: Docker
- **Orchestration**: Docker Compose (development), Kubernetes (production)
- **Web Server**: Nginx
- **Reverse Proxy**: Nginx
- **Caching**: Redis (optional)
- **Message Queue**: Celery (future for async tasks)
- **CI/CD**: GitHub Actions
- **Hosting**: AWS, Google Cloud, or self-hosted

---

## Design Patterns

### 1. Layered Architecture

```
Presentation Layer (API Endpoints)
        ↓
Business Logic Layer (Services)
        ↓
Data Access Layer (Repositories)
        ↓
Database Layer (PostgreSQL)
```

**Benefits**:
- Clear separation of concerns
- Easy testing of each layer
- Scalability and maintainability

### 2. Service Layer Pattern

All business logic is encapsulated in service classes:

```python
# Example Service
class ProductionService:
    def __init__(self, db: Session):
        self.db = db
    
    def record_production(self, data: ProductionCreate) -> Production:
        # Validate data
        # Calculate derived fields (production %)
        # Create database record
        # Return created record
        pass
    
    def get_daily_stats(self, date: date) -> DailyStats:
        # Query production records
        # Calculate aggregates
        # Return stats
        pass
```

### 3. Repository Pattern

Data access is abstracted through repositories:

```python
class ProductionRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, obj: ProductionCreate) -> Production:
        pass
    
    def get_by_date_house(self, date: date, house_id: UUID) -> Optional[Production]:
        pass
    
    def list_by_date_range(self, from_date: date, to_date: date) -> List[Production]:
        pass
```

### 4. Dependency Injection

FastAPI's dependency injection system for loose coupling:

```python
from fastapi import Depends, APIRouter

router = APIRouter()

def get_production_service(db: Session = Depends(get_db)) -> ProductionService:
    return ProductionService(db)

@router.post("/production")
async def create_production(
    data: ProductionCreate,
    service: ProductionService = Depends(get_production_service)
):
    return service.record_production(data)
```

### 5. DTO (Data Transfer Object) Pattern

Separate internal models from API models:

```python
# Internal database model
class Production(Base):
    __tablename__ = "production_records"
    # ... database fields

# API request schema
class ProductionCreate(BaseModel):
    date: date
    house: str
    # ... request fields

# API response schema
class ProductionResponse(BaseModel):
    id: UUID
    date: date
    house: str
    production_percentage: float
    # ... response fields
```

---

## Authentication & Authorization

### JWT Token Strategy

```python
# Token payload structure
{
  "sub": "user_id",
  "email": "user@example.com",
  "role": "admin",
  "exp": 1624704600,
  "iat": 1624701000
}
```

### Role-Based Access Control (RBAC)

```python
# Define roles and permissions
ROLE_PERMISSIONS = {
    "admin": ["create_user", "delete_user", "view_reports", "delete_records"],
    "manager": ["record_production", "record_sales", "view_reports"],
    "worker": ["record_production"],
    "accountant": ["view_reports", "approve_expenses", "view_financials"]
}

# Dependency for checking permissions
async def check_permission(required_role: str):
    async def permission_checker(current_user: User = Depends(get_current_user)):
        if current_user.role not in [required_role, "admin"]:
            raise HTTPException(status_code=403, detail="Insufficient permissions")
        return current_user
    return permission_checker
```

---

## Error Handling

### Exception Hierarchy

```python
class AppException(Exception):
    """Base exception for application errors"""
    code: str
    status_code: int
    message: str

class ValidationException(AppException):
    code = "VALIDATION_ERROR"
    status_code = 400

class UnauthorizedException(AppException):
    code = "UNAUTHORIZED"
    status_code = 401

class NotFoundException(AppException):
    code = "NOT_FOUND"
    status_code = 404

class ConflictException(AppException):
    code = "CONFLICT"
    status_code = 409
```

### Exception Middleware

```python
@app.exception_handler(AppException)
async def app_exception_handler(request: Request, exc: AppException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": {
                "code": exc.code,
                "message": exc.message,
                "timestamp": datetime.utcnow().isoformat(),
                "request_id": request.headers.get("X-Request-ID")
            }
        }
    )
```

---

## Data Validation

### Pydantic Models with Custom Validators

```python
from pydantic import BaseModel, field_validator, model_validator

class ProductionCreate(BaseModel):
    date: date
    number_of_birds: int
    eggs_collected: int
    broken_eggs: int = 0
    
    @field_validator('number_of_birds')
    def validate_birds(cls, v):
        if v <= 0:
            raise ValueError('Number of birds must be positive')
        return v
    
    @model_validator(mode='after')
    def validate_eggs_vs_birds(self):
        if self.eggs_collected > self.number_of_birds:
            raise ValueError('Eggs collected cannot exceed number of birds')
        return self
```

---

## Performance Optimization

### 1. Database Query Optimization

```python
# Use select() with proper joins
from sqlalchemy import select

# Good: Only select needed columns
query = select(
    Production.date,
    Production.eggs_collected,
    Production.production_percentage
).filter(Production.date >= from_date)

# Bad: Select all columns (N+1 query problem)
records = db.query(Production).all()
for record in records:
    print(record.house.name)  # Triggers separate query

# Good: Eager loading
records = db.query(Production).options(
    joinedload(Production.house)
).all()
```

### 2. Caching Strategy

```python
from functools import lru_cache
from redis import Redis

# In-memory cache for computed values
@lru_cache(maxsize=128)
def get_daily_stats(date: str) -> dict:
    # Expensive computation
    pass

# Redis cache for frequently accessed data
def get_customer(customer_id: UUID):
    cache_key = f"customer:{customer_id}"
    
    # Try cache first
    cached = redis_client.get(cache_key)
    if cached:
        return json.loads(cached)
    
    # Query database
    customer = db.query(Customer).get(customer_id)
    
    # Store in cache for 1 hour
    redis_client.setex(
        cache_key,
        3600,
        json.dumps(customer.dict())
    )
    
    return customer
```

### 3. Pagination for Large Datasets

```python
class PaginationParams(BaseModel):
    page: int = 1
    per_page: int = 20

def get_paginated_results(
    query,
    params: PaginationParams
) -> dict:
    total = query.count()
    skip = (params.page - 1) * params.per_page
    
    items = query.offset(skip).limit(params.per_page).all()
    
    return {
        "data": items,
        "pagination": {
            "page": params.page,
            "per_page": params.per_page,
            "total": total,
            "pages": (total + params.per_page - 1) // params.per_page
        }
    }
```

---

## Logging & Monitoring

### Structured Logging

```python
import structlog
import logging

logger = structlog.get_logger()

# Structured logs with context
logger.info(
    "production_recorded",
    user_id=user_id,
    date=record.date,
    eggs_produced=record.eggs_collected,
    production_percentage=record.production_percentage
)

# Error logging with traceback
try:
    record_production(data)
except Exception as e:
    logger.error(
        "production_recording_failed",
        user_id=user_id,
        error=str(e),
        exc_info=True
    )
```

### Monitoring Metrics

- Request latency (p50, p95, p99)
- Database query times
- Cache hit ratio
- Error rate by endpoint
- Active user sessions

---

## Deployment Strategy

### Development
```bash
docker-compose up
```

### Production
1. Build Docker images
2. Push to registry
3. Deploy to Kubernetes cluster
4. Configure load balancer
5. Set up SSL/TLS certificates
6. Configure monitoring and alerting

---

*Architecture Version: 1.0*
*Last Updated: 2026-06-26*