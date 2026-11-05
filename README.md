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

### 1. Clone the Repository

```bash
git clone https://github.com/shreyashdhale06-sketch/Serverless-Resume-API.git
```

### 2. Navigate to the Project

```bash
cd Serverless-Resume-API
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the API Locally

Start the Flask development server:

```bash
python local_api.py
```

Open the following address in your browser:

```text
http://127.0.0.1:5000/
```

## Test the API

Run the automated test suite:

```bash
python -m pytest -v
```

The project includes seven automated tests covering API functionality, authentication, invalid sections, and HTTP methods.

## Example API Request

Using PowerShell:

```powershell
$headers = @{"x-api-key"="local-demo-key"}

Invoke-RestMethod `
-Uri "http://127.0.0.1:5000/resume/skills" `
-Headers $headers
```

## Security

- API key authentication is used to protect endpoints.
- Unauthorized requests are rejected.
- Sensitive configuration values should not be committed to the repository.
- The local demo API key is intended for development and testing only.

## Future Improvements

- Deploy the API to AWS Lambda.
- Connect a live DynamoDB database.
- Implement secure API key management.
- Add a frontend resume portfolio.
- Add more API endpoints and features.

## Author

**Shreyash Dhale**

BSc Computer Science

GitHub: [shreyashdhale06-sketch](https://github.com/shreyashdhale06-sketch)

---

*This project demonstrates serverless application development, REST API design, database integration, authentication, and automated testing using Python and AWS technologies.*
