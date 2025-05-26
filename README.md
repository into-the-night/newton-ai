# NEWTON 🤖

Your personal AI tutor

**Newton** is a multi-agent AI tutoring system that intelligently routes academic questions to subject-specialist agents (Math and Physics). It leverages Google ADK and FastAPI to provide a web-based API and UI for interactive learning.

## Features ✨

- **Multi-agent orchestration:** Routes queries to Math or Physics agents based on question context.
- **Math Agent:** Solves arithmetic, algebra, and calculus problems, providing step-by-step explanations.
- **Physics Agent:** Answers conceptual and numerical physics questions, with access to a database of physical constants.
- **Web API & UI:** FastAPI server with endpoints and optional web interface.
- **Session management:** Uses SQLite for session storage.

## Packages Used 📦

- [google-adk](https://pypi.org/project/google-adk/) - Agent Development Kit for LLM orchestration
- [fastapi](https://fastapi.tiangolo.com/) - Web framework for the API
- [uvicorn](https://www.uvicorn.org/) - ASGI server for FastAPI
- [poetry](https://python-poetry.org/) - Dependency management and packaging

## Setup & Running Locally 🏃🏻‍♀️🏃🏻

1. **Clone the repository:**
   ```
   git clone https://github.com/yourusername/newton-ai.git
   cd newton-ai
   ```

2. **Install dependencies:** Make sure you have Poetry installed.
    ```
    poetry install
    ```

3. **Set up environment variables:** Copy or edit the .env file in src/ with your Google API key:
    ```
    GOOGLE_GENAI_USE_VERTEXAI=FALSE
    GOOGLE_API_KEY=your-google-api-key
    ```

4. **Run the server:**
    ```
    uvicorn src.main:app --reload
    ```

## LICENSE 📜

[MIT License](LICENSE)