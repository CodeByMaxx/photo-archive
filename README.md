# Photo Archive

A simple self-hosted photo archive built with **Flask** and **Docker**.

The application provides a lightweight web interface for storing and browsing photos through a containerized Flask application.

## Overview

```text
┌───────────────┐
│    Browser    │
└───────┬───────┘
        │
        │ HTTP
        ▼
┌───────────────┐
│     Flask     │
│      App      │
└───────┬───────┘
        │
        ▼
   Photo Storage
```

The project is intentionally kept small and focuses on providing a simple photo-archive application that can be started with Docker Compose.

## Technology Stack

| Component        | Technology     |
| ---------------- | -------------- |
| Backend          | Flask          |
| Language         | Python         |
| Containerization | Docker         |
| Orchestration    | Docker Compose |
| Interface        | Web browser    |

## Project Structure

```text
photo-archive/
├── app/
├── Dockerfile
├── docker-compose.yml
├── Image1.png
├── image.png
├── requirements.txt
└── README.md
```

## Features

* Web-based photo archive
* Flask backend
* Docker-based deployment
* Docker Compose setup
* Local self-hosted deployment
* Browser-based access

## Screenshots

The repository contains the existing application images:

### Application

![Application](Image1.png)

### Archive

![Archive](image.png)

These images are part of the repository and are intentionally kept as part of the project documentation.

## Requirements

You need:

* Docker
* Docker Compose

No local Python installation is required when running the application through Docker.

## Start the Application

Clone the repository:

```bash
git clone https://github.com/CodeByMaxx/photo-archive.git
cd photo-archive
```

Build and start the application:

```bash
docker compose up --build
```

If your Docker setup requires elevated privileges:

```bash
sudo docker compose up --build
```

The application can then be accessed at:

```text
http://localhost:5000/
```

## Stop the Application

Stop the running containers with:

```bash
docker compose down
```

To rebuild the application after changes:

```bash
docker compose up --build
```

## Development

The Flask application is located in:

```text
app/
```

Python dependencies are defined in:

```text
requirements.txt
```

The container configuration is defined in:

```text
Dockerfile
```

while the complete local service setup is defined in:

```text
docker-compose.yml
```

## Docker Architecture

The application is designed to run as a containerized service:

```text
Docker Compose
      │
      ▼
┌───────────────┐
│ Photo Archive │
│    Flask      │
└───────┬───────┘
        │
        ▼
      :5000
        │
        ▼
     Browser
```

This makes the application easy to reproduce on another machine without manually installing the Python runtime and dependencies.

## Project Goals

The project demonstrates a compact example of:

* Flask web application development
* Containerized Python applications
* Docker image creation
* Docker Compose deployment
* Local self-hosted web applications

It is intentionally much smaller than the data-engineering projects in the portfolio and serves as a focused example of **Python web development and containerization**.

## Possible Extensions

Potential future improvements could include:

* User authentication
* Multiple users
* Photo upload through the web interface
* Thumbnail generation
* EXIF metadata extraction
* Search and filtering
* Albums
* Tags
* Date-based navigation
* Persistent database storage
* Object storage support
* Automatic image resizing
* Docker health checks
* Automated tests
* CI/CD

## License

See the repository for the current project license.

