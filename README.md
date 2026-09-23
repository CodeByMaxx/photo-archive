# Photo Archive

A small photo archive application built with **Flask**, **SQLAlchemy**, **Pillow**, and **Docker**.

The project provides a simple web interface for uploading, viewing, and deleting photos. It is primarily a compact demonstration project for a containerized Flask application with persistent photo storage.

## ✨ Features

* Upload photos through a web interface
* Display stored photos in a gallery
* Delete photos
* Persistent storage using Docker volumes
* SQLite database via SQLAlchemy
* Image handling with Pillow
* Docker and Docker Compose support
* Simple Flask-based web application

## 🛠️ Technology Stack

* **Python**
* **Flask**
* **SQLAlchemy**
* **Pillow**
* **SQLite**
* **Docker**
* **Docker Compose**
* **HTML / CSS**

## 📸 Result

The application provides a simple photo archive with a web-based gallery.

![Photo Archive](Image1.png)

![Photo Archive Application](image.png)

## 📂 Project Structure

```text
photo-archive/
├── app/
│   ├── app.py
│   ├── models.py
│   ├── templates/
│   └── ...
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── Image1.png
├── image.png
└── README.md
```

## 🚀 Run with Docker

Build and start the application with Docker Compose:

```bash
docker compose up --build
```

The application is then available at:

```text
http://localhost:5000/
```

To stop the application:

```bash
docker compose down
```

## 🐳 Docker

The application is containerized so that the required Python environment and dependencies can be started consistently.

Docker Compose is used to simplify the local setup and to keep uploaded data persistent through the configured volume.

## 🖼️ Application Workflow

The basic workflow is:

```text
Upload Photo
     │
     ▼
 Flask Application
     │
     ├── Store Photo
     └── Store Metadata
     │
     ▼
 Photo Gallery
     │
     ▼
 View / Delete
```

## 📦 Persistence

Uploaded photos are stored outside the temporary container filesystem through the Docker volume configuration.

This means that restarting the container does not automatically remove the stored application data.

## 🔐 Security Considerations

This project is intentionally kept simple and is primarily intended as a portfolio/demo application.

For a production deployment, additional measures would be appropriate, including:

* file type and file size validation
* stronger upload restrictions
* authentication and authorization
* CSRF protection
* production WSGI server configuration
* secure deployment configuration
* more comprehensive error handling

## 🧪 Development

Install the Python dependencies locally with:

```bash
pip install -r requirements.txt
```

The Docker setup is the recommended way to run the application consistently.

## 🎯 Purpose

The main purpose of this project is to demonstrate:

* Flask application development
* database integration with SQLAlchemy
* image handling with Pillow
* Docker containerization
* persistent application storage
* a simple web-based CRUD workflow

It is deliberately smaller than the larger data, cloud, and streaming projects in the portfolio.

## 🔮 Possible Improvements

Potential future improvements include:

* image thumbnails
* image metadata
* search and filtering
* authentication
* pagination
* improved frontend styling
* automated tests
* object storage such as Amazon S3
* production deployment

## 📄 License

No license file is currently included in the repository. If this project is intended for reuse by others, an explicit open-source license can be added.

---

**Project:** Photo Archive
**Author:** Markus

