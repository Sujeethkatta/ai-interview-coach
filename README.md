# AI Interview Coach

A comprehensive AI-powered interview coaching platform built with FastAPI, React, and Machine Learning models. This application helps candidates prepare for interviews through realistic interview simulations, real-time feedback, and personalized coaching.

## 🎯 Features

- 🎤 **Interview Simulations** - Realistic interview scenarios across domains
- 🤖 **AI-Powered Evaluation** - Real-time answer analysis and feedback
- 🎙️ **Speech Recognition** - Whisper-based speech-to-text for spoken answers
- 💬 **Natural Language Processing** - Advanced NLP for answer evaluation
- 📊 **Analytics & Reports** - Comprehensive performance analytics
- 📋 **Resume Parser** - Extract and analyze resume information
- 🧠 **Vector Database** - RAG-based knowledge retrieval
- 🔐 **Secure Authentication** - JWT and OAuth2 support
- 📱 **Responsive Design** - Professional UI/UX with React

## 🛠️ Tech Stack

### Backend
- **Framework**: FastAPI
- **Database**: PostgreSQL, Chroma (Vector DB)
- **Authentication**: JWT, OAuth2
- **AI/ML**: Ollama (Llama2), Hugging Face, Whisper
- **Task Queue**: Celery

### Frontend
- **Framework**: React 18+
- **Styling**: Tailwind CSS, Shadcn/ui
- **State Management**: Redux Toolkit
- **HTTP Client**: Axios
- **Animations**: Framer Motion

### ML/AI
- **LLM**: Llama2 (via Ollama)
- **Embeddings**: Sentence-Transformers
- **Speech**: OpenAI Whisper
- **Vector DB**: Chroma, FAISS

## 📁 Project Structure

```
ai-interview-coach/
├── backend/                 # FastAPI backend
├── frontend/                # React frontend
├── ml_models/              # ML models and configs
├── vector_db/              # Vector database setup
├── datasets/               # Interview datasets
├── deployment/             # Deployment configs
├── docs/                   # Documentation
├── scripts/                # Utility scripts
└── docker-compose.yml      # Docker compose setup
```

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Node.js 16+
- Docker & Docker Compose
- PostgreSQL 13+

### Using Docker Compose (Recommended)

```bash
git clone https://github.com/Sujeethkatta/ai-interview-coach.git
cd ai-interview-coach
docker-compose up -d
```

This will start:
- PostgreSQL on port 5432
- Redis on port 6379
- Ollama on port 11434
- Backend API on port 8000
- Frontend on port 3000
- Nginx on port 80

### Backend Setup (Manual)

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
pip install -r requirements.txt

# Setup environment variables
cp .env.example .env

# Run migrations
alembic upgrade head

# Start server
uvicorn app.main:app --reload
```

### Frontend Setup (Manual)

```bash
cd frontend
npm install
cp .env.example .env
npm start
```

## 📚 API Documentation

Once the backend is running:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## ⚙️ Configuration

Create `.env` file in backend directory:

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
HUGGINGFACE_API_KEY=your-api-key

# Vector DB
CHROMA_PERSIST_DIR=./chroma_data
```

## 🧪 Testing

```bash
# Backend tests
cd backend
pytest tests/ -v

# Frontend tests
cd frontend
npm test

# Coverage
pytest tests/ --cov=app
```

## 🔍 Code Quality

```bash
# Backend
cd backend
black app/
flake8 app/
mypy app/

# Frontend
cd frontend
npm run lint
npm run format
```

## 📦 Deployment

### Kubernetes
```bash
cd deployment/kubernetes
kubectl apply -f .
```

### AWS (Terraform)
```bash
cd deployment/terraform
terraform init
terraform plan
terraform apply
```

## 📖 Documentation

- [API Documentation](docs/API.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Database Schema](docs/DATABASE.md)
- [Deployment Guide](docs/DEPLOYMENT.md)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

MIT License - see LICENSE file for details

## 💬 Support

For issues and questions:
- GitHub Issues: [Report an issue](https://github.com/Sujeethkatta/ai-interview-coach/issues)
- Email: support@interviewcoach.ai

## 🗺️ Roadmap

- [ ] Multi-language support
- [ ] Video interview recording
- [ ] Mock interviews with peers
- [ ] Certification programs
- [ ] Mobile app (React Native)
- [ ] Advanced analytics
- [ ] AI personality matching
- [ ] Interview scheduling

---

**Made with ❤️ for interview preparation**
