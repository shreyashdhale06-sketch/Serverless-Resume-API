# Architecture

Client -> API Gateway (API key and usage plan) -> Python Lambda -> DynamoDB.

On the first request, Lambda reads the packaged `data/resume.json` and seeds DynamoDB if the table has no resume records. It then returns the requested section from DynamoDB.

## DynamoDB schema
Partition key: `PK` (String), value `RESUME`.
Sort key: `SK` (String), values PERSONAL, EXPERIENCE, EDUCATION, SKILLS, PROJECTS.
Other attributes: `section` and `content`.

## Security and efficiency
The SAM template requires an API key and defines a usage plan of 5 requests/second, burst 10, and 1,000 requests/day. DynamoDB uses on-demand billing and encryption at rest. Lambda receives table-scoped DynamoDB permissions. API keys are for usage control, not strong user authentication; production private data should use Cognito/JWT or IAM authorization.
