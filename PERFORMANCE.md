# Performance Optimization Guide

## Database Optimization

### Indexing
```sql
-- Create indexes for frequently queried columns
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_interviews_user_id ON interviews(user_id);
CREATE INDEX idx_interviews_created_at ON interviews(created_at);
```

### Connection Pooling
```python
# Use connection pooling for better performance
from sqlalchemy.pool import QueuePool

engine = create_engine(
    DATABASE_URL,
    poolclass=QueuePool,
    pool_size=20,
    max_overflow=40
)
```

### Query Optimization
```python
# Use select() and eager loading
from sqlalchemy import select
from sqlalchemy.orm import selectinload

stmt = select(Interview).options(
    selectinload(Interview.questions),
    selectinload(Interview.answers)
)
```

## Caching Strategy

### Redis Caching
```python
# Cache frequently accessed data
import redis

redis_client = redis.Redis(host='localhost', port=6379)

# Cache interview questions
cache_key = f"interview:{interview_id}:questions"
redis_client.setex(cache_key, 3600, json.dumps(questions))
```

### API Response Caching
```python
from fastapi_cache2 import FastAPICache2

@app.get("/interviews/list")
@cached(expire=300)  # Cache for 5 minutes
async def list_interviews():
    pass
```

## Frontend Optimization

### Code Splitting
```typescript
// Lazy load pages
const Dashboard = lazy(() => import('./pages/Dashboard'));
const Interview = lazy(() => import('./pages/Interview'));

<Suspense fallback={<Loading />}>
  <Dashboard />
</Suspense>
```

### Bundle Analysis
```bash
# Analyze bundle size
npm run build
npm install -D webpack-bundle-analyzer
```

### Image Optimization
```typescript
// Use responsive images
<img 
  src="image.jpg" 
  srcSet="image-small.jpg 480w, image.jpg 1024w"
  sizes="(max-width: 600px) 480px, 1024px"
  alt="description"
/>
```

## API Optimization

### Pagination
```python
@app.get("/interviews")
async def list_interviews(
    skip: int = 0,
    limit: int = 20,
    db: Session = Depends(get_db)
):
    # Always paginate large result sets
    return db.query(Interview).offset(skip).limit(limit).all()
```

### Filtering & Sorting
```python
# Implement efficient filtering
@app.get("/interviews")
async def list_interviews(
    category: Optional[str] = None,
    difficulty: Optional[str] = None,
    sort_by: str = "created_at"
):
    query = db.query(Interview)
    if category:
        query = query.filter(Interview.category == category)
    if difficulty:
        query = query.filter(Interview.difficulty == difficulty)
    return query.order_by(sort_by).all()
```

### Response Compression
```python
from fastapi.middleware.gzip import GZIPMiddleware

app.add_middleware(GZIPMiddleware, minimum_size=1000)
```

## LLM Optimization

### Prompt Caching
```python
# Cache similar prompts
prompt_hash = hashlib.md5(prompt.encode()).hexdigest()
cache_key = f"prompt:{prompt_hash}"

result = redis_client.get(cache_key)
if not result:
    result = llm_client.generate(prompt)
    redis_client.setex(cache_key, 3600, result)
```

### Model Optimization
```python
# Use smaller models for non-critical tasks
question_generator = SmallModel()  # Fast
answer_evaluator = LargeModel()    # Accurate
```

### Parallel Processing
```python
# Process multiple answers in parallel
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(evaluate_answer, answers))
```

## Vector Database Optimization

### Indexing
```python
# Create proper indexes
vector_db.create_index(
    index_name="interviews",
    index_type="hnsw",
    metric="cosine"
)
```

### Batch Operations
```python
# Batch insert for efficiency
vector_db.add_documents(
    documents=batch_documents,
    embeddings=batch_embeddings,
    ids=batch_ids
)
```

## Monitoring & Profiling

### APM Setup
```python
from prometheus_client import Counter, Histogram

request_count = Counter(
    'http_requests_total',
    'Total HTTP requests'
)

request_duration = Histogram(
    'http_request_duration_seconds',
    'HTTP request duration'
)
```

### Database Query Monitoring
```python
from sqlalchemy import event

@event.listens_for(Engine, "before_cursor_execute")
def receive_before_cursor_execute(conn, cursor, statement, params, context, executemany):
    conn.info.setdefault('query_start_time', []).append(time.time())
```

## Load Testing

### Using Apache JMeter
```bash
# Performance test
jmeter -n -t test_plan.jmx -l results.jtl
```

### Using Locust
```python
from locust import HttpUser, task, between

class InterviewCoachUser(HttpUser):
    wait_time = between(1, 3)
    
    @task
    def get_dashboard(self):
        self.client.get("/api/v1/analytics/dashboard")
    
    @task
    def start_interview(self):
        self.client.post(
            "/api/v1/interviews/start",
            json={"interview_type": "technical"}
        )
```

## Production Checklist

- [ ] Enable database connection pooling
- [ ] Configure Redis caching
- [ ] Enable API response compression
- [ ] Implement rate limiting
- [ ] Enable CORS for production domain
- [ ] Use environment-specific configurations
- [ ] Enable logging and monitoring
- [ ] Set up error tracking (Sentry)
- [ ] Configure CDN for static files
- [ ] Implement health checks
- [ ] Set up backup strategies
- [ ] Configure auto-scaling
