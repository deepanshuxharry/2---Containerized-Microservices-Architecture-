Project 02 - Containerized Microservices App using Docker Compose!

Super excited to share a hands-on project that simulates a real-world microservices backend — containerized and orchestrated using Docker Compose! 🐳



⚙️ What I Built:

A modular, two-service architecture with:

🔹 Flask – Lightweight REST APIs for both services  

🔹 PostgreSQL – For reliable user data persistence  

🔹 Redis – For blazing-fast caching  

🔹 Docker Compose – To spin up and connect everything seamlessly  



🧩 Microservices Breakdown:

1. user-service  

  - Exposes APIs for user registration  

  - Interacts directly with PostgreSQL to store and retrieve user data  

  - Built using Flask + psycopg2



2. data-service  

  - Fetches user data and serves it via APIs  

  - Implements Redis caching to reduce DB load and improve response times  

  - Also uses Flask + Redis client for fast lookups



🔗 System Design Highlights:

- Each service runs in its own container, promoting isolation and fault tolerance  

- A custom Docker network ensures secure communication between containers  

- PostgreSQL and Redis services run as containers too — enabling full-stack containerization  

- All configurations and dependencies are handled via docker-compose.yml — no manual linking required!



📁 Source Code:  

GitHub Repo: https://github.com/Sayantan2k24/02-Containerized-Microservices-Architecture.git



💡 If you're just starting with containerized backend systems, this project is a solid entry point to learn:

- How services communicate in isolation

- Database and cache integration

- Docker Compose orchestration



My immense gratitude to Vimal Daga Sir, I got to learn a lot while working on this project.



#Docker #Flask #Microservices #Redis #PostgreSQL #DevOps #DockerCompose #BackendDevelopment #Python #Containerization

