"""Flask web application embedding a Tableau Public Olympics dashboard and story."""

import os
from flask import Flask, render_template

app = Flask(__name__)

# Tableau Public view URLs. Set TABLEAU_STORY_URL in your environment once
# your published Tableau Story URL is available.
TABLEAU_DASHBOARD_URL = os.getenv(
    "TABLEAU_DASHBOARD_URL",
    "https://public.tableau.com/views/smartbridge_17932641696630/OlympicDashboard",
).strip()
TABLEAU_STORY_URL = os.getenv("TABLEAU_STORY_URL", "").strip()
TABLEAU_PROFILE_URL = os.getenv(
    "TABLEAU_PROFILE_URL",
    "https://public.tableau.com/app/profile/aarna.vyas",
).strip()


def common_context():
    return {
        "dashboard_url": TABLEAU_DASHBOARD_URL,
        "story_url": "https://public.tableau.com/views/smartbridge_17932641696630/Story1?:language=en-GB&publish=yes&:sid=&showOnboarding=true&:display_count=n&:origin=viz_share_link",
        "tableau_profile_url": TABLEAU_PROFILE_URL,
    }


@app.route("/")
def index():
    return render_template("index.html", **common_context())


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", **common_context())


@app.route("/story")
def story():
    return render_template("story.html", **common_context())


@app.route("/health")
def health():
    return {"status": "ok"}, 200


if __name__ == "__main__":
    # Local development only. Render runs the app with Gunicorn via the Procfile.
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")), debug=True)
