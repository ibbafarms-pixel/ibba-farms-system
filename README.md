# IBBA Farms Management System

A comprehensive web application for poultry farm management, designed for IBBA Farms in Rwanda.

## 🚀 Features (Phase 1)

- ✅ User authentication with JWT
- ✅ Daily production recording
- ✅ Egg sales tracking
- ✅ Expense recording
- ✅ Feed inventory management
- ✅ Main dashboard with overview
- 🔄 Real-time data synchronization
- 📱 Responsive mobile design

## 🛠️ Technology Stack

- **Frontend**: React 18, Vite, Tailwind CSS
- **Backend**: FastAPI, Python 3.11, SQLAlchemy
- **Database**: PostgreSQL 15
- **Cache**: Redis 7
- **Containerization**: Docker & Docker Compose

## 📋 Quick Start

### With Docker (Recommended)

```bash
git clone https://github.com/ibbafarms-pixel/ibba-farms-system.git
cd ibba-farms-system
docker-compose up
```

Access:
- Frontend: http://localhost:5173
- Backend: http://localhost:8000
- API Docs: http://localhost:8000/docs

### Without Docker

See [SETUP.md](SETUP.md) for detailed local setup instructions.

## 📚 Documentation

- [Setup Guide](SETUP.md)
- [API Specification](docs/API_SPEC.md)
- [Database Schema](docs/DATABASE_SCHEMA.md)
- [System Architecture](docs/ARCHITECTURE.md)
- [Development Guide](docs/DEVELOPMENT.md)
- [Development Roadmap](ROADMAP.md)
- [Contributing Guidelines](CONTRIBUTING.md)

## 🎯 Project Phases

### Phase 1: Core Operations (Current)
- Production recording
- Sales management
- Expense tracking
- Feed inventory
- Dashboard overview

### Phase 2: Financial Management
- Complete accounting system
- Customer management
- Bank & cash reconciliation
- Loan tracking
- Financial reports

### Phase 3: Advanced Operations
- Flock management
- Advanced inventory
- Analytics & ratios
- Notifications

### Phase 4: AI & Future
- Forecasting
- Anomaly detection
- Mobile apps
- SMS/WhatsApp integration

## 🏗️ Project Structure

```
.
├── backend/              # FastAPI application
│   ├── app/
│   │   ├── models/       # Database models
│   │   ├── schemas/      # Pydantic schemas
│   │   ├── routers/      # API endpoints
│   │   ├── services/     # Business logic
│   │   ├── auth/         # Authentication
│   │   └── utils/        # Utilities
│   ├── tests/            # Test suite
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/             # React application
│   ├── src/
│   │   ├── pages/        # Page components
│   │   ├── components/   # Reusable components
│   │   ├── context/      # React context
│   │   ├── services/     # API services
│   │   └── styles/       # CSS styles
│   ├── package.json
│   └── Dockerfile
├── docs/                 # Documentation
│   ├── API_SPEC.md
│   ├── DATABASE_SCHEMA.md
│   ├── ARCHITECTURE.md
│   └── DEVELOPMENT.md
├── docker-compose.yml
├── SETUP.md
├── ROADMAP.md
└── CONTRIBUTING.md
```

## 🔐 Security

- JWT-based authentication
- Role-based access control (RBAC)
- Password hashing with bcrypt
- CORS protection
- SQL injection prevention (SQLAlchemy ORM)
- Rate limiting on authentication endpoints

## 📊 Database

PostgreSQL with 8+ core tables:
- users
- houses
- production_records
- sales_records
- customers
- expense_records
- suppliers
- feed_inventory
- feed_transactions

## 🧪 Testing

```bash
# Backend
cd backend
pytest --cov=app

# Frontend
cd frontend
npm test -- --coverage
```

## 🤝 Contributing

We welcome contributions! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details.

### Quick Start for Contributors

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make your changes and commit: `git commit -m "feat: add feature"`
4. Push to branch: `git push origin feature/your-feature`
5. Open a pull request

## 📝 Commit Message Format

```
feat: add new feature
fix: fix bug
docs: update documentation
test: add tests
refactor: refactor code
style: format code
chore: update dependencies
```

## 🐛 Known Issues

None yet - this is an early-stage project.

## 🗺️ Future Enhancements

- AI-powered forecasting
- Mobile native apps (iOS/Android)
- SMS/WhatsApp integration
- Advanced analytics
- Multi-farm support
- API marketplace

## 📞 Support

- 📖 Read the [documentation](docs/)
- 🔍 Check [GitHub Issues](https://github.com/ibbafarms-pixel/ibba-farms-system/issues)
- 💬 Create a new issue with details

## 📄 License

Proprietary - IBBA Farms

## 👥 Team

Developed for IBBA Farms Rwanda

---

**Get Started**: Follow the [SETUP.md](SETUP.md) guide to run the application locally.

**Last Updated**: 2026-06-26
