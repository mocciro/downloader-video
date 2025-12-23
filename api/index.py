import os
from flask import Flask, render_template, request
import yt_dlp

# Seting folder template agar bisa terbaca dari folder api
app = Flask(__name__, template_folder='../templates')

# Penting untuk Vercel
app.debug = True

@app.route('/', methods=['GET', 'POST'])
def home():
    video_info = None
    if request.method == 'POST':
        url = request.form.get('url_video')
        # Konfigurasi agar ada suara dan pencarian cepat
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
            'format': 'best[ext=mp4]/best',
        }
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                video_info = ydl.extract_info(url, download=False)
        except Exception as e:
            print(f"Error: {e}")
            
    return render_template('index.html', video=video_info)

# Ini variabel yang dicari Vercel
app = app
