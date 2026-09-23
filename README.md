# Photo Archive

A small photo archive web application built with **Python, Flask and Docker**.

The application provides a simple browser-based gallery where images can be uploaded, displayed and deleted.

---

## Features

* Image gallery
* Image upload
* Image deletion
* Docker support
* Docker Compose configuration
* Persistent upload directory
* Secure upload filenames with Werkzeug

---

## Technology Stack

| Component               | Technology               |
| ----------------------- | ------------------------ |
| Language                | Python 3.12              |
| Web Framework           | Flask 3.0.3              |
| WSGI/Application Server | Flask development server |
| Container               | Docker                   |
| Orchestration           | Docker Compose           |
| Port                    | `5000`                   |

The repository also contains Flask-SQLAlchemy and Pillow as dependencies, but the current `app.py` does not use them in the active gallery/upload workflow.

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

The current GitHub repository contains the application, Docker configuration, requirements and two image assets.

---

## How It Works

The current application uses the following storage path:

```text
app/uploads/thumbs/
```

When the application starts, this directory is created if it does not already exist.

```python
UPLOAD_FOLDER = os.path.join(
    os.path.dirname(__file__),
    "uploads"
)

THUMB_FOLDER = os.path.join(
    UPLOAD_FOLDER,
    "thumbs"
)
```

The gallery then reads the files from this directory.

> **Note:** The `thumbs` directory is currently used as the image storage directory. The application does not currently generate thumbnails with Pillow.

---

## Application Routes

### Gallery

```text
GET /
```

Displays the images found in:

```text
app/uploads/thumbs/
```

The filenames are passed to the gallery template.

### Upload

```text
POST /upload
```

The application expects an uploaded file under the form field:

```text
file
```

The filename is passed through Werkzeug's `secure_filename()` before the file is saved.

### Serve Images

```text
GET /uploads/<filename>
```

Uploaded files are served from the `thumbs` directory.

### Delete

```text
POST /delete/<filename>
```

The selected file is removed from the upload directory.

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

The Compose configuration exposes:

```text
localhost:5000
```

and mounts:

```text
./app/uploads
```

to:

```text
/app/app/uploads
```

inside the container.

Open:

```text
http://localhost:5000
```

---

## Stop the Container

Stop the application with:

```bash
docker compose down
```

---

## Docker Configuration

The Docker image is based on:

```text
python:3.12-slim
```

The image:

1. creates `/app`
2. installs `requirements.txt`
3. copies the repository into the container
4. exposes port `5000`
5. starts `python app/app.py`

This behaviour is defined in the current `Dockerfile`.

---

## Local Development

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

Start the application:

```bash
python app/app.py
```

Then open:

```text
http://localhost:5000
```

---

## Persistence

Docker Compose mounts:

```text
./app/uploads
```

into the container.

This means uploaded files are stored on the host filesystem and are not lost when the container itself is recreated.

For a production deployment, a dedicated persistent storage solution or object storage would be preferable.

---

## Database Model

The repository contains an SQLAlchemy model:

```python
class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255))
```

However, the current `app.py` does not initialize or use this database model for the active upload/gallery workflow.

This can serve as a foundation for a future database-backed version.

---

## Screenshots

The repository contains two image assets:

```text
Image1.png
image.png
```

They can be used as documentation/examples for the project.

---

## Security Notes

The current implementation uses `secure_filename()` for uploaded filenames, which helps prevent unsafe filenames.

For production use, additional security measures should be added:

* validate file types
* limit upload size
* generate unique filenames
* add authentication
* add CSRF protection
* disable Flask debug mode
* use a production WSGI server
* separate uploaded files from application source
* restrict access to uploaded content

The current application starts Flask with:

```python
debug=True
```

so it should **not be exposed directly to the public internet in its current form**.

---

## Current Scope

The current application intentionally remains small:

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

It is a simple foundation for a personal photo archive.

---

## Possible Improvements

Future versions could add:

* automatic thumbnail generation
* EXIF metadata
* albums
* tags
* search
* pagination
* image metadata
* duplicate detection
* authentication
* database-backed image records
* object storage such as Amazon S3
* automated tests
* production WSGI deployment

---

## Author

**Markus**

