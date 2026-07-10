# Installation & Setup Guide

## Quick Start (5 minutes)

### Prerequisites
- Docker & Docker Compose installed
- Git

### Steps

```bash
# 1. Clone repository
git clone https://github.com/Sujeethkatta/ai-interview-coach.git
cd ai-interview-coach

# 2. Start with Docker Compose
docker-compose up -d

# 3. Wait for services to start (~2 minutes)
docker-compose logs -f

# 4. Access the application
# Frontend: http://localhost:3000
# Backend API: http://localhost:8000
# API Documentation: http://localhost:8000/docs
```

## Manual Setup (15 minutes)

### Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Setup environment
cp .env.example .env

# Configure database in .env
# DATABASE_URL=postgresql://user:password@localhost:5432/interview_coach

# Run migrations
alembic upgrade head

# Start server
uvicorn app.main:app --reload
```

### Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Setup environment
cp .env.example .env

# Start development server
npm start
```

### Database Setup (PostgreSQL)

```bash
# Create database
psql -U postgres

CREATE DATABASE interview_coach;
CREATE USER interview_coach WITH PASSWORD 'secure_password';
GRANT ALL PRIVILEGES ON DATABASE interview_coach TO interview_coach;
```

## First Steps

### 1. Create Account
- Go to http://localhost:3000
- Click "Sign Up"
- Fill in email, username, password
- Click "Create Account"

### 2. Login
- Use your credentials to login
- You'll be redirected to dashboard

### 3. Start Interview
- Click "Interview" in sidebar
- Select interview type (Behavioral, Technical, HR)
- Choose difficulty level
- Click "Start Interview"

### 4. Practice
- Answer the questions
- Get AI-powered feedback
- Review your performance
- Track progress in Analytics

## Configuration

### Environment Variables

#### Backend (.env)
```env
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/interview_coach
REDIS_URL=redis://localhost:6379

# JWT
JWT_SECRET_KEY=your-secret-key-change-in-production
JWT_ALGORITHM=HS256
JWT_EXPIRATION_HOURS=24

# CORS
CORS_ORIGINS=["http://localhost:3000", "https://yourdomain.com"]

# AI/ML
OLLAMA_API_URL=http://localhost:11434
OLLAMA_MODEL=llama2

# Environment
ENVIRONMENT=development
DEBUG=True
```

#### Frontend (.env)
```env
REACT_APP_API_URL=http://localhost:8000/api/v1
REACT_APP_WS_URL=ws://localhost:8000/ws
```

## Troubleshooting

### Port Already in Use
```bash
# Change port in docker-compose.yml or
# Kill process on port
lsof -ti:8000 | xargs kill -9  # Backend
lsof -ti:3000 | xargs kill -9  # Frontend
```

### Database Connection Error
```bash
# Check PostgreSQL is running
pg_isready -h localhost -p 5432

# Verify credentials in .env
# Check DATABASE_URL format
```

### Dependencies Issues
```bash
# Backend
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall

# Frontend
rm -rf node_modules package-lock.json
npm install
```

### Ollama Not Working
```bash
# Start Ollama
docker run -d -v ollama:/root/.ollama -p 11434:11434 ollama/ollama

# Pull required model
docker exec <container> ollama pull llama2
```

## Next Steps

1. **Read Documentation**: Check `docs/` folder for detailed guides
2. **Explore API**: Visit http://localhost:8000/docs
3. **Customize**: Edit interview questions in datasets/
4. **Deploy**: Follow deployment guide for production
5. **Contribute**: See CONTRIBUTING.md for development guidelines

## Support

- **Issues**: https://github.com/Sujeethkatta/ai-interview-coach/issues
- **Discussions**: https://github.com/Sujeethkatta/ai-interview-coach/discussions
- **Email**: support@interviewcoach.ai

## License

MIT License - see LICENSE file
