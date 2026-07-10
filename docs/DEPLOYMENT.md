# Deployment Guide

## Prerequisites
- Docker & Docker Compose
- Node.js 16+
- Python 3.9+
- PostgreSQL 13+
- Kubernetes (optional)
- AWS Account (for cloud deployment)

## Local Development

### Using Docker Compose
```bash
# Clone repository
git clone https://github.com/Sujeethkatta/ai-interview-coach.git
cd ai-interview-coach

# Setup environment
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env

# Start services
docker-compose up -d

# Access applications
# Frontend: http://localhost:3000
# Backend: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

### Manual Setup

#### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Setup database
alembic upgrade head

# Start server
uvicorn app.main:app --reload
```

#### Frontend
```bash
cd frontend
npm install
npm start
```

## Production Deployment

### Docker Build
```bash
# Build backend
docker build -t interview-coach-backend:latest ./backend

# Build frontend
docker build -t interview-coach-frontend:latest ./frontend
```

### Kubernetes Deployment
```bash
# Apply configurations
kubectl apply -f deployment/kubernetes/

# Check status
kubectl get pods
kubectl get services

# View logs
kubectl logs -f deployment/interview-coach-backend
```

### AWS Deployment (Terraform)
```bash
cd deployment/terraform

# Initialize
terraform init

# Plan
terraform plan -var="db_password=your-password"

# Apply
terraform apply -var="db_password=your-password"

# Get outputs
terraform output
```

## Environment Configuration

### Backend (.env)
```env
DATABASE_URL=postgresql://user:password@localhost:5432/db
REDIS_URL=redis://localhost:6379
JWT_SECRET_KEY=your-secret-key
CORS_ORIGINS=["http://localhost:3000"]
OLLAMA_API_URL=http://ollama:11434
```

### Frontend (.env)
```env
REACT_APP_API_URL=http://localhost:8000/api/v1
REACT_APP_WS_URL=ws://localhost:8000/ws
```

## Database Setup

### Create Database
```bash
psql -U postgres

CREATE DATABASE interview_coach;
CREATE USER interview_coach WITH PASSWORD 'secure_password';
ALTER ROLE interview_coach SET client_encoding TO 'utf8';
ALTER ROLE interview_coach SET default_transaction_isolation TO 'read committed';
ALTER ROLE interview_coach SET default_transaction_deferrable TO on;
GRANT ALL PRIVILEGES ON DATABASE interview_coach TO interview_coach;
```

### Run Migrations
```bash
cd backend
alembic upgrade head
```

## Health Checks

### Backend Health
```bash
curl http://localhost:8000/health
```

### Frontend Health
```bash
curl http://localhost:3000
```

## Monitoring

### Logs
```bash
# Docker
docker-compose logs -f backend
docker-compose logs -f frontend

# Kubernetes
kubectl logs -f deployment/interview-coach-backend
kubectl logs -f deployment/interview-coach-frontend
```

### Metrics
- Monitor CPU/Memory usage
- Track database connections
- Monitor API response times
- Track error rates

## Scaling

### Horizontal Scaling
```bash
# Docker Compose
docker-compose up -d --scale backend=3 --scale frontend=2

# Kubernetes
kubectl scale deployment interview-coach-backend --replicas=3
kubectl scale deployment interview-coach-frontend --replicas=2
```

## Backup & Recovery

### Database Backup
```bash
# Backup
pg_dump interview_coach > backup.sql

# Restore
psql interview_coach < backup.sql
```

## Troubleshooting

### Common Issues

1. **Database Connection Error**
   - Check DATABASE_URL
   - Verify PostgreSQL is running
   - Check network connectivity

2. **API Not Responding**
   - Check backend logs
   - Verify port 8000 is accessible
   - Check JWT_SECRET_KEY configuration

3. **Frontend Loading Issues**
   - Check REACT_APP_API_URL
   - Clear browser cache
   - Check npm dependencies

4. **Ollama Connection Error**
   - Verify Ollama container is running
   - Check OLLAMA_API_URL
   - Download required models: `ollama pull llama2`
