# AI Interview Coach Pro

An AI-powered full-stack interview preparation platform that generates personalized technical interviews, evaluates candidate answers using AI, analyzes resumes, and produces detailed performance reports with actionable feedback and personalized learning roadmaps.

## Live Demo

Frontend: https://ai-interview-coach-gold.vercel.app/

Backend API: https://ai-interview-coach-7kwf.onrender.com

API Documentation: https://ai-interview-coach-7kwf.onrender.com/docs

## Features

- JWT-based user authentication
- Resume upload and PDF text extraction
- AI-powered personalized interview generation
- Company and role-specific interview questions
- AI-based answer evaluation
- Technical, communication, and confidence scoring
- Intelligent handling of AI quota and service failures
- Detailed interview performance reports
- Strengths and areas-for-improvement analysis
- Personalized learning roadmap
- Hiring recommendation
- Interview history and progress tracking
- Performance dashboard with latest and average scores
- Responsive React frontend
- Production deployment with separate frontend and backend services

## Tech Stack

### Frontend

- React
- TypeScript
- Vite
- Tailwind CSS
- Axios
- React Router

### Backend

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic
- JWT Authentication
- Pydantic

### AI and Resume Intelligence

- Google Gemini API
- Prompt Engineering
- Structured AI Evaluation
- PyMuPDF for resume text extraction

### Deployment

- Vercel — Frontend
- Render — Backend
- PostgreSQL — Production database

## System Architecture

The application follows a modular full-stack architecture:

1. The React frontend handles authentication, resume upload, interview sessions, dashboards, and reports.
2. The FastAPI backend provides REST APIs for authentication, resume processing, interviews, answer evaluation, and report generation.
3. PostgreSQL stores users, interviews, answers, evaluation scores, and reports.
4. Gemini AI generates personalized interview questions and evaluates candidate responses.
5. A deterministic scoring layer prevents AI service failures or quota issues from incorrectly reducing candidate performance scores.

## Interview Flow

1. User creates an account and logs in.
2. User uploads a resume.
3. Resume text is extracted and analyzed.
4. User selects a target company, role, interview type, and difficulty.
5. AI generates personalized interview questions.
6. Candidate submits answers.
7. Gemini evaluates each answer across:
   - Technical ability
   - Communication
   - Confidence
8. The platform generates a detailed final report.
9. The dashboard tracks interview history, latest performance, average score, and recommended improvement areas.

## Scoring Reliability

The application includes fault-tolerant scoring logic.

If an AI evaluation fails because of quota limits, network problems, or temporary service unavailability, that failed evaluation is explicitly marked as unavailable and excluded from candidate score calculations.

This prevents infrastructure failures from being incorrectly interpreted as poor candidate performance.

## Project Structure

```text
ai-interview-coach/
├── backend/
│   ├── app/
│   │   ├── ai/
│   │   ├── api/
│   │   ├── core/
│   │   ├── models/
│   │   ├── repositories/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── utils/
│   ├── alembic/
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── api/
│   │   ├── components/
│   │   ├── context/
│   │   ├── hooks/
│   │   ├── pages/
│   │   └── ui/
│   └── package.json
│
└── README.md
