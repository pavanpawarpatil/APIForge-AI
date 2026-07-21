# 🚀 APIForge AI

> **Intelligent Backend API Generator Using Multi-Agent LLMs**

APIForge AI is an AI-powered backend code generation platform that automates the creation of production-ready backend projects using a **Multi-Agent Architecture**. Users simply describe the backend they want, and APIForge AI generates a complete project structure, source code, configuration files, and packages everything into a downloadable ZIP file.

The application combines **FastAPI**, **LangGraph**, **LangChain**, **Ollama**, and **Next.js** to provide an intelligent and user-friendly development experience.

---

# 📌 Features

- 🤖 Multi-Agent AI Workflow using LangGraph
- 📝 Natural Language Project Generation
- ⚡ FastAPI Backend Generation
- 📂 Automatic Folder Structure Creation
- 🔐 JWT Authentication Support
- 🗄️ MySQL Database Integration
- 📦 Automatic ZIP File Generation
- ⬇️ One-Click Project Download
- 🎨 Modern Next.js Frontend
- 🔄 Real-time Backend Generation Workflow

---

# 🏗️ System Architecture

```
                    User Request
                         │
                         ▼
               Next.js Frontend (UI)
                         │
                         ▼
                FastAPI Backend API
                         │
                         ▼
              LangGraph Multi-Agent System
                         │
     ┌─────────────┬──────────────┬──────────────┐
     ▼             ▼              ▼
Request Parser  Project Planner  Code Generator
     │             │              │
     └─────────────┴──────────────┘
                     │
                     ▼
             Generate Project Files
                     │
                     ▼
                Create ZIP Archive
                     │
                     ▼
                Download to User
```

---

# ⚙️ Tech Stack

## Frontend

- Next.js
- React
- TypeScript
- Tailwind CSS

## Backend

- FastAPI
- Python
- SQLAlchemy
- PyMySQL
- JWT Authentication

## AI & LLM

- LangGraph
- LangChain
- Ollama
- Local LLM

## Database

- MySQL

---

# 🤖 Multi-Agent Workflow

APIForge AI follows a Multi-Agent architecture where each agent is responsible for a specific task.

### Agent 1 — Request Parser

- Understands user requirements
- Extracts project information
- Converts natural language into structured JSON

### Agent 2 — Project Planner

- Creates the project architecture
- Plans folders and files
- Decides required APIs and modules

### Agent 3 — Code Generator

- Generates backend source code
- Creates routes
- Creates models
- Creates schemas
- Creates services
- Generates configuration files

### Final Step

- Creates project folder
- Compresses project
- Returns downloadable ZIP file


# 🚀 Installation

## 1. Clone Repository

```bash
git clone https://github.com/pavanpawarpatil/APIForge-AI.git

cd APIForge-AI
```

---

# 🖥️ Backend Setup

## Step 1

Open terminal inside the backend folder.

```bash
cd backend
```

You should now be inside:

```
APIForge-AI/backend
```

---

## Step 2

Create a virtual environment.

```bash
python -m venv .venv
```

---

## Step 3

Activate the virtual environment.

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

If activated successfully, your terminal will look similar to:

```
(.venv) APIForge-AI/backend>
```

---

## Step 4

Install Python dependencies.

```bash
pip install -r requirements.txt
```

---

## Step 5

Create a `.env` file inside the backend folder using `.env.example`.

Example:

```env
DB_HOST=localhost
DB_PORT=3306
DB_NAME=apiforge_ai_db
DB_USER=your_username
DB_PASSWORD=your_password

OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=qwen2.5:3b

SECRET_KEY=your_secret_key
```

---

## Step 6

Run the backend server.

```bash
uvicorn app.main:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

---

# 💻 Frontend Setup

Open a new terminal.

```bash
cd frontend
```

Install dependencies.

```bash
npm install
```

Run the frontend.

```bash
npm run dev
```

Frontend URL

```
http://localhost:3000
```

---

# ▶️ Running the Complete Application

Open two terminals.

## Terminal 1 (Backend)

```bash
cd backend

.venv\Scripts\activate

uvicorn app.main:app --reload
```

---

## Terminal 2 (Frontend)

```bash
cd frontend

npm install

npm run dev
```

---

Open your browser.

Frontend

```
http://localhost:3000
```

Backend

```
http://127.0.0.1:8000
```

---

# 📷 Screenshots

Add screenshots of:

- Home Page
- Prompt Input
- Generated Backend Project
- Download ZIP
- Workflow

---

# 🔮 Future Improvements

- Docker Support
- PostgreSQL Support
- Multiple Framework Support
- Authentication Templates
- Cloud Deployment
- Project History
- API Documentation Generation
- Multi-LLM Support

---

# 👨‍💻 Author

**Pavan Pawar**

- GitHub: https://github.com/pavanpawarpatil
- LinkedIn: https://www.linkedin.com/in/pavan-pawar-patil/

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

---

# 📄 License

This project is licensed under the MIT License.