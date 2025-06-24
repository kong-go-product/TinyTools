# MP4 to MP3 Converter (Flask + FFmpeg)

A simple cloud-powered API to convert uploaded `.mp4` videos into `.mp3` audio files.

## 🚀 How to Deploy (on Render)

1. Fork or clone this repo
2. Push it to your GitHub
3. Go to https://render.com, create a Web Service
4. Choose this repo
5. Done — you'll get a live API at `https://your-app.onrender.com`

## 🧪 Test API (with curl)

```bash
curl -F "file=@yourfile.mp4" https://tinytools-3bj7.onrender.com/convert --output output.mp3