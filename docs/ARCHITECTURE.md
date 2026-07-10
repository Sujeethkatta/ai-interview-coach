# Architecture

## System Overview

```
┌─────────────────────────────────────────────────────────────┐
│                       Client Layer                           │
│                    React SPA (Browser)                       │
└────────────────────────┬────────────────────────────────────┘
                         │
                    HTTP/HTTPS
                         │
┌─────────────────────────┴────────────────────────────────────┐
│                   API Gateway / Proxy                        │
│                      (Nginx)                                 │
└────────────────────────┬────────────────────────────────────┘
                         │
        ┌────────────────┼────────────────┐
        │                │                │
┌───────▼────────┐ ┌────▼─────────┐ ┌───▼────────────┐
│  Backend API   │ │  WebSocket   │ │  Static Files │
│  (FastAPI)     │ │  Server      │ │  (Frontend)    │
└───────┬────────┘ └────┬─────────┘ └────────────────┘
        │                │
        └────────────────┬──────────────────┐
                         │                  │
         ┌───────────────┼──────────┐      │
         │               │          │      │
    ┌────▼────┐    ┌────▼────┐ ┌──▼──┐ ┌─▼──┐
    │Database │    │  Cache  │ │ ML  │ │ VDB│
    │(PostgreSQL)  │ (Redis) │ │Models  │ │Chroma
    └─────────┘    └─────────┘ └──────┘ └────┘
```

## Component Architecture

### Frontend
- **Framework**: React 18 with TypeScript
- **State Management**: Redux Toolkit
- **Styling**: Tailwind CSS
- **HTTP Client**: Axios with interceptors
- **UI Components**: Custom components with Shadcn UI principles

### Backend
- **Framework**: FastAPI with Pydantic
- **Database**: PostgreSQL for relational data
- **ORM**: SQLAlchemy
- **Authentication**: JWT with bcrypt
- **API Documentation**: Auto-generated Swagger UI

### Services
- **Interview Engine**: Question generation and management
- **Answer Evaluator**: Answer quality assessment
- **RAG Pipeline**: Semantic search and context retrieval
- **LLM Client**: Integration with Ollama and HuggingFace

### Data Layer
- **Primary DB**: PostgreSQL (users, interviews, resumes)
- **Cache**: Redis (sessions, rate limiting)
- **Vector DB**: Chroma (embeddings, semantic search)
- **File Storage**: Local filesystem or S3

## Data Flow

### Interview Creation Flow
1. User selects interview type and difficulty
2. Backend creates interview record
3. Questions are generated using LLM
4. Questions are indexed in vector DB
5. Frontend displays interview interface

### Answer Evaluation Flow
1. User submits answer
2. Answer is stored in database
3. LLM evaluates answer quality
4. Feedback is generated and stored
5. Analytics are updated
6. Results displayed to user

## Scalability Considerations

### Horizontal Scaling
- Stateless backend (FastAPI)
- Load balancer (Nginx)
- Database replication
- Cache cluster (Redis Sentinel)

### Performance Optimization
- Database indexing
- API caching with Redis
- Frontend code splitting
- Lazy loading components
- Image optimization

## Security

- JWT token-based authentication
- Password hashing with bcrypt
- HTTPS/TLS encryption
- CORS configuration
- Rate limiting
- Input validation
- SQL injection prevention (ORM)
- XSS protection (React escaping)
