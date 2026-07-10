# Project Structure Guide

## Directory Overview

```
ai-interview-coach/
│
├── backend/                    # FastAPI Backend
│   ├── app/
│   │   ├── api/               # API routes and endpoints
│   │   │   ├── v1/
│   │   │   │   ├── endpoints/ # Individual route handlers
│   │   │   │   │   ├── auth.py
│   │   │   │   │   ├── users.py
│   │   │   │   │   ├── interviews.py
│   │   │   │   │   ├── resumes.py
│   │   │   │   │   ├── reports.py
│   │   │   │   │   └── analytics.py
│   │   │   │   └── api.py    # Route aggregation
│   │   ├── core/              # Core configuration
│   │   │   ├── config.py      # Settings
│   │   │   ├── security.py    # Auth & encryption
│   │   │   └── logging_config.py
│   │   ├── db/                # Database setup
│   │   │   ├── base.py        # SQLAlchemy base
│   │   │   ├── session.py     # DB session
│   │   │   └── __init__.py
│   │   ├── models/            # SQLAlchemy models
│   │   │   ├── user.py
│   │   │   ├── interview.py
│   │   │   ├── resume.py
│   │   │   ├── feedback.py
│   │   │   └── analytics.py
│   │   ├── schemas/           # Pydantic schemas
│   │   │   ├── auth.py
│   │   │   ├── user.py
│   │   │   ├── interview.py
│   │   │   └── resume.py
│   │   ├── services/          # Business logic
│   │   │   ├── interview_engine.py
│   │   │   └── answer_evaluator.py
│   │   ├── ml/                # ML components
│   │   │   ├── llm_client.py
│   │   │   ├── embeddings.py
│   │   │   ├── prompt_manager.py
│   │   │   ├── rag_pipeline.py
│   │   │   └── vector_db.py
│   │   ├── utils/             # Utilities
│   │   │   ├── file_handler.py
│   │   │   ├── validators.py
│   │   │   └── helpers.py
│   │   ├── main.py            # Application entry point
│   │   └── __init__.py
│   ├── tests/                 # Test suite
│   │   ├── test_auth.py
│   │   ├── test_interviews.py
│   │   ├── test_api.py
│   │   └── __init__.py
│   ├── requirements.txt        # Python dependencies
│   ├── .env.example           # Environment template
│   ├── Dockerfile             # Container image
│   └── alembic/               # Database migrations
│
├── frontend/                   # React Frontend
│   ├── src/
│   │   ├── components/        # Reusable components
│   │   │   ├── Layout/
│   │   │   │   ├── Layout.tsx
│   │   │   │   ├── Navbar.tsx
│   │   │   │   └── Sidebar.tsx
│   │   │   ├── Common/        # Shared components
│   │   │   └── ...
│   │   ├── pages/             # Page components
│   │   │   ├── Home.tsx
│   │   │   ├── Login.tsx
│   │   │   ├── Register.tsx
│   │   │   ├── Dashboard.tsx
│   │   │   ├── Interview.tsx
│   │   │   ├── CodingInterview.tsx
│   │   │   ├── Resume.tsx
│   │   │   ├── Report.tsx
│   │   │   ├── Analytics.tsx
│   │   │   ├── Profile.tsx
│   │   │   └── Settings.tsx
│   │   ├── services/          # API services
│   │   │   └── api.ts
│   │   ├── store/             # Redux state
│   │   │   ├── authSlice.ts
│   │   │   └── index.ts
│   │   ├── styles/            # Global styles
│   │   │   └── index.css
│   │   ├── App.tsx            # Root component
│   │   ├── main.tsx           # Entry point
│   │   └── vite-env.d.ts
│   ├── public/                # Static assets
│   │   └── index.html
│   ├── package.json           # Dependencies
│   ├── tsconfig.json          # TypeScript config
│   ├── vite.config.ts         # Vite config
│   ├── tailwind.config.js     # Tailwind config
│   ├── .env.example           # Environment template
│   ├── Dockerfile             # Production image
│   ├── Dockerfile.dev         # Development image
│   └── ...
│
├── ml_models/                 # ML Models
│   ├── embeddings/            # Embedding models
│   ├── whisper/               # Speech recognition
│   ├── llm/                   # Language models
│   └── README.md
│
├── vector_db/                 # Vector Database
│   ├── chroma_data/           # Chroma storage
│   ├── faiss_index/           # FAISS index
│   └── README.md
│
├── datasets/                  # Interview Questions
│   ├── behavioral.json
│   ├── technical.json
│   ├── coding.json
│   ├── hr.json
│   └── README.md
│
├── deployment/                # Deployment configs
│   ├── kubernetes/            # K8s manifests
│   │   ├── backend-deployment.yaml
│   │   └── frontend-deployment.yaml
│   ├── nginx/                 # Nginx config
│   │   └── nginx.conf
│   ├── terraform/             # Terraform IaC
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── outputs.tf
│   └── README.md
│
├── docs/                      # Documentation
│   ├── API.md                 # API documentation
│   ├── ARCHITECTURE.md        # System architecture
│   ├── DATABASE.md            # Database schema
│   ├── DEPLOYMENT.md          # Deployment guide
│   └── README.md
│
├── scripts/                   # Utility scripts
│   ├── migrate.sh             # Database migration
│   ├── seed.sh                # Database seeding
│   ├── backup.sh              # Database backup
│   └── ...
│
├── .github/                   # GitHub config
│   └── workflows/             # CI/CD pipelines
│       ├── backend-tests.yml
│       ├── frontend-tests.yml
│       └── build-deploy.yml
│
├── docker-compose.yml         # Local development
├── README.md                  # Project overview
├── SETUP.md                   # Setup guide
├── LICENSE                    # MIT License
├── CONTRIBUTING.md            # Contributing guide
├── CHANGELOG.md               # Version history
└── .gitignore                 # Git ignore rules
```

## Key Directories Explained

### Backend (app/)
- **api/**: REST API routes organized by version and endpoint type
- **core/**: Core configuration, security, and logging setup
- **db/**: Database connection, session management, and base models
- **models/**: SQLAlchemy ORM models for database tables
- **schemas/**: Pydantic models for request/response validation
- **services/**: Business logic and complex operations
- **ml/**: Machine learning integrations and utilities
- **utils/**: Helper functions and utilities

### Frontend (src/)
- **components/**: Reusable React components
- **pages/**: Full page components (routes)
- **services/**: API client and external service calls
- **store/**: Redux state management
- **styles/**: Global CSS and Tailwind configuration

### Deployment
- **kubernetes/**: Container orchestration manifests
- **terraform/**: Infrastructure as Code for AWS
- **nginx/**: Web server and reverse proxy configuration

## File Naming Conventions

### Python
- Files: `snake_case.py`
- Classes: `PascalCase`
- Functions: `snake_case`
- Constants: `UPPER_SNAKE_CASE`

### TypeScript/React
- Files: `PascalCase.tsx` (components), `camelCase.ts` (utilities)
- Components: `PascalCase`
- Variables: `camelCase`
- Constants: `UPPER_SNAKE_CASE`

## Import Patterns

### Backend
```python
# Absolute imports from app root
from app.core.config import settings
from app.db.session import SessionLocal
from app.models.user import User
from app.schemas.auth import LoginRequest
```

### Frontend
```typescript
// Absolute imports
import { RootState } from '@/store';
import { authApi } from '@/services/api';
import { Navbar } from '@/components/Layout';
```

## Adding New Features

### New API Endpoint
1. Create model in `app/models/`
2. Create schema in `app/schemas/`
3. Create endpoint handler in `app/api/v1/endpoints/`
4. Add service logic in `app/services/` if needed
5. Include router in `app/api/v1/api.py`

### New Frontend Page
1. Create component in `src/pages/`
2. Add route in `src/App.tsx`
3. Add navigation link in `src/components/Layout/Sidebar.tsx`
4. Create API calls in `src/services/api.ts` if needed
5. Use Redux for state management if complex

## Testing Structure

```
tests/
├── test_auth.py          # Authentication tests
├── test_interviews.py    # Interview endpoints
├── test_api.py           # General API tests
└── conftest.py           # Pytest configuration
```

## Environment Variables

Each section has its own `.env.example`:
- `backend/.env.example` - Backend configuration
- `frontend/.env.example` - Frontend configuration

Copy to `.env` and update values for your environment.
