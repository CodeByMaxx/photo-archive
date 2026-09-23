# Photo Archive

A small self-hosted photo gallery built with **Flask** and **Docker**.

The application provides a simple web interface for uploading, viewing, and deleting photos. Uploaded files are stored on the local filesystem and can be persisted with the included Docker Compose volume configuration.

> **Project status:** This is a lightweight personal project and is not intended to be a production-grade photo management system.

---

## Features

* Flask-based web application
* Web gallery for uploaded photos
* Photo upload
* Photo deletion
* Persistent uploads with Docker volumes
* Docker and Docker Compose support
* Simple local filesystem storage
* Pillow available for image processing

---

## Tech Stack

| Component        | Technology       |
| ---------------- | ---------------- |
| Language         | Python           |
| Web Framework    | Flask            |
| Database Layer   | Flask-SQLAlchemy |
| Image Processing | Pillow           |
| Containerization | Docker           |
| Orchestration    | Docker Compose   |

---

## Project Structure

```text
photo-archive/
│
├── app/
│   ├── app.py
│   ├── models.py
│   ├── templates/
│   ├── static/
│   └── uploads/
│       └── thumbs/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── Image1.png
├── image.png
└── README.md
```

The exact contents of `templates/` and `static/` may change as the UI evolves.

---

## How It Works

The Flask application uses a local upload directory:

```text
app/uploads/
```

Thumbnails are currently stored in:

```text
app/uploads/thumbs/
```

The gallery reads the available thumbnail files and displays them through the web interface.

Uploaded files are handled by the Flask application and stored on the local filesystem.

---

## Running with Docker

The easiest way to run the application is Docker Compose.

Build and start the application:

```bash
docker compose up --build
```

The application is exposed on:

```text
http://localhost:5000
```

Open that address in a browser.

To stop the application:

```bash
docker compose down
```

---

## Persistent Storage

The Docker Compose configuration mounts the local upload directory into the container:

```text
./app/uploads:/app/app/uploads
```

This means uploaded photos remain available when the container is recreated.

The photos are therefore stored on the host machine under:

```text
app/uploads/
```

Make sure this directory is included in your backup strategy if the photos are important.

---

## Running Without Docker

A local Python environment can also be used.

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it on Linux/macOS:

```bash
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Start the Flask application:

```bash
python app/app.py
```

The application listens on:

```text
http://localhost:5000
```

---

## Photo Upload

Photos can be uploaded through the web interface.

The application uses Werkzeug's `secure_filename()` when processing uploaded filenames.

The current implementation does not provide a comprehensive image-validation or media-security pipeline, so this project should be treated as a personal/local application rather than an internet-facing upload service.

---

## Photo Deletion

The application also provides a delete operation for uploaded files.

Deleted files are removed from the local upload directory.

Because the application operates directly on the filesystem, backups should be maintained separately if the stored photos are valuable.

---

## Database

The project includes a SQLAlchemy model:

```text
app/models.py
```

The current application, however, does not use the database model as the primary storage mechanism for the gallery.

The current gallery is filesystem-based.

This leaves room for a future metadata/database layer containing information such as:

* original filename
* upload timestamp
* image dimensions
* file type
* tags
* albums
* descriptions

---

## Configuration

The application currently has no complex external configuration system.

The main application settings are defined in:

```text
app/app.py
```

The default Flask development server listens on:

```text
0.0.0.0:5000
```

---

## Development

The application currently runs Flask with:

```python
debug=True
```

This is useful during development but should **not** be used for an internet-facing production deployment.

For a production deployment, use an appropriate WSGI server and put the application behind a reverse proxy where required.

---

## Screenshots

The repository contains example images that can be used to document the application interface.

Recommended screenshots:

* gallery overview
* photo upload
* uploaded photo
* delete operation

---

## Current Limitations

The current implementation is intentionally simple.

Known limitations include:

* filesystem-based photo storage
* no authentication
* no user management
* no album management
* no search
* no metadata management
* no dedicated production WSGI configuration
* limited upload validation
* database model is not currently integrated into the main gallery workflow

These are potential areas for future development.

---

## Possible Improvements

Future versions could add:

* image type and size validation
* automatic thumbnail generation
* EXIF metadata extraction
* albums and tags
* search and filtering
* authentication
* database-backed photo metadata
* image pagination
* production WSGI configuration
* automated tests
* backup functionality

---

## License

No license file is currently included in the repository.

Unless a license is added, the project should be treated as **all rights reserved**.

---

## Author

**Markus**

Personal Python / Flask project.

