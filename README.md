## Overview
This guide provides instructions to set up, run, and deploy a Java-based application built with Maven and Spring Boot, alongside an integrated Flask-based Python backend. Follow the steps below for configuring the environment, compiling code, and executing the application on both Java and Python platforms.

---

## Running the Maven-Based Application
The main application is built as a Maven Project and uses Spring Boot as its framework.

### Prerequisites
1. Maven must be installed.
2. Install Spring Boot dependencies.
3. (Optional) If using VS Code, create a simple Maven project:
   - Open VS Code and click on **Create New Project**.
   - Select **Maven**.
   - Choose **maven-archetype-quickstart** as the archetype.
   - Set the version to 1.4.
   - Enter the group ID as `com.JavaRestfulAPIs`.
   - Name the project `eventmanagement`.
   - Choose a directory for the Maven project and note the path for future reference.

---

## Project Directory Structure
.vscode/
src/
└── main/
    └── java/
        └── com/
            └── eventmanagement/
                ├── controller/
                │   ├── EventController.java
                │   ├── RoomController.java
                │   └── UserController.java
                ├── model/
                │   ├── Event.java
                │   ├── Manage.java
                │   ├── Role.java
                │   ├── RoomInfo.java
                │   └── User.java
                ├── repository/
                │   ├── EventRepository.java
                │   ├── RoomRepository.java
                │   └── UserRepository.java
                ├── service/
                │   ├── EventService.java
                │   ├── EventServiceImpl.java
                │   ├── RoomService.java
                │   ├── RoomServiceImpl.java
                │   ├── UserService.java
                │   └── UserServiceImpl.java
                ├── utils/
                │   └── JwtTokenUtils.java
                └── Main.java
resources/
└── application.properties
target/
Pom.xml


---

### Dependencies to Install (for VS Code)
1. Maven for Java
2. Spring Boot Extension Pack
3. Spring Boot Tools
4. Spring Initializr Java Support
5. Spring Boot Dashboard

### Running the Maven Project
1. Build the Maven project using:
   mvn clean mvn install
2. Execute the application:
   cd "c:\path\to\project" java -jar target/eventmanagement.jar
Or, right-click on `Main.java` in VS Code and select **Run Java**.

---

## Running the Flask Backend
The Python backend is built using Flask.

### Prerequisites
1. Python installed on your machine.
2. Create a virtual environment and install dependencies.

### Steps to Run
1. Navigate to the Flask project folder:
   cd path/to/flask_project
2. Set up a virtual environment:
   python -m venv venv .\venv\Scripts\Activate
3. Install dependencies:
   pip install Flask Flask-WTF WTForms Flask-SQLAlchemy flask-login requests
4. Run the Flask application:
   python app.py
5. Once the server starts, access the application at:
[http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## Important Notes
1. Always start the Maven project (Java) before running the Flask backend (Python).
2. Ensure directory structures and paths match the configurations to avoid errors.

