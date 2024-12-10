## Overview
This guide provides instructions to set up, run, and deploy a Java-based application built with Maven and Spring Boot, alongside an integrated Flask-based Python backend. Follow the steps below for configuring the environment, compiling code, and executing the application on both Java and Python platforms.

---

## Running the Java Code (Terminal Version)
The terminal-based version of the application has no additional dependencies. To run:
1. Ensure the code folder is in the correct path.
2. Compile all the Java files.
3. Run the application by executing the `Main.java` file.

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
.vscode/ src/ └── main/ └── java/ └── com/ └── eventmanagement/ ├── controller/ │ ├── EventController.java │ ├── RoomController.java │ └── UserController.java ├── model/ │ ├── Event.java │ ├── Manage.java │ ├── Role.java │ ├── RoomInfo.java │ └── User.java ├── repository/ │ ├── EventRepository.java │ ├── RoomRepository.java │ └── UserRepository.java ├── service/ │ ├── EventService.java │ ├── EventServiceImpl.java │ ├── RoomService.java │ ├── RoomServiceImpl.java │ ├── UserService.java │ └── UserServiceImpl.java ├── utils/ │ └── JwtTokenUtils.java └── Main.java resources/ └── application.properties target/ Pom.xml
