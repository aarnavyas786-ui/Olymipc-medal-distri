# Smart Bridge — Olympics Dashboard

A responsive Flask web application that embeds the **Olympics Dashboard** published on Tableau Public. The application provides a landing page, a dedicated interactive dashboard page, a Tableau Story page, and links to the Tableau Public profile and original views.

> **Important:** This application hosts the website, not the Tableau workbook itself. Embedded Tableau Public views are loaded from Tableau's servers and require an internet connection. A separately published Tableau Story URL must be configured before the Story page can embed it.

## Features

- Responsive landing page with project navigation
- Tableau Embedding API v3 integration
- Dedicated `/dashboard` and `/story` pages
- Direct links to the original Tableau Public content
- Environment-based Tableau URL configuration
- Flask health endpoint at `/health`
- Render.com deployment configuration using Gunicorn

## Project structure

```text
olympics_tableau_web/
├── app.py
├── requirements.txt
├── Procfile
├── README.md
├── .gitignore
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── dashboard.html
│   └── story.html
└── static/
    └── css/
        └── style.css
```

## Tableau content

The dashboard URL is configured by default as:

`https://public.tableau.com/views/smartbridge_17932641696630/OlympicDashboard`

The Tableau Public profile link is:

`https://public.tableau.com/app/profile/aarna.vyas`

To embed a Tableau Story, obtain its published **Share → Copy Link** URL from Tableau Public and set `TABLEAU_STORY_URL` as described below. A story link is not assumed from the dashboard URL because a Tableau Story is a separately published view.

## Run locally

### 1. Prerequisites

- Python 3.10 or newer
- Internet connection to load the Tableau Public visualization

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Windows Command Prompt:

```cmd
py -m venv .venv
.venv\Scripts\activate.bat
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Tableau Story URL (optional until available)

Windows PowerShell:

```powershell
$env:TABLEAU_STORY_URL="https://public.tableau.com/views/your-workbook/your-story"
```

Windows Command Prompt:

```cmd
set TABLEAU_STORY_URL=https://public.tableau.com/views/your-workbook/your-story
```

macOS/Linux:

```bash
export TABLEAU_STORY_URL="https://public.tableau.com/views/your-workbook/your-story"
```

Set the value to your real Tableau Public Story link. If it is not configured, `/story` displays a helpful placeholder and a link to the Tableau profile.

### 5. Start the application

```bash
python app.py
```

Open these pages in your browser:

- Home: http://127.0.0.1:5000/
- Dashboard: http://127.0.0.1:5000/dashboard
- Story: http://127.0.0.1:5000/story
- Health check: http://127.0.0.1:5000/health

Stop the server with `Ctrl+C`.

## Deploy to Render.com

### 1. Push the project to GitHub

Create a repository and push all project files to its root. Do not commit virtual environments or secrets.

### 2. Create a Render Web Service

- In Render, create a **New → Web Service**.
- Connect your GitHub repository.
- Choose the branch to deploy.
- Set **Runtime** to Python.
- Set **Build Command** to:

  ```bash
  pip install -r requirements.txt
  ```

- Set **Start Command** to:

  ```bash
  gunicorn app:app
  ```

Render can also use the included `Procfile` (`web: gunicorn app:app`).

### 3. Set environment variables

In the Render service's Environment settings, add:

| Key | Value |
| --- | --- |
| `TABLEAU_DASHBOARD_URL` | `https://public.tableau.com/views/smartbridge_17932641696630/OlympicDashboard` |
| `TABLEAU_STORY_URL` | Your published Tableau Story URL (optional until available) |
| `TABLEAU_PROFILE_URL` | `https://public.tableau.com/app/profile/aarna.vyas` |

### 4. Deploy

Click **Deploy**. When the service is live, Render will provide a public URL such as `https://your-service-name.onrender.com`.

## Routes

| Route | Purpose |
| --- | --- |
| `/` | Project overview and navigation |
| `/dashboard` | Embedded Tableau dashboard |
| `/story` | Embedded Tableau story, or configuration placeholder |
| `/health` | Simple service health check |

## Troubleshooting

- **Tableau view doesn't appear:** confirm the Tableau view is published and accessible publicly, check your internet connection, and verify the URL copied from Tableau Public.
- **Story page shows a placeholder:** set `TABLEAU_STORY_URL` to the published Story's Share link, then restart/redeploy the app.
- **`py` or `python` command not found:** install Python and ensure it is available in your PATH.
- **Render deployment fails:** check the Render build and runtime logs; ensure `requirements.txt` and `Procfile` are at the repository root.
- **Embedding API errors:** use the HTTPS Tableau Public URL and test the original view directly on Tableau Public.

## Technology stack

- Python and Flask
- HTML5 and CSS3
- Tableau Embedding API v3
- Gunicorn
- Render.com

## License and data

This repository contains the web application code. The embedded visualization and its underlying data remain hosted on Tableau Public and are subject to the workbook owner's terms and Tableau's policies.
