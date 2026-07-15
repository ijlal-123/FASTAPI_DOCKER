\# Automated CI/CD Pipeline \& Containerized API



\## Overview

This project demonstrates foundational Site Reliability Engineering (SRE) and DevOps practices. It features a high-performance Python REST API (FastAPI) that is containerized using Docker and integrated with an automated Continuous Integration/Continuous Deployment (CI/CD) pipeline via GitHub Actions.



\## Technologies Used

\* \*\*Programming Language:\*\* Python (FastAPI)

\* \*\*Containerization:\*\* Docker

\* \*\*CI/CD:\*\* GitHub Actions

\* \*\*Version Control:\*\* Git \& GitHub

\* \*\*Testing:\*\* Pytest



\## Architecture \& Features

1\. \*\*Health Check Endpoints:\*\* Simulated metrics and health monitoring endpoints.

2\. \*\*Infrastructure as Code:\*\* A `Dockerfile` configures the precise environment needed to run the application securely and consistently.

3\. \*\*Automated Testing:\*\* Unit tests run automatically on every commit to ensure code reliability.

4\. \*\*Automated Builds:\*\* GitHub Actions pipeline automatically validates dependencies, runs tests, and builds the Docker image.



\## How to Run Locally

1\. Clone the repository: `git clone <your-repo-link>`

2\. Build the image: `docker build -t sre-api .`

3\. Run the container: `docker run -p 8000:8000 sre-api`

4\. Access the API at `http://localhost:8000`

