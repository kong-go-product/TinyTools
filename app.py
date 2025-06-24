from flask import Flask, request, send_file, render_template
import os
import subprocess
import uuid


app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/convert", methods=["POST"])
def convert():
    uploaded_file = request.files.get("file")
    if not uploaded_file or not uploaded_file.filename.endswith(".mp4"):
        return {"error": "Please upload a .mp4 file"}, 400

    file_id = str(uuid.uuid4())
    input_path = os.path.join(UPLOAD_FOLDER, f"{file_id}.mp4")
    output_path = os.path.join(UPLOAD_FOLDER, f"{file_id}.mp3")

    uploaded_file.save(input_path)

    try:
        subprocess.run(
            ["ffmpeg", "-i", input_path, "-vn", "-acodec", "libmp3lame", output_path],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return send_file(output_path, as_attachment=True)
    except Exception as e:
        return {"error": f"Conversion failed: {str(e)}"}, 500
    finally:
        os.remove(input_path)
        if os.path.exists(output_path):
            os.remove(output_path)

if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))  # Render 会提供 PORT 环境变量
    app.run(host="0.0.0.0", port=port, debug=True)
    # app.run(debug=True, port=5000)