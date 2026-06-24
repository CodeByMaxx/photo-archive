import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)

# ✅ FIXED: single clean path
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), "uploads")
THUMB_FOLDER = os.path.join(UPLOAD_FOLDER, "thumbs")

os.makedirs(THUMB_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# -----------------------
# GALLERY
# -----------------------
@app.route("/")
def gallery():
    images = os.listdir(THUMB_FOLDER)
    return render_template("gallery.html", images=images)


# -----------------------
# UPLOAD
# -----------------------
@app.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("file")

    if not file:
        return redirect(url_for("gallery"))

    filename = secure_filename(file.filename)

    save_path = os.path.join(THUMB_FOLDER, filename)
    file.save(save_path)

    return redirect(url_for("gallery"))


# -----------------------
# SERVE UPLOADED FILES
# -----------------------
@app.route("/uploads/<path:filename>")
def uploaded_file(filename):
    return send_from_directory(THUMB_FOLDER, filename)

@app.route("/delete/<filename>", methods=["POST"])
def delete_file(filename):
    file_path = os.path.join(THUMB_FOLDER, filename)

    # security check (prevents path traversal)
    if not os.path.exists(file_path):
        abort(404)

    try:
        os.remove(file_path)
    except OSError:
        abort(500)

    return redirect(url_for("gallery"))

# -----------------------
# RUN
# -----------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
