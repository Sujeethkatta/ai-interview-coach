# Troubleshooting Guide

## Common Issues

### 1. Database Connection Failed

**Error**: `psycopg2.OperationalError: could not connect to server`

**Solutions**:
```bash
# Check if PostgreSQL is running
pg_isready -h localhost -p 5432

# Check DATABASE_URL format
# Format: postgresql://user:password@host:port/database

# Verify credentials
psql -U interview_coach -h localhost -d interview_coach

# Check .env file
grep DATABASE_URL backend/.env
```

### 2. Port Already in Use

**Error**: `Address already in use`

**Solutions**:
```bash
# Find process on port 8000
lsof -i :8000

# Kill process
kill -9 <PID>

# Or change port
uvicorn app.main:app --port 8001
```

### 3. Import Errors

**Error**: `ModuleNotFoundError: No module named 'app'`

**Solutions**:
```bash
# Make sure you're in correct directory
cd backend

# Install dependencies
pip install -r requirements.txt

# Check Python path
export PYTHONPATH=$(pwd)

# Verify installation
python -c "import app; print(app.__version__)"
```

### 4. JWT Token Invalid

**Error**: `Invalid or expired token`

**Solutions**:
```python
# Check JWT_SECRET_KEY is set
echo $JWT_SECRET_KEY

# Verify token format
# Should be: Bearer <token>

# Check token expiration
# Default: 24 hours

# Update .env if needed
JWT_SECRET_KEY=your-new-secret-key
```

### 5. Ollama Connection Error

**Error**: `HTTPConnectionPool(host='localhost', port=11434)`

**Solutions**:
```bash
# Check if Ollama is running
curl http://localhost:11434/api/tags

# Start Ollama container
docker run -d -p 11434:11434 ollama/ollama

# Download model
curl http://localhost:11434/api/pull -d '{"name": "llama2"}'

# Check OLLAMA_API_URL in .env
echo $OLLAMA_API_URL
```

### 6. Redis Connection Error

**Error**: `ConnectionError: Error 111 connecting to localhost:6379`

**Solutions**:
```bash
# Check if Redis is running
redis-cli ping

# Start Redis container
docker run -d -p 6379:6379 redis:7-alpine

# Verify connection
redis-cli -h localhost -p 6379 ping

# Check REDIS_URL in .env
echo $REDIS_URL
```

### 7. CORS Issues

**Error**: `Access to XMLHttpRequest blocked by CORS policy`

**Solutions**:
```python
# Check CORS_ORIGINS in backend/.env
# Add frontend URL to list
CORS_ORIGINS=["http://localhost:3000", "https://yourdomain.com"]

# Verify backend has CORS middleware
# In app/main.py:
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### 8. Frontend API Calls Failing

**Error**: `GET http://localhost:8000/api/v1/... 404 (Not Found)`

**Solutions**:
```bash
# Check REACT_APP_API_URL
grep REACT_APP_API_URL frontend/.env

# Should be: http://localhost:8000/api/v1

# Verify backend is running
curl http://localhost:8000/health

# Check API endpoint exists
curl http://localhost:8000/docs
```

### 9. Hot Reload Not Working

**Error**: Changes not reflecting in browser

**Solutions**:
```bash
# Backend: Ensure --reload flag
uvicorn app.main:app --reload

# Frontend: Check vite config
cat frontend/vite.config.ts

# Clear browser cache
# Ctrl+Shift+Delete (Chrome)
# Cmd+Shift+Delete (Safari)

# Restart development servers
```

### 10. Docker Container Won't Start

**Error**: `Error response from daemon`

**Solutions**:
```bash
# Check logs
docker logs <container_id>

# Rebuild image
docker build -t interview-coach-backend:latest ./backend

# Remove stopped containers
docker container prune

# Check disk space
docker system df

# Clean up unused images
docker image prune
```

## Performance Issues

### Slow API Responses
```bash
# Check database indexes
SELECT schemaname, tablename, indexname FROM pg_indexes;

# Monitor active queries
SELECT * FROM pg_stat_statements ORDER BY total_time DESC;

# Check query plans
EXPLAIN ANALYZE SELECT * FROM interviews WHERE user_id = '...';
```

### High Memory Usage
```bash
# Check process memory
ps aux | grep python

# Limit memory in Docker
# Add to docker-compose.yml:
mem_limit: 1g
mem_reservation: 512m
```

### Slow Frontend
```bash
# Bundle analysis
npm run build
ls -lh frontend/dist/

# Check network tab in DevTools
# Look for slow API calls
# Look for large assets
```

## Debugging Tips

### Enable Debug Logging
```python
# In backend .env
DEBUG=True
LOG_LEVEL=DEBUG
```

### Check Logs
```bash
# Backend logs
docker-compose logs -f backend

# Frontend logs
# Open browser console (F12)

# Database logs
psql -h localhost -U interview_coach -d interview_coach \
  -c "SELECT * FROM pg_stat_statements;"
```

### Use Debugging Tools
```bash
# Python debugger
python -m pdb app/main.py

# React DevTools browser extension
# Redux DevTools browser extension

# Postman - Test APIs
# https://www.postman.com/
```

## Getting Help

1. Check documentation in `docs/`
2. Search GitHub issues
3. Check server logs
4. Enable debug mode
5. Use debugging tools
6. Create detailed issue report
7. Contact support

## Issue Report Template

```markdown
## Description
Clear description of the issue

## Steps to Reproduce
1. Step 1
2. Step 2
3. Step 3

## Expected Behavior
What should happen

## Actual Behavior
What actually happens

## Environment
- OS: Windows/Mac/Linux
- Python: 3.9/3.10/3.11
- Node: 16/18/20
- Docker: version

## Error Logs
```
Paste error log here
```

## Additional Info
Any other relevant information
```
