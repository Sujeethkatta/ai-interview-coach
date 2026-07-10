# Technology Stack

## Backend

### Framework & Server
- **FastAPI** - Modern async Python web framework
- **Uvicorn** - ASGI web server
- **Pydantic** - Data validation using Python type hints

### Database
- **PostgreSQL** - Relational database
- **SQLAlchemy** - ORM and database toolkit
- **Alembic** - Database migration tool

### Authentication & Security
- **python-jose** - JWT token generation and validation
- **Passlib** - Password hashing with bcrypt
- **cryptography** - Cryptographic recipes

### AI/ML
- **Transformers** - Hugging Face models
- **sentence-transformers** - Semantic embeddings
- **torch** - Deep learning framework
- **openai-whisper** - Speech recognition
- **Ollama** - Local LLM inference

### Vector Database
- **Chroma** - Embedded vector database
- **FAISS** - Vector similarity search

### Caching & Jobs
- **Redis** - Caching and task queue
- **Celery** - Distributed task queue

### File Processing
- **python-pptx** - PowerPoint files
- **pypdf** - PDF manipulation
- **python-docx** - Word documents
- **openpyxl** - Excel files
- **pillow** - Image processing

### Testing & Quality
- **pytest** - Testing framework
- **black** - Code formatter
- **flake8** - Linter
- **mypy** - Static type checker

### API Documentation
- **Swagger/OpenAPI** - Auto-generated API docs
- **ReDoc** - Alternative API documentation

## Frontend

### Core
- **React** 18+ - UI library
- **TypeScript** - Type-safe JavaScript
- **Vite** - Fast build tool

### Routing & State
- **React Router** - Client-side routing
- **Redux Toolkit** - State management
- **react-redux** - React bindings for Redux

### Styling
- **Tailwind CSS** - Utility-first CSS framework
- **PostCSS** - CSS processing

### UI & Components
- **Shadcn/ui** - High-quality components
- **@headlessui/react** - Headless UI components
- **@heroicons/react** - Beautiful SVG icons
- **lucide-react** - Icon library
- **Framer Motion** - Animation library

### Data Visualization
- **Recharts** - React charting library

### HTTP & API
- **Axios** - HTTP client
- **react-hot-toast** - Toast notifications

### Forms & Validation
- **react-hook-form** - Form state management
- **Zod** - TypeScript-first schema validation

### Audio
- **react-mic** - Audio recording component
- **wavesurfer.js** - Audio waveform visualization

### Build & Development
- **Eslint** - Code linting
- **Prettier** - Code formatting

## DevOps & Deployment

### Containerization
- **Docker** - Container engine
- **Docker Compose** - Multi-container orchestration

### Orchestration
- **Kubernetes** - Container orchestration
- **kubectl** - K8s CLI

### Infrastructure as Code
- **Terraform** - Infrastructure provisioning
- **AWS** - Cloud provider

### CI/CD
- **GitHub Actions** - CI/CD platform

### Web Server
- **Nginx** - Reverse proxy and web server

### Database Tools
- **pgAdmin** - PostgreSQL management
- **pg_dump** - Database backup

## Development Tools

### Python
- **pip** - Package manager
- **venv** - Virtual environments
- **Poetry** - Dependency management (optional)

### Node.js
- **npm** - Package manager
- **Node.js** 16+ - Runtime

### Version Control
- **Git** - Version control
- **GitHub** - Repository hosting

### IDE & Editors
- **VS Code** - Recommended editor
- **PyCharm** - Python IDE
- **WebStorm** - JavaScript IDE

## Free/Open-Source Alternatives

All technologies chosen are either free or have free tiers:
- ✅ FastAPI - Open source
- ✅ PostgreSQL - Open source
- ✅ React - Open source
- ✅ Ollama - Open source (local LLM)
- ✅ Chroma - Open source
- ✅ Whisper - Open source
- ✅ Docker - Open source
- ✅ Kubernetes - Open source
- ✅ Terraform - Open source
- ✅ GitHub Actions - Free for public repos
- ✅ Tailwind CSS - Open source

## Performance Characteristics

### API Response Times
- Authentication: ~50ms
- List interviews: ~100ms
- Generate question: ~2-5s (LLM dependent)
- Evaluate answer: ~3-8s (LLM dependent)
- Search resumes: ~50ms

### Storage
- Database (per user): ~5-10MB
- Resume files: Variable
- Vector embeddings: ~384 dimensions × 4 bytes = ~1.5KB per embedding

### Scalability
- Backend: Horizontal (stateless)
- Frontend: Static files (CDN)
- Database: Vertical scaling + read replicas
- Cache: Redis cluster
- Vector DB: Sharded across servers

## Security

- ✅ HTTPS/TLS encryption
- ✅ JWT token-based auth
- ✅ Password hashing (bcrypt)
- ✅ CORS protection
- ✅ SQL injection prevention (ORM)
- ✅ XSS protection (React escaping)
- ✅ Rate limiting
- ✅ Input validation
