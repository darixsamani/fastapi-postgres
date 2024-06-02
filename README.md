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

## Here are the steps to follow to run the program: 
After cloning the repository, go to it. 
 1. DOCKER COMPOSE
    ```
    docker-compose up
    
    ```

 2. RUN FRIST MIGRATION
      ```
      docker-compose exec app alembic revision --autogenerate -m "first migration"
      docker-compose exec app alembic upgrade head
      ```
 3. Please turn on the LISTEN Docs app. `0.0.0.0:8081/docs`



 4. PGADMIN4
   
   access to pgadmin by specified db as name server and 5434 as port at localhost/5050
   
   username: admin@gmail.com
   password: admin
 
 5. EXAMPLE
    ![IMAGE](./img/img.png)
