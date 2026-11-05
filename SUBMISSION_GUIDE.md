# Submission Guide

Project: Deploy a Serverless Resume API on AWS.

Run locally:
1. `python -m venv venv`
2. `venv\\Scripts\\Activate.ps1` (Windows PowerShell)
3. `pip install -r requirements.txt`
4. `python local_api.py`
5. Open `http://127.0.0.1:5000/`.
6. Call API endpoints with header `x-api-key: local-demo-key`.
7. Run `python -m pytest -v`.

Before submitting, replace placeholder contact details, college name, internship organization and dates in `data/resume.json`.

Deployment note: The SAM template defines AWS resources, but a live AWS deployment was not performed because no AWS account was available. Flask and Moto provide local demonstration/testing only.
