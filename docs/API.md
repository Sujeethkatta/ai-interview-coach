# API Documentation

## Base URL

```
http://localhost:8000/api/v1
```

## Authentication

All endpoints require JWT token in `Authorization` header:

```
Authorization: Bearer <access_token>
```

## Endpoints

### Auth Endpoints

#### Register
```
POST /auth/register

{
  "email": "user@example.com",
  "username": "username",
  "password": "password",
  "full_name": "Full Name" (optional)
}

Response: 200 OK
{
  "message": "User registered successfully",
  "user_id": "uuid",
  "email": "user@example.com"
}
```

#### Login
```
POST /auth/login

{
  "email": "user@example.com",
  "password": "password"
}

Response: 200 OK
{
  "access_token": "jwt_token",
  "token_type": "bearer"
}
```

#### Get Current User
```
GET /auth/me

Headers: Authorization: Bearer <token>

Response: 200 OK
{
  "id": "uuid",
  "email": "user@example.com",
  "username": "username",
  "full_name": "Full Name"
}
```

### Interview Endpoints

#### Start Interview
```
POST /interviews/start

{
  "interview_type": "behavioral|technical|coding|hr",
  "difficulty": "beginner|intermediate|advanced|expert",
  "category": "string" (optional),
  "title": "string" (optional),
  "description": "string" (optional)
}

Response: 200 OK
{
  "id": "uuid",
  "title": "string",
  "interview_type": "string",
  "difficulty": "string",
  "category": "string"
}
```

#### List Interviews
```
GET /interviews/list?skip=0&limit=20

Headers: Authorization: Bearer <token>

Response: 200 OK
{
  "total": 10,
  "interviews": [
    {
      "id": "uuid",
      "title": "string",
      "interview_type": "string",
      "difficulty": "string",
      "score": 85.5
    }
  ]
}
```

#### Get Interview
```
GET /interviews/{interview_id}

Headers: Authorization: Bearer <token>

Response: 200 OK
{
  "id": "uuid",
  "title": "string",
  "interview_type": "string",
  "difficulty": "string",
  "score": 85.5
}
```

### Resume Endpoints

#### Upload Resume
```
POST /resumes/upload

Headers: 
  Authorization: Bearer <token>
  Content-Type: multipart/form-data

Body:
  file: <file>

Response: 200 OK
{
  "id": "uuid",
  "filename": "resume.pdf",
  "created_at": "2024-01-01T00:00:00"
}
```

#### List Resumes
```
GET /resumes/list

Headers: Authorization: Bearer <token>

Response: 200 OK
{
  "total": 5,
  "resumes": [
    {
      "id": "uuid",
      "filename": "resume.pdf",
      "created_at": "2024-01-01T00:00:00",
      "is_primary": true
    }
  ]
}
```

### Analytics Endpoints

#### Get Dashboard
```
GET /analytics/dashboard

Headers: Authorization: Bearer <token>

Response: 200 OK
{
  "total_interviews": 10,
  "completed_interviews": 8,
  "average_score": 82.5,
  "interviews": [
    {
      "id": "uuid",
      "title": "string",
      "type": "string",
      "score": 85.0
    }
  ]
}
```

## Error Responses

### 400 Bad Request
```json
{
  "detail": "Invalid request parameters"
}
```

### 401 Unauthorized
```json
{
  "detail": "Invalid or expired token"
}
```

### 404 Not Found
```json
{
  "detail": "Resource not found"
}
```

### 500 Internal Server Error
```json
{
  "detail": "Internal server error"
}
```

## Testing with cURL

### Register
```bash
curl -X POST http://localhost:8000/api/v1/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "username": "testuser",
    "password": "TestPass123"
  }'
```

### Login
```bash
curl -X POST http://localhost:8000/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "TestPass123"
  }'
```

### Start Interview
```bash
curl -X POST http://localhost:8000/api/v1/interviews/start \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <token>" \
  -d '{
    "interview_type": "technical",
    "difficulty": "intermediate"
  }'
```

## Interactive API Documentation

After starting the server, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
