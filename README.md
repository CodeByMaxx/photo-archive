# Photo Archive

A simple photo archive web application built with **Python, Flask, Flask-SQLAlchemy, Pillow and Docker**.

The application provides a lightweight web interface for uploading, viewing and deleting images. The application runs inside a Docker container and exposes the web interface on port `5000`.

---

## Features

* 🖼️ Image gallery
* ⬆️ Image upload
* 🗑️ Image deletion
* 🐳 Docker support
* 💾 Persistent upload storage through Docker volumes
* 🗄️ SQLite/SQLAlchemy-ready data model
* 🔐 Secure filenames using Werkzeug
* 🐍 Python 3.12

---

## Architecture

```text
Browser
   │
   ▼
Flask Web Application
   │
   ├── Gallery
   ├── Upload
   └── Delete
   │
   ▼
Image Storage
   │
   └── app/uploads/
          │
          └── thumbs/
```

The application is packaged as a Docker container and exposes Flask on port `5000`.

---

## Technology Stack

| Component        | Technology               |
| ---------------- | ------------------------ |
| Language         | Python 3.12              |
| Web Framework    | Flask 3.0.3              |
| ORM              | Flask-SQLAlchemy 3.1.1   |
| Image Processing | Pillow 11.0.0            |
| Web Server       | Flask development server |
| Containerization | Docker                   |
| Orchestration    | Docker Compose           |
| Port             | `5000`                   |

The dependencies are defined in `requirements.txt`.

---

## Project Structure

```text
photo-archive/
│
├── app/
│   ├── app.py
│   ├── models.py
│   ├── templates/
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

The Flask entry point is `app/app.py`. The Docker image also starts this file directly.

---

## Application

The Flask application provides a simple gallery interface.

### Gallery

The root route displays the available images:

```text
GET /
```

The application reads the image files from:

```text
app/uploads/thumbs/
```

and renders them through the gallery template.

### Upload

Images can be uploaded through:

```text
POST /upload
```

Uploaded filenames are processed with Werkzeug's `secure_filename()` before being stored.

### Serve Images

Uploaded images are served through:

```text
GET /uploads/<filename>
```

### Delete

Images can be removed through:

```text
POST /delete/<filename>
```

The application checks that the target file exists before deleting it.

---

## Docker

The project uses a minimal Python 3.12 image:

```dockerfile
FROM python:3.12-slim
```

Dependencies are installed from `requirements.txt`, the application is copied into the container and port `5000` is exposed. The container starts with:

```text
python app/app.py
```

---

## Run with Docker Compose

Clone the repository:

```bash
git clone https://github.com/CodeByMaxx/photo-archive.git
cd photo-archive
```

Start the application:

```bash
docker compose up --build
```

The repository's Compose configuration builds the application and maps:

```text
5000:5000
```

It also mounts the upload directory:

```text
./app/uploads:/app/app/uploads
```

so uploaded files remain outside the container lifecycle.

Open the application in your browser:

```text
http://localhost:5000
```

---

## Stop the Application

Press:

```text
Ctrl+C
```

or stop the Compose stack with:

```bash
docker compose down
```

---

## Local Development

The project can also be run directly with Python.

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

### Linux / macOS

```bash
source .venv/bin/activate
```

### Windows

```powershell
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start Flask:

```bash
python app/app.py
```

Then open:

```text
http://localhost:5000
```

---

## Data Persistence

Docker Compose mounts:

```text
./app/uploads
```

into:

```text
/app/app/uploads
```

inside the container. This means uploaded images are stored in the repository's `app/uploads` directory rather than only inside the container.

For a production deployment, uploaded photos should generally be stored separately from the application source tree, for example on dedicated persistent storage or object storage.

---

## Data Model

The project already contains a SQLAlchemy model for images:

```python
class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255))
```

This provides a foundation for extending the application with database-backed image metadata.

Possible future metadata includes:

* original filename
* upload timestamp
* file size
* MIME type
* image dimensions
* EXIF metadata
* album/category
* description

---

## Security Considerations

The application uses Werkzeug's `secure_filename()` when handling uploaded filenames.

For production use, additional protections should be added:

* restrict allowed image formats
* validate MIME types
* limit upload sizes
* generate unique storage filenames
* disable Flask debug mode
* add authentication
* add CSRF protection
* store uploads outside the source tree
* avoid exposing arbitrary uploaded files
* use a production WSGI server

---

## Screenshots

The repository contains example images that can be used to document the application:

![Photo Archive](Image1.png)

![Photo Archive](image.png)

---

## Current Scope

This project is intentionally lightweight.

The current implementation focuses on the basic photo-management workflow:

```text
Upload
  │
  ▼
Store
  │
  ▼
Display
  │
  ▼
Delete
```

It provides a small foundation that can be extended into a more complete personal photo archive.

---

## Possible Improvements

Future development could include:

* image thumbnails generated with Pillow
* EXIF metadata extraction
* search and filtering
* albums
* tags
* pagination
* image previews
* duplicate detection
* authentication
* user accounts
* database-backed image management
* object storage such as Amazon S3
* background image processing
* production WSGI server
* automated tests
* CI/CD

---

## License

No license file is currently visible in the repository.

If this project is intended to be publicly reusable, add an appropriate `LICENSE` file.

---

## Author

**Markus**

