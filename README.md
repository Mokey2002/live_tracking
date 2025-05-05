project/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── routes/
│   │   │   │   ├── fleet.py
│   │   │   │   └── analytics.py
│   │   │   └── deps.py
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   └── security.py
│   │   ├── models/
│   │   │   ├── truck.py
│   │   │   └── location.py
│   │   ├── services/
│   │   │   ├── kafka_consumer.py
│   │   │   └── location_cache.py
│   │   ├── tasks/
│   │   │   └── analytics.py
│   │   ├── main.py
│   │   └── database.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── .env
├── infra/
│   ├── docker-compose.yml
│   └── terraform/
│       ├── main.tf
│       ├── variables.tf
│       └── outputs.tf
├── tests/
│   ├── test_fleet.py
│   ├── test_analytics.py
│   └── conftest.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── README.md
│
│   # FleetOps - Real-Time Fleet Management Backend
│
│   ## 🎯 Project Overview
│   FleetOps is a real-time fleet tracking backend system designed to ingest, store, and analyze GPS data from moving vehicles. It simulates a real-world logistics platform with microservices, event streaming, caching, background tasks, and cloud infrastructure.
│
│   ## 🛠 Tech Stack
│   - **FastAPI** for API development
│   - **Kafka** for real-time message streaming
│   - **PostgreSQL** for relational data storage
│   - **Redis** for caching
│   - **Celery** for background analytics tasks
│   - **Docker** and **Docker Compose** for local development
│   - **Terraform** for AWS infrastructure
│   - **GitHub Actions** for CI/CD
│
│   ## 📚 Learning Goals
│   - Design RESTful APIs with FastAPI
│   - Stream and process data in real time with Kafka
│   - Model and persist structured data using SQL and ORMs
│   - Cache dynamic data for low-latency access with Redis
│   - Run background tasks asynchronously using Celery
│   - Set up local dev environments with Docker Compose
│   - Write and maintain unit/integration tests with pytest
│   - Deploy infrastructure-as-code using Terraform
│   - Monitor services and set up basic observability
│   - Practice scalable, production-ready backend design
│
│   ## 🧪 How to Run Locally
│   1. Ensure Docker and Docker Compose are installed
│   2. Copy `.env.example` to `.env` and update variables
│   3. Run `docker compose up --build`
│   4. Visit `http://localhost:8000/docs` for the API docs
│   5. Run tests with `pytest`
│
│   ## 🔋 Future Enhancements
│   - WebSocket support for live UI updates
│   - React dashboard with Leaflet for tracking
│   - S3 integration for file uploads
│   - Kubernetes deployment
└── Makefile

