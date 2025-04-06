# Cargo Command ISS Optimizer

## Overview
This repository contains the frontend and backend for the Cargo Command ISS Optimizer application. The application helps manage and optimize cargo operations in a space station like the International Space Station (ISS).

## Directory Structure
- `backend/`: Contains the backend code implemented using FastAPI and SQLite.
- `frontend/`: Contains the frontend code implemented using Next.js and React.

## Setup Instructions

### Prerequisites
- [Git](https://git-scm.com/)
- [Python 3.8+](https://www.python.org/downloads/)
- [Node.js 14+](https://nodejs.org/)
- [npm](https://www.npmjs.com/)
- [Visual Studio Code (VS Code)](https://code.visualstudio.com/)

### Clone the Repository
1. Open a terminal or command prompt.
2. Navigate to the directory where you want to clone the repository.
3. Run the following command to clone the repository:
   ```sh
   git clone https://github.com/ninaadsaxena/cargo-command-iss-optimiser.git
   ```

### Backend Setup
1. Navigate to the `backend` directory:
   ```sh
   cd cargo-command-iss-optimiser/backend
   ```

2. Create a virtual environment:
   ```sh
   python -m venv venv
   ```

3. Activate the virtual environment:
   - **Windows**:
     ```sh
     venv\Scripts\activate
     ```
   - **Mac/Linux**:
     ```sh
     source venv/bin/activate
     ```

4. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

5. Initialize the SQLite database:
   ```sh
   python -c "from database import init_db; init_db()"
   ```

6. Run the backend server:
   ```sh
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

### Frontend Setup
1. Open a new terminal or command prompt.
2. Navigate to the `frontend` directory:
   ```sh
   cd cargo-command-iss-optimiser/frontend
   ```

3. Install the required dependencies:
   ```sh
   npm install
   ```

4. Create a `.env` file in the `frontend` directory and add the following environment variable:
   ```env
   NEXT_PUBLIC_API_URL=http://localhost:8000/api
   ```

5. Run the frontend application:
   ```sh
   npm start
   ```

### Running the Application
1. Ensure both the backend and frontend servers are running.
2. Open your web browser and navigate to `http://localhost:3000`.

## Docker Setup (Optional)
You can also use Docker to run the application.

1. Navigate to the root directory of the project:
   ```sh
   cd cargo-command-iss-optimiser
   ```

2. Build the Docker images for both frontend and backend:
   ```sh
   docker-compose build
   ```

3. Run the application using Docker Compose:
   ```sh
   docker-compose up
   ```

## Environment Variables
- `NEXT_PUBLIC_API_URL`: The API endpoint for the backend.

## License
This project is licensed under the MIT License.
