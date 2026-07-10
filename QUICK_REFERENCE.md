# Quick Reference

## Common Commands

### Docker Compose
```bash
# Start services
docker-compose up -d

# Stop services
docker-compose down

# View logs
docker-compose logs -f

# Rebuild images
docker-compose build

# Run migrations
docker-compose exec backend alembic upgrade head

# Create admin user
docker-compose exec backend python scripts/seed.sh
```

### Database
```bash
# Connect to database
psql -h localhost -U interview_coach -d interview_coach

# List tables
\dt

# Run query
SELECT * FROM users;

# Backup database
pg_dump -h localhost -U interview_coach interview_coach > backup.sql

# Restore database
psql -h localhost -U interview_coach interview_coach < backup.sql
```

### Backend
```bash
# Run server
cd backend
uvicorn app.main:app --reload

# Run tests
pytest tests/ -v

# Format code
black app/

# Lint code
flake8 app/

# Type check
mypy app/

# Run migrations
alembic upgrade head

# Create migration
alembic revision --autogenerate -m "Description"
```

### Frontend
```bash
# Development server
cd frontend
npm start

# Build production
npm run build

# Run tests
npm test

# Lint code
npm run lint

# Format code
npm run format
```

## API Endpoints

### Auth
- `POST /api/v1/auth/register` - Register user
- `POST /api/v1/auth/login` - Login user
- `GET /api/v1/auth/me` - Get current user

### Interviews
- `POST /api/v1/interviews/start` - Start interview
- `GET /api/v1/interviews/list` - List interviews
- `GET /api/v1/interviews/{id}` - Get interview details

### Resumes
- `POST /api/v1/resumes/upload` - Upload resume
- `GET /api/v1/resumes/list` - List resumes

### Analytics
- `GET /api/v1/analytics/dashboard` - Get dashboard data

### Reports
- `GET /api/v1/reports/{id}` - Get interview report

## URLs

### Local Development
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
- Database: localhost:5432
- Redis: localhost:6379
- Ollama: localhost:11434

## Environment Variables

### Backend
```env
DATABASE_URL=postgresql://interview_coach:password@localhost:5432/interview_coach
REDIS_URL=redis://localhost:6379
JWT_SECRET_KEY=your-secret-key
OLLAMA_API_URL=http://localhost:11434
CORS_ORIGINS=["http://localhost:3000"]
```

### Frontend
```env
REACT_APP_API_URL=http://localhost:8000/api/v1
REACT_APP_WS_URL=ws://localhost:8000/ws
```

## File Structure Quick Navigation

```
backend/
  app/
    api/v1/endpoints/  ← API routes
    models/            ← Database models
    schemas/           ← Request/response validation
    services/          ← Business logic
    ml/                ← AI/ML components
    core/              ← Configuration
    utils/             ← Helper functions

frontend/
  src/
    pages/             ← Page components
    components/        ← Reusable components
    services/api.ts    ← API client
    store/             ← Redux state
    styles/            ← CSS/Tailwind
```

## Git Workflow

```bash
# Clone repository
git clone https://github.com/Sujeethkatta/ai-interview-coach.git
cd ai-interview-coach

# Create feature branch
git checkout -b feature/your-feature

# Make changes and commit
git add .
git commit -m "feat: Add your feature"

# Push to GitHub
git push origin feature/your-feature

# Create Pull Request
# On GitHub website
```

## Testing Quick Commands

```bash
# Backend
cd backend
pytest tests/ -v                    # Run all tests
pytest tests/test_auth.py -v       # Run specific file
pytest tests/ -v --cov=app         # With coverage

# Frontend
cd frontend
npm test                            # Run all tests
npm test -- --watch                # Watch mode
npm test -- --coverage             # With coverage
```

## Useful Links

- **FastAPI Docs**: https://fastapi.tiangolo.com/
- **React Docs**: https://react.dev/
- **Tailwind CSS**: https://tailwindcss.com/
- **PostgreSQL Docs**: https://www.postgresql.org/docs/
- **Ollama**: https://ollama.ai/
- **Docker**: https://docs.docker.com/
- **GitHub**: https://github.com/Sujeethkatta/ai-interview-coach

## Support Resources

- **Issues**: https://github.com/Sujeethkatta/ai-interview-coach/issues
- **Discussions**: https://github.com/Sujeethkatta/ai-interview-coach/discussions
- **Documentation**: ./docs/
- **Email**: support@interviewcoach.ai
