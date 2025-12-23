import os
from flask import Flask, render_template, request
import yt_dlp

# Mengatur folder template agar Flask bisa menemukan file index.html di folder /templates
app = Flask(__name__, template_folder='../templates')

@app.route('/', methods=['GET', 'POST'])
def home():
    video_info = None
    if request.method == 'POST':
        url = request.form.get('url_video')
        
        # Konfigurasi YDL_OPTS untuk mengatasi suara hilang dan error 403
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
            # 'format' ini memaksa pencarian file MP4 yang sudah menyatu (video+audio)
            'format': 'best[ext=mp4]/best',
            # User-agent untuk meniru browser asli agar tidak diblokir YouTube/TikTok
            'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'nocheckcertificate': True,
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                # Mengambil informasi video tanpa mendownload ke server
                video_info = ydl.extract_info(url, download=False)
        except Exception as e:
            # Jika ada error, kita buat pesan sederhana agar aplikasi tidak crash
            video_info = {'error': str(e)}
            
    return render_template('index.html', video=video_info)

# Variabel aplikasi untuk Vercel
app = app
