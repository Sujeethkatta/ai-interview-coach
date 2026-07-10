# Database Schema

## Users Table
```sql
CREATE TABLE users (
  id UUID PRIMARY KEY,
  email VARCHAR(255) UNIQUE NOT NULL,
  username VARCHAR(255) UNIQUE NOT NULL,
  full_name VARCHAR(255),
  hashed_password VARCHAR(255) NOT NULL,
  profile_picture VARCHAR(255),
  bio TEXT,
  is_active BOOLEAN DEFAULT TRUE,
  is_verified BOOLEAN DEFAULT FALSE,
  is_admin BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  last_login TIMESTAMP
);
```

## Interviews Table
```sql
CREATE TABLE interviews (
  id UUID PRIMARY KEY,
  user_id UUID NOT NULL REFERENCES users(id),
  title VARCHAR(255) NOT NULL,
  description TEXT,
  interview_type VARCHAR(50) NOT NULL,
  difficulty VARCHAR(50),
  category VARCHAR(100),
  is_completed BOOLEAN DEFAULT FALSE,
  is_submitted BOOLEAN DEFAULT FALSE,
  duration_minutes INTEGER,
  score FLOAT,
  feedback TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  completed_at TIMESTAMP
);
```

## Interview Questions Table
```sql
CREATE TABLE interview_questions (
  id UUID PRIMARY KEY,
  interview_id UUID NOT NULL REFERENCES interviews(id),
  question TEXT NOT NULL,
  question_type VARCHAR(50),
  expected_answer TEXT,
  question_index INTEGER NOT NULL,
  code_template TEXT,
  test_cases JSONB,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Interview Answers Table
```sql
CREATE TABLE interview_answers (
  id UUID PRIMARY KEY,
  question_id UUID NOT NULL REFERENCES interview_questions(id),
  interview_id UUID NOT NULL REFERENCES interviews(id),
  answer_text TEXT,
  code_answer TEXT,
  audio_url VARCHAR(255),
  score FLOAT,
  feedback TEXT,
  is_correct BOOLEAN,
  time_spent_seconds INTEGER,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Resumes Table
```sql
CREATE TABLE resumes (
  id UUID PRIMARY KEY,
  user_id UUID NOT NULL REFERENCES users(id),
  filename VARCHAR(255) NOT NULL,
  file_path VARCHAR(255) NOT NULL,
  file_type VARCHAR(50),
  file_size VARCHAR(50),
  parsed_content JSONB,
  name VARCHAR(255),
  email VARCHAR(255),
  phone VARCHAR(20),
  location VARCHAR(255),
  summary TEXT,
  skills JSONB,
  experience JSONB,
  education JSONB,
  certifications JSONB,
  is_analyzed BOOLEAN DEFAULT FALSE,
  analysis_score VARCHAR(50),
  is_primary BOOLEAN DEFAULT FALSE,
  is_archived BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Feedback Table
```sql
CREATE TABLE feedback (
  id UUID PRIMARY KEY,
  answer_id UUID NOT NULL REFERENCES interview_answers(id),
  interview_id UUID NOT NULL REFERENCES interviews(id),
  user_id UUID NOT NULL REFERENCES users(id),
  content_score FLOAT,
  delivery_score FLOAT,
  confidence_score FLOAT,
  overall_score FLOAT,
  strengths TEXT,
  areas_for_improvement TEXT,
  suggestions TEXT,
  detailed_feedback TEXT,
  keyword_match FLOAT,
  sentiment VARCHAR(50),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## User Analytics Table
```sql
CREATE TABLE user_analytics (
  id UUID PRIMARY KEY,
  user_id UUID NOT NULL REFERENCES users(id),
  total_interviews INTEGER DEFAULT 0,
  completed_interviews INTEGER DEFAULT 0,
  average_score FLOAT,
  best_score FLOAT,
  worst_score FLOAT,
  top_skills JSONB,
  weak_skills JSONB,
  category_performance JSONB,
  weekly_stats JSONB,
  monthly_stats JSONB,
  date DATE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Indexes
```sql
-- Performance indexes
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_username ON users(username);
CREATE INDEX idx_interviews_user_id ON interviews(user_id);
CREATE INDEX idx_interviews_created_at ON interviews(created_at);
CREATE INDEX idx_interview_questions_interview_id ON interview_questions(interview_id);
CREATE INDEX idx_interview_answers_interview_id ON interview_answers(interview_id);
CREATE INDEX idx_resumes_user_id ON resumes(user_id);
CREATE INDEX idx_feedback_interview_id ON feedback(interview_id);
CREATE INDEX idx_user_analytics_user_id ON user_analytics(user_id);
```
