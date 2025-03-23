# Automobile-Configuration-Platform

## Project Overview
The goal of this project is to develop a web application that allows users to explore, search, and configure automobiles. The application will provide an intuitive interface for users to browse through a catalog of vehicles, apply filters based on their preferences, and view detailed configurations. The platform will be designed to meet the client's requirements for a modern, responsive, and user-friendly experience.

### Key Features:
1. **Search Functionality**: Users can search for specific automobile models or brands.
![image](https://github.com/user-attachments/assets/3555251e-3310-4d25-8498-a5556a529f3b)
2. **Filtering Options**: Users can filter automobiles based on criteria such as price range, fuel type, transmission, and more.
![image](https://github.com/user-attachments/assets/aa16f083-0511-46ff-9cbe-c411ff715cd9)
3. **Configuration Details**: Users can view detailed configurations for each automobile, including specifications, features, and customization options.
![image](https://github.com/user-attachments/assets/430fd2a1-a0f9-4626-8c55-517b6cb4c8f1)

---

## Technical Specifications

### Frontend:
- **Framework**: Bootstrap.
- **Languages**: HTML, CSS, JavaScript.

### Backend:
- **Framework**: Python Flask.
- **Database**: MongoDB.
- **API Design**: RESTful APIs.

### Hosting and Deployment:
- **Containerization**: Docker.
- **Hosting**: Node.js.

### Plugins and Libraries:
- **Frontend**: Bootstrap plugins for UI components.
- **Backend**: Flask extensions such as MongoClient and Flask.

---

## Project Plan

### Phase 1: Requirements Gathering and Planning
- Finalize the list of features and functionalities.
- Create wireframes and mockups for the user interface.
- Define the database schema and API endpoints.

### Phase 2: Frontend Development
- Develop the user interface using Bootstrap.
- Implement search and filtering functionality using JavaScript.
- Ensure responsiveness across all devices.

### Phase 3: Backend Development
- Set up the Flask backend and connect it to the MongoDB database.
- Develop RESTful APIs for frontend-backend communication.
- Implement logic for handling search, filtering, and configuration requests.

### Phase 4: Integration and Testing
- Integrate the frontend and backend components.
- Test the application for bugs, performance issues, and security vulnerabilities.
- Gather feedback from the client and make necessary adjustments.

### Phase 5: Deployment
- Containerize the application using Docker.

---

## How to Build and Run the Application

### Prerequisites
1. **Docker**: Ensure Docker is installed on your system.
3. **Git**: Clone the repository to your local machine.

### Step 1: Clone the Repository
```bash
git clone https://github.com/banmepls/Automobile-Configuration-Platform.git
cd Automobile-Configuration-Platform
```

### Step 2: Access the Application
```bash
docker compose up --build
```

### Step 3: Build and Run the Application
- **Frontend**: Open your browser and go to http://localhost:3000 to access the frontend.
- **Backend**: The Flask backend will be running on http://localhost:5000.
- **MongoDB**: MongoDB will be accessible internally within the Docker network.


### Step 4: Stop the Application
```bash
docker compose down
```

---

## Conclusion
This project aims to deliver a scalable, responsive, and user-friendly automobile configuration platform. By leveraging Bootstrap for the frontend, Python Flask for the backend, and MongoDB for the database, we ensure a robust and efficient solution. The use of Docker for deployment guarantees consistency and ease of management across environments.
