
# Roblox Shorts AI Studio - Backend

Backend API built with Python and FastAPI.

## Requirements

- Python 3.10 or newer
- pip

## Installation

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Activate it on Linux or macOS:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the server

```bash
uvicorn app.main:app --reload
```

## API URLs

- API: http://127.0.0.1:8000
- Health: http://127.0.0.1:8000/api/v1/health
- API documentation: http://127.0.0.1:8000/docs
- 
