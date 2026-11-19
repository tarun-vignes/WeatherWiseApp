# WeatherWise

WeatherWise is a weather application being built for a full-stack technical assessment. This repository is developed in small, reviewable milestones.

## Current milestone

The project foundation contains a Next.js frontend shell and a FastAPI health endpoint. Weather lookup, forecasts, and saved searches are planned for later milestones and are not implemented yet.

## Project layout

```text
frontend/    Next.js and React user interface
backend/     FastAPI application and tests
```

## Run locally

Requirements: Node.js 20.9 or newer, npm, and Python 3.10 or newer. Use separate terminals for the frontend and backend.

Backend (PowerShell):

```powershell
cd backend
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload --port 8000
```

Open `http://localhost:8000/api/health` to check the backend, or `http://localhost:8000/docs` for the API documentation. If PowerShell blocks activation, use Command Prompt and `.venv\Scripts\activate.bat`. On macOS or Linux, activate with `source .venv/bin/activate`.

Frontend:

```powershell
cd frontend
npm install
npm run dev
```

Open `http://localhost:3000`. If PowerShell blocks `npm.ps1`, use `npm.cmd` in place of `npm`. The frontend does not call the backend yet.

## Checks

```powershell
# From backend, with the virtual environment active
python -m pytest -q

# From frontend
npm run lint
npm run build
```

The backend test checks the health endpoint. The frontend build checks its TypeScript and production compilation.
