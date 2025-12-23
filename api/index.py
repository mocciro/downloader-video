import os
from flask import Flask, render_template, request
import yt_dlp

# Mengatur folder template agar Flask bisa menemukan file index.html
app = Flask(__name__, template_folder='../templates')

@app.route('/', methods=['GET', 'POST'])
def home():
    video_info = None
    if request.method == 'POST':
        url = request.form.get('url_video')
        
        # Konfigurasi Anti-Blokir & Paksa Format MP4 (Ada Suara)
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
            'format': 'best[ext=mp4]/best',  # Kunci agar ada suara
            'nocheckcertificate': True,
            'ignoreerrors': True,
            'geo_bypass': True,
            # Menyamar sebagai browser PC agar tidak diblokir YouTube/TikTok
            'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'referer': 'https://www.google.com/',
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                if info:
                    video_info = info
                else:
                    video_info = {'error': 'Gagal mengambil data video.'}
        except Exception as e:
            video_info = {'error': str(e)}
            
    return render_template('index.html', video=video_info)

# Penting untuk Vercel Serverless Function
app = app
