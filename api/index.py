import os
from flask import Flask, render_template, request
import yt_dlp

app = Flask(__name__, template_folder='../templates')

@app.route('/', methods=['GET', 'POST'])
def home():
    video_info = None
    if request.method == 'POST':
        url = request.form.get('url_video')
        
        # Pengaturan untuk menembus blokir dan memastikan ada suara
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
            'format': 'best[ext=mp4]/best',
            'nocheckcertificate': True,
            'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'referer': 'https://www.google.com/',
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                video_info = ydl.extract_info(url, download=False)
        except Exception as e:
            video_info = {'error': str(e)}
            
    return render_template('index.html', video=video_info)

app = app
