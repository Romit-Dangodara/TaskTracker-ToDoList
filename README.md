# Tasks Tracker-ToDoList
The project is a Dockerized task tracker web app with a Python Flask backend and a simple HTML frontend. It supports CRUD operations for managing tasks, demonstrating a lightweight approach to task tracking.

It provides basic CRUD (Create, Read, Update, Delete) functionality for managing tasks. The frontend is rendered using HTML templates, and the backend handles data storage and processing. The application is containerized using Docker, making it portable and easy to deploy. Users can add, edit, and delete tasks through a user-friendly interface. 

How to deploy in the local machine:
1. Open Docker in the Background
2. Download the folder into the local machine and import it in VS Code. 
3. Open the terminal in VS Code and enter the following commands


    docker build -t TaskTracker-ToDoList .
    docker run -p 5000:5000 TaskTracker-ToDoList
