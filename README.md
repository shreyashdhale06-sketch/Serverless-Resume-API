# Serverless Resume API

A serverless Resume API built using **Python, AWS Lambda, API Gateway, and DynamoDB**. This project provides structured REST API endpoints to access resume information, including personal details, education, experience, skills, and projects.

It also includes API key authentication, local development support, and automated testing.

## Features

- **Serverless Architecture:** Designed using AWS Lambda and API Gateway.
- **DynamoDB Integration:** Stores and manages structured resume data.
- **API Key Authentication:** Protects API endpoints from unauthorized access.
- **Multiple API Endpoints:** Access different sections of the resume independently.
- **Local Development:** Run and test the API locally using Flask.
- **Automated Testing:** Includes pytest-based test cases.
- **AWS Simulation:** Uses Moto to simulate AWS services during local testing.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| AWS Lambda | Serverless execution |
| Amazon API Gateway | API management |
| Amazon DynamoDB | Database |
| Flask | Local API development |
| Moto | AWS service simulation |
| Pytest | Automated testing |
| AWS SAM | Serverless application configuration |

## Project Structure

```text
Serverless-Resume-API/
│
├── data/
│   └── resume.json
│
├── lambda/
│   └── app.py
│
├── tests/
│   └── test_api.py
│
├── local_api.py
├── requirements.txt
├── template.yaml
├── ARCHITECTURE.md
├── SUBMISSION_GUIDE.md
└── .gitignore
```

## API Endpoints

The local API provides the following endpoints:

| Endpoint | Description |
|---|---|
| `/` | API welcome information |
| `/resume` | Complete resume information |
| `/resume/personal` | Personal details |
| `/resume/experience` | Work experience |
| `/resume/education` | Educational details |
| `/resume/skills` | Technical skills |
| `/resume/projects` | Project information |

### Authentication

API requests require an API key in the request header.

```text
x-api-key: local-demo-key
```

Requests without a valid API key are rejected.

## Installation and Setup

###
