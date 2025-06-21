# FASTAPI-POSTGRESQL
Template for building FastAPI Asynchronous applications with PostgreSQL

# Features
 - Python FastAPI backend
 - POSTGRESQL Database
 - Docker-Compose
 - Authentification
 - Migration with Alembic
 - PGADMIN4 for Graphical Database Visualization
 - Asynchronous
 - Support SQLmodel

## Here are the steps to follow to run the program: 
After cloning the repository, go to it. 
 1. DOCKER COMPOSE
    ```
    docker compose up -d --build
    
    ```

 2. RUN FRIST MIGRATION
      ```
      docker compose exec app uv run alembic revision --autogenerate -m "first migration"
      docker compose exec app uv run alembic upgrade head
      ```
 3. Please turn on the LISTEN Docs app. `0.0.0.0:8001/docs`



 4. PGADMIN4
   
   access to pgadmin by specified db as name server and 5434 as port at localhost/5050
   
   username: admin@gmail.com
   password: admin

   Please turn on the LISTEN Docs app. `0.0.0.0:5050`
 
 5. EXAMPLE
    ![IMAGE](./img/img.png)
